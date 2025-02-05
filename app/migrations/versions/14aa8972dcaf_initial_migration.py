"""Initial migration

Revision ID: 14aa8972dcaf
Revises: 
Create Date: 2024-12-02 20:16:48.609186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14aa8972dcaf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('action', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_logs_id'), 'logs', ['id'], unique=False)
    op.create_table('rates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cargo_type', sa.String(), nullable=True),
    sa.Column('declared_value', sa.Float(), nullable=True),
    sa.Column('rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rates_cargo_type'), 'rates', ['cargo_type'], unique=False)
    op.create_index(op.f('ix_rates_id'), 'rates', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rates_id'), table_name='rates')
    op.drop_index(op.f('ix_rates_cargo_type'), table_name='rates')
    op.drop_table('rates')
    op.drop_index(op.f('ix_logs_id'), table_name='logs')
    op.drop_table('logs')
    # ### end Alembic commands ###
