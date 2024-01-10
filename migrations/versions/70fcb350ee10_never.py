"""never

Revision ID: 70fcb350ee10
Revises: 18d463f4313f
Create Date: 2024-01-11 00:40:43.407097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70fcb350ee10'
down_revision = '18d463f4313f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lots', 'start_bet',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.drop_constraint('lots_winner_uid_key', 'lots', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('lots_winner_uid_key', 'lots', ['winner_uid'])
    op.alter_column('lots', 'start_bet',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
