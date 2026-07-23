"""Add is_active column to students (Revision 002)

Revision ID: 002_add_is_active_to_students
Revises: 001_initial_schema
Create Date: 2026-07-23 11:35:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '002_add_is_active_to_students'
down_revision: Union[str, None] = '001_initial_schema'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Task 2 Step 98, 100: Add is_active column to students table
    op.add_column(
        'students',
        sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False)
    )


def downgrade() -> None:
    # Rollback operation: drop column is_active from students table
    op.drop_column('students', 'is_active')
