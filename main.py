import asyncio
import sys
import aiofiles
import os
import json
from app.db.repository import save_cve_to_db
from app.db.config import get_db


async def process_cve_file(user_path: str):
    async with aiofiles.open(user_path, 'r', encoding='utf-8') as file:
        file_content = await file.read()
        data = json.loads(file_content)
        return data


async def process_directory(directory_path: str):
    async with get_db() as session:
        tasks = []

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    task = process_cve_file(file_path)
                    tasks.append(task)

        batch_data = await asyncio.gather(*tasks)
        await save_cve_to_db(session, batch_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_json_files>")
        sys.exit(1)

    directory_path = sys.argv[1]
    asyncio.run(process_directory(directory_path))
