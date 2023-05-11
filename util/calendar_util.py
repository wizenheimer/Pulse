import requests
import arrow
import pytz
from ics import Calendar
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def get_on_call(
    url=None,
    date=arrow.now(),
    timezone="utc",
    shift_day=0,
    shift_hour=0,
    shift_minute=0,
    shift_second=0,
):
    """
    The function queries the calendar and returns a timezone aware on-call list
    We can even specify the time difference with number of hours instead of timezone eg '-05:00'
    """
    # take the timezone
    if url is None:
        return []

    calendar = Calendar(requests.get(url).text)
    # convert the current date to a date in the calendar timezone
    begin_date = (
        arrow.get(date)
        .to(timezone)
        .shift(
            days=shift_day,
            hours=shift_hour,
            minutes=shift_minute,
            seconds=shift_second,
        )
    )

    # fetch the timeline at the specified date
    timeline = calendar.timeline.at(begin_date)

    on_call_list = []
    for event in timeline:
        # prepare the call list for the timeline
        email = event.name
        try:
            # check if there's only a single email address
            if validate_email(email):
                on_call_list.append(email)
        except ValidationError:
            # check if there's a list of emails in the event name
            email_list = email.split(",")
            for email in email_list:
                try:
                    if validate_email(email):
                        on_call_list.append(email)
                except ValidationError:
                    continue
    return on_call_list


def get_arrow_date(year, month, day, hour, minute, seconds, timezone="utc"):
    """
    Return the date as an arrow object
    """
    return arrow.Arrow(year, month, day, hour, minute, seconds).to(timezone)


def get_arrow_date(date, timezone="utc"):
    """
    Parses the date and return an arrow object
    """
    return arrow.get(date, "MMMM DD YYYY HH:mm").to(timezone)
