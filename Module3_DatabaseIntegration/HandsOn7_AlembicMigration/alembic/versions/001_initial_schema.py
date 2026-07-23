"""Initial schema creation (Revision 001)

Revision ID: 001_initial_schema
Revises: 
Create Date: 2026-07-23 11:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '001_initial_schema'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Create departments table
    op.create_table(
        'departments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('dept_name', sa.String(length=100), nullable=False),
        sa.Column('head_of_dept', sa.String(length=100), nullable=False),
        sa.Column('budget', sa.Float(), nullable=False, server_default='0.0'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('dept_name')
    )
    op.create_index(op.f('ix_departments_id'), 'departments', ['id'], unique=False)

    # 2. Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('course_name', sa.String(length=150), nullable=False),
        sa.Column('course_code', sa.String(length=20), nullable=False),
        sa.Column('credits', sa.Integer(), nullable=False, server_default='3'),
        sa.Column('department_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('course_code')
    )
    op.create_index(op.f('ix_courses_course_code'), 'courses', ['course_code'], unique=True)
    op.create_index(op.f('ix_courses_id'), 'courses', ['id'], unique=False)

    # 3. Create students table
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('date_of_birth', sa.Date(), nullable=False),
        sa.Column('enrollment_year', sa.Integer(), nullable=False, server_default='2026'),
        sa.Column('department_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_students_email'), 'students', ['email'], unique=True)
    op.create_index(op.f('ix_students_id'), 'students', ['id'], unique=False)

    # 4. Create enrollments table
    op.create_table(
        'enrollments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.Column('enrollment_date', sa.Date(), nullable=False),
        sa.Column('grade', sa.String(length=5), nullable=True),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('student_id', 'course_id', name='uq_student_course')
    )
    op.create_index(op.f('ix_enrollments_id'), 'enrollments', ['id'], unique=False)

    # 5. Create professors table
    op.create_table(
        'professors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('prof_name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('department_id', sa.Integer(), nullable=False),
        sa.Column('salary', sa.Float(), nullable=False, server_default='0.0'),
        sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_professors_id'), 'professors', ['id'], unique=False)


def downgrade() -> None:
    op.drop_table('professors')
    op.drop_table('enrollments')
    op.drop_table('students')
    op.drop_table('courses')
    op.drop_table('departments')
