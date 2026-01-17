"""empty message

Revision ID: d21d667e95d0
Revises: 352336723187
Create Date: 2026-01-14 18:47:24.703277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd21d667e95d0'
down_revision: Union[str, Sequence[str], None] = '352336723187'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
