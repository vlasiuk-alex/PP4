"""empty message

Revision ID: f16c8745778b
Revises: 
Create Date: 2020-12-23 02:54:07.884279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f16c8745778b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('uarticles',
    sa.Column('art_id', sa.Integer(), nullable=False),
    sa.Column('us_id', sa.Integer(), nullable=True),
    sa.Column('mod_id', sa.Integer(), nullable=True),
    sa.Column('ed_text', sa.String(), nullable=True),
    sa.Column('ed_date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('art_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('ustatus', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('uarticles')
    op.drop_table('articles')
    # ### end Alembic commands ###
