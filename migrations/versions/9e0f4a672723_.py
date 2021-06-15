"""empty message

Revision ID: 9e0f4a672723
Revises: f88ac8035126
Create Date: 2021-06-14 13:08:47.507314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e0f4a672723'
down_revision = 'f88ac8035126'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('task_goal_id_fkey', 'task', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('task_goal_id_fkey', 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###
