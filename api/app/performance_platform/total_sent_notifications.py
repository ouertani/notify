from datetime import timedelta

from app import performance_platform_client
from app.dao.notifications_dao import get_total_sent_notifications_in_date_range
from app.utils import get_sydney_midnight_in_utc, convert_utc_to_aet


def send_total_notifications_sent_for_day_stats(date, notification_type, count):
    payload = performance_platform_client.format_payload(
        dataset='notifications',
        date=date,
        group_name='channel',
        group_value=notification_type,
        count=count
    )

    performance_platform_client.send_stats_to_performance_platform(payload)


def get_total_sent_notifications_for_day(day):
    """
     :day a UTC datetime
    """
    day_in_aet = convert_utc_to_aet(day)
    start_date = get_sydney_midnight_in_utc(day_in_aet)
    end_date = start_date + timedelta(days=1)

    email_count = get_total_sent_notifications_in_date_range(start_date, end_date, 'email')
    sms_count = get_total_sent_notifications_in_date_range(start_date, end_date, 'sms')
    letter_count = get_total_sent_notifications_in_date_range(start_date, end_date, 'letter')

    return {
        "start_date": start_date,
        "email": {
            "count": email_count
        },
        "sms": {
            "count": sms_count
        },
        "letter": {
            "count": letter_count
        },
    }
