"""never

Revision ID: 312d90263f10
Revises: 6dd89da21944
Create Date: 2023-11-18 01:13:27.541577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '312d90263f10'
down_revision = '6dd89da21944'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lots',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('start_bet', sa.Integer(), nullable=False),
    sa.Column('winner_uid', sa.Uuid(), nullable=True),
    sa.Column('current_bet', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('closed_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['winner_uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('winner_uid')
    )
    op.create_foreign_key(None, 'users_lots', 'lots', ['lot_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users_lots', type_='foreignkey')
    op.drop_table('lots')
    # ### end Alembic commands ###
