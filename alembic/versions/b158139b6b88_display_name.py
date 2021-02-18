"""display_name

Revision ID: b158139b6b88
Revises: eea46f6d8a42
Create Date: 2021-01-28 13:21:10.505062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b158139b6b88'
down_revision = 'eea46f6d8a42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('display_name', sa.String(length=255), nullable=False))
    op.drop_constraint('user_username_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['display_name'])
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_username_key', 'user', ['username'])
    op.drop_column('user', 'display_name')
    # ### end Alembic commands ###