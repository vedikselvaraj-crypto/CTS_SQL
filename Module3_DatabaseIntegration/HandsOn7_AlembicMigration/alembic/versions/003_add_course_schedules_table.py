"""Add course_schedules table (Revision 003)

Revision ID: 003_add_course_schedules_table
Revises: 002_add_is_active_to_students
Create Date: 2026-07-23 11:40:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '003_add_course_schedules_table'
down_revision: Union[str, None] = '002_add_is_active_to_students'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Task 2 Step 102: Create course_schedules table
    op.create_table(
        'course_schedules',
        sa.Column('schedule_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.Column('day_of_week', sa.String(length=15), nullable=False),
        sa.Column('start_time', sa.String(length=10), nullable=False),
        sa.Column('end_time', sa.String(length=10), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.PrimaryKeyConstraint('schedule_id')
    )
    op.create_index(op.f('ix_course_schedules_schedule_id'), 'course_schedules', ['schedule_id'], unique=False)


def downgrade() -> None:
    # Rollback operation: drop course_schedules table
    op.drop_table('course_schedules')
