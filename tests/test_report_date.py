"""Tests for timezone-aware report dates."""

from datetime import datetime, timezone

from src.time_utils import report_date


def test_report_date_uses_configured_timezone(monkeypatch):
    monkeypatch.setenv("HORIZON_TIMEZONE", "Asia/Shanghai")
    instant = datetime(2026, 7, 27, 23, 30, tzinfo=timezone.utc)

    assert report_date(instant) == "2026-07-28"


def test_report_date_defaults_to_utc(monkeypatch):
    monkeypatch.delenv("HORIZON_TIMEZONE", raising=False)
    instant = datetime(2026, 7, 27, 23, 30, tzinfo=timezone.utc)

    assert report_date(instant) == "2026-07-27"
