"""Add published_date to Post

Revision ID: cd34624efd18
Revises: c2dc288dc36a
Create Date: 2024-10-15 10:32:45.234643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd34624efd18'
down_revision: Union[str, None] = 'c2dc288dc36a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('published_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'published_date')
    # ### end Alembic commands ###
