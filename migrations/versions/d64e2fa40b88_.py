"""empty message

Revision ID: d64e2fa40b88
Revises: 92afc8158d15
Create Date: 2022-04-05 00:25:03.977220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd64e2fa40b88'
down_revision = '92afc8158d15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('user_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'book', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'user_id')
    # ### end Alembic commands ###