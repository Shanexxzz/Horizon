"""Timezone helpers for reader-facing report dates."""

import logging
import os
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

logger = logging.getLogger(__name__)


def report_date(now: datetime | None = None) -> str:
    """Return YYYY-MM-DD in HORIZON_TIMEZONE (UTC by default)."""
    instant = now or datetime.now(timezone.utc)
    if instant.tzinfo is None:
        instant = instant.replace(tzinfo=timezone.utc)

    timezone_name = os.environ.get("HORIZON_TIMEZONE", "UTC")
    try:
        target_timezone = ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError:
        if timezone_name == "Asia/Shanghai":
            # Some minimal Python distributions do not bundle the IANA
            # database. China has used UTC+08:00 year-round since 1991.
            target_timezone = timezone(timedelta(hours=8), name="Asia/Shanghai")
        else:
            logger.warning("Unknown HORIZON_TIMEZONE=%s; falling back to UTC.", timezone_name)
            target_timezone = timezone.utc

    return instant.astimezone(target_timezone).strftime("%Y-%m-%d")
