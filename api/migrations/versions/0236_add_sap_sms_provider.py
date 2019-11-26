"""

Revision ID: 0236
Revises: 0235
Create Date: 2019-11-26 11:24:31.565916

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
import uuid


revision = '0236'
down_revision = '0235'


def upgrade():
    op.execute(
        "INSERT INTO provider_details (id, display_name, identifier, priority, notification_type, active, supports_international, version) values ('{}', 'SAP', 'sap', 3, 'sms', true, true, 1)".format(str(uuid.uuid4()))
    )

    op.execute((
        "INSERT INTO provider_rates (id, valid_from, rate, provider_id) VALUES ('{}', '{}', 4.0, "
        "(SELECT id FROM provider_details WHERE identifier = 'sap'))").format(uuid.uuid4(), datetime.utcnow()))

    op.execute(
        """
        INSERT INTO provider_details_history (id, display_name, identifier, priority, notification_type, active, supports_international, version)
        SELECT id, display_name, identifier, priority, notification_type, active, supports_international, version FROM provider_details WHERE identifier = 'sap'
        """
    )


def downgrade():
    op.execute("""
    DELETE FROM provider_rates WHERE provider_id IN (
        SELECT * FROM (
            SELECT id FROM provider_details WHERE identifier = 'sap'
        ) AS p
    )
""")

    op.execute("DELETE FROM provider_details WHERE identifier = 'sap'")

    op.execute("DELETE FROM provider_details_history where identifier = 'sap'")
