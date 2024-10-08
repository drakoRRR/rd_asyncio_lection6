"""cve_table

Revision ID: b9fc452fa3da
Revises: 
Create Date: 2024-08-17 18:45:18.270913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9fc452fa3da'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cve_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cve_id', sa.String(), nullable=False),
    sa.Column('published_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('problem_types', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cve_id')
    )
    op.create_index(op.f('ix_cve_records_id'), 'cve_records', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cve_records_id'), table_name='cve_records')
    op.drop_table('cve_records')
    # ### end Alembic commands ###
