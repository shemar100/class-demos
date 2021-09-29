"""empty message

Revision ID: 66eac7894e71
Revises: 696fcd5d143c
Create Date: 2021-09-28 19:07:33.453783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66eac7894e71'
down_revision = '696fcd5d143c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todo', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todo', 'todolist', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'list_id')
    op.drop_table('todolist')
    # ### end Alembic commands ###