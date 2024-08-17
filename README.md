# Installation
1. ```git clone https://github.com/CVEProject/cvelistV5 --depth=1```
2. Fill .env file by .env .example
3. ```pip install -r requirements.txt```
4. ```docker-compose up -d --build```
5. ```alembic upgrade head```
6. ```python main.py /path/to/cves```
