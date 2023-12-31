"""never

Revision ID: b0b0a7c3fe50
Revises: 5e85753c303d
Create Date: 2023-12-04 23:39:06.537985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0b0a7c3fe50'
down_revision = '5e85753c303d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lots', sa.Column('is_active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lots', 'is_active')
    # ### end Alembic commands ###
