"""empty message

Revision ID: ffc2103c720f
Revises: 0f1cac3e2ac7
Create Date: 2022-03-31 22:58:52.918160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffc2103c720f'
down_revision = '0f1cac3e2ac7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('condition', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('publisher', sa.String(length=50), nullable=True),
    sa.Column('publish_year', sa.String(length=50), nullable=True),
    sa.Column('categories', sa.String(length=50), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
