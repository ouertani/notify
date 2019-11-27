"""

Revision ID: 0237
Revises: 0236
Create Date: 2019-11-27 12:43:25.440354

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
import uuid


revision = '0237'
down_revision = '0236'


def upgrade():
    op.execute("""
    DELETE FROM provider_statistics WHERE provider_id IN (
        SELECT * FROM (
            SELECT id FROM provider_details WHERE identifier = 'mmg' OR identifier = 'firetext'
        ) AS p
    )
""")

    op.execute("""
    DELETE FROM provider_rates WHERE provider_id IN (
        SELECT * FROM (
            SELECT id FROM provider_details WHERE identifier = 'mmg' OR identifier = 'firetext'
        ) AS p
    )
""")

    op.execute("DELETE FROM provider_details WHERE identifier = 'mmg' OR identifier = 'firetext'")

    op.execute("DELETE FROM provider_details_history where identifier = 'mmg' OR identifier = 'firetext'")


def downgrade():
    op.execute(
        "INSERT INTO provider_details (id, display_name, identifier, priority, notification_type, active, supports_international, version) values ('{}', 'MMG', 'mmg', 20, 'sms', false, false, 1)".format(str(uuid.uuid4()))
    )

    op.execute((
        "INSERT INTO provider_rates (id, valid_from, rate, provider_id) VALUES ('{}', '{}', 1.8, "
        "(SELECT id FROM provider_details WHERE identifier = 'mmg'))").format(uuid.uuid4(), datetime.utcnow()))

    op.execute(
        """
        INSERT INTO provider_details_history (id, display_name, identifier, priority, notification_type, active, supports_international, version)
        SELECT id, display_name, identifier, priority, notification_type, active, supports_international, version FROM provider_details WHERE identifier = 'mmg'
        """
    )

    op.execute(
        "INSERT INTO provider_details (id, display_name, identifier, priority, notification_type, active, supports_international, version) values ('{}', 'Firetext', 'firetext', 20, 'sms', false, false, 1)".format(str(uuid.uuid4()))
    )

    op.execute((
        "INSERT INTO provider_rates (id, valid_from, rate, provider_id) VALUES ('{}', '{}', 2.5, "
        "(SELECT id FROM provider_details WHERE identifier = 'firetext'))").format(uuid.uuid4(), datetime.utcnow()))

    op.execute(
        """
        INSERT INTO provider_details_history (id, display_name, identifier, priority, notification_type, active, supports_international, version)
        SELECT id, display_name, identifier, priority, notification_type, active, supports_international, version FROM provider_details WHERE identifier = 'firetext'
        """
    )
