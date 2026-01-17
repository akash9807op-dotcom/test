"""create post table

Revision ID: 352336723187
Revises: 
Create Date: 2026-01-14 18:16:24.470881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '352336723187'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("age",sa.String(),nullable=False,default="23"))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","age")
    pass
