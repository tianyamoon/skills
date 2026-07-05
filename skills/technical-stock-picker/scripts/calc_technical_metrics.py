#!/usr/bin/env python3
"""Calculate technical metrics from stock K-line JSON."""

from __future__ import annotations

import argparse
import calendar
import json
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable


DATE_KEYS = ("date", "日期", "day", "trade_date")
OPEN_KEYS = ("open", "开盘")
HIGH_KEYS = ("high", "最高")
LOW_KEYS = ("low", "最低")
CLOSE_KEYS = ("close", "收盘", "latest")
VOLUME_KEYS = ("volume", "vol", "成交量")
AMOUNT_KEYS = ("amount", "成交额")
TURNOVER_KEYS = ("turnover", "turnover_rate", "换手率")


@dataclass
class Bar:
    dt: date
    open: float
    high: float
    low: float
    close: float
    volume: float | None = None
    amount: float | None = None
    turnover: float | None = None


def load_json(path: str) -> Any:
    if path == "-":
        import sys

        return json.load(sys.stdin)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def unwrap_rows(payload: Any) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("data", "rows", "items", "result", "klines"):
            value = payload.get(key)
            if isinstance(value, list):
                return value
    raise ValueError("unsupported JSON structure: expected list or object with data/rows/items/result/klines")


def pick_value(row: dict[str, Any], keys: Iterable[str], default: Any = None) -> Any:
    for key in keys:
        if key in row and row[key] not in (None, ""):
            return row[key]
    return default


def parse_date(raw: Any) -> date:
    if isinstance(raw, (int, float)):
        raw = str(int(raw))
    text = str(raw).strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y%m%d", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"unsupported date format: {raw}")


def to_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).replace(",", "").strip()
    if not text:
        return None
    return float(text)


def normalize_rows(rows: list[Any]) -> list[Bar]:
    normalized: list[Bar] = []
    for item in rows:
        if not isinstance(item, dict):
            raise ValueError("each row must be an object")
        dt = parse_date(pick_value(item, DATE_KEYS))
        open_value = to_float(pick_value(item, OPEN_KEYS))
        high_value = to_float(pick_value(item, HIGH_KEYS))
        low_value = to_float(pick_value(item, LOW_KEYS))
        close_value = to_float(pick_value(item, CLOSE_KEYS))
        if None in (open_value, high_value, low_value, close_value):
            raise ValueError(f"row on {dt} missing open/high/low/close")
        normalized.append(
            Bar(
                dt=dt,
                open=open_value,
                high=high_value,
                low=low_value,
                close=close_value,
                volume=to_float(pick_value(item, VOLUME_KEYS)),
                amount=to_float(pick_value(item, AMOUNT_KEYS)),
                turnover=to_float(pick_value(item, TURNOVER_KEYS)),
            )
        )
    normalized.sort(key=lambda bar: bar.dt)
    return normalized


def aggregate_period(daily: list[Bar], mode: str) -> list[Bar]:
    groups: dict[tuple[int, int], list[Bar]] = {}
    for bar in daily:
        if mode == "weekly":
            iso = bar.dt.isocalendar()
            key = (iso.year, iso.week)
        elif mode == "monthly":
            key = (bar.dt.year, bar.dt.month)
        else:
            raise ValueError(f"unsupported mode: {mode}")
        groups.setdefault(key, []).append(bar)

    result: list[Bar] = []
    for key in sorted(groups):
        rows = groups[key]
        result.append(
            Bar(
                dt=rows[-1].dt,
                open=rows[0].open,
                high=max(row.high for row in rows),
                low=min(row.low for row in rows),
                close=rows[-1].close,
                volume=sum(row.volume or 0.0 for row in rows) or None,
                amount=sum(row.amount or 0.0 for row in rows) or None,
                turnover=sum(row.turnover or 0.0 for row in rows) or None,
            )
        )
    return result


def moving_average(values: list[float], window: int) -> list[float | None]:
    result: list[float | None] = []
    for index in range(len(values)):
        if index + 1 < window:
            result.append(None)
            continue
        segment = values[index + 1 - window : index + 1]
        result.append(sum(segment) / window)
    return result


def pct_change(values: list[float], periods: int) -> float | None:
    if len(values) <= periods:
        return None
    base = values[-periods - 1]
    if base == 0:
        return None
    return values[-1] / base - 1


def average_or_none(values: list[float | None]) -> float | None:
    filtered = [value for value in values if value is not None]
    if not filtered:
        return None
    return sum(filtered) / len(filtered)


def last_n(values: list[Any], count: int) -> list[Any]:
    return values[-count:] if len(values) >= count else values[:]


def month_is_incomplete(latest_day: date) -> bool:
    month_days = calendar.monthrange(latest_day.year, latest_day.month)[1]
    return latest_day.day != month_days


def round_or_none(value: float | None, digits: int = 4) -> float | None:
    if value is None:
        return None
    return round(value, digits)


def compute_metrics(daily: list[Bar], weekly: list[Bar], monthly: list[Bar]) -> dict[str, Any]:
    daily_closes = [bar.close for bar in daily]
    weekly_closes = [bar.close for bar in weekly]
    monthly_closes = [bar.close for bar in monthly]

    ma20w_series = moving_average(weekly_closes, 20)
    ma6m_series = moving_average(monthly_closes, 6)
    ma12m_series = moving_average(monthly_closes, 12)

    monthly_reasons: list[str] = []
    monthly_score = 0
    latest_month_close = monthly_closes[-1] if monthly_closes else None
    latest_ma6 = ma6m_series[-1] if ma6m_series else None
    latest_ma12 = ma12m_series[-1] if ma12m_series else None
    prev_ma6 = ma6m_series[-2] if len(ma6m_series) >= 2 else None

    if latest_month_close is not None and latest_ma6 is not None and latest_month_close >= latest_ma6:
        monthly_score += 1
        monthly_reasons.append("最新月收盘在6月线之上")
    if latest_ma6 is not None and prev_ma6 is not None and latest_ma6 >= prev_ma6:
        monthly_score += 1
        monthly_reasons.append("6月线继续上行")
    if latest_month_close is not None and latest_ma12 is not None and latest_month_close >= latest_ma12:
        monthly_score += 1
        monthly_reasons.append("最新月收盘在12月线之上")

    if monthly_score >= 2:
        monthly_trend = "up"
    elif monthly_score == 1:
        monthly_trend = "watch"
    else:
        monthly_trend = "down"

    weekly_reasons: list[str] = []
    weekly_score = 0
    latest_week_close = weekly_closes[-1] if weekly_closes else None
    latest_ma20w = ma20w_series[-1] if ma20w_series else None
    prev_ma20w = ma20w_series[-2] if len(ma20w_series) >= 2 else None

    if latest_week_close is not None and latest_ma20w is not None and latest_week_close >= latest_ma20w:
        weekly_score += 1
        weekly_reasons.append("最新周收盘在20周线之上")
    if latest_ma20w is not None and prev_ma20w is not None and latest_ma20w >= prev_ma20w:
        weekly_score += 1
        weekly_reasons.append("20周线继续上行")
    if len(weekly_closes) >= 4 and len(ma20w_series) >= 4:
        recent = list(zip(last_n(weekly_closes, 4), last_n(ma20w_series, 4)))
        valid = [close >= ma for close, ma in recent if ma is not None]
        if valid and sum(valid) >= max(1, len(valid) - 1):
            weekly_score += 1
            weekly_reasons.append("最近4周大多数收盘仍在20周线之上")

    if weekly_score >= 2:
        weekly_trend = "up"
    elif weekly_score == 1:
        weekly_trend = "watch"
    else:
        weekly_trend = "down"

    latest_daily = daily[-1]
    latest_close = latest_daily.close
    latest_date = latest_daily.dt.isoformat()

    deviation_basis = "dynamic_monthly" if month_is_incomplete(latest_daily.dt) else "closed_monthly"
    deviation_6m = latest_close / latest_ma6 - 1 if latest_ma6 else None
    deviation_12m = latest_close / latest_ma12 - 1 if latest_ma12 else None

    daily_returns = {
        "ret_5d": pct_change(daily_closes, 5),
        "ret_20d": pct_change(daily_closes, 20),
        "ret_60d": pct_change(daily_closes, 60),
    }

    ytd_base = None
    for bar in daily:
        if bar.dt.year == latest_daily.dt.year:
            ytd_base = bar.close
            break
    ytd_return = latest_close / ytd_base - 1 if ytd_base else None

    highs_60 = [bar.high for bar in last_n(daily, 60)]
    lows_20 = [bar.low for bar in last_n(daily, 20)]
    distance_to_60d_high = latest_close / max(highs_60) - 1 if highs_60 else None
    support_20d = min(lows_20) if lows_20 else None
    resistance_60d = max(highs_60) if highs_60 else None

    vol_ratio = None
    amount_ratio = None
    daily_volumes = [bar.volume for bar in daily]
    daily_amounts = [bar.amount for bar in daily]
    if len(daily) >= 20:
        volume_20 = average_or_none(last_n(daily_volumes, 20))
        amount_20 = average_or_none(last_n(daily_amounts, 20))
        if volume_20:
            vol_ratio = average_or_none(last_n(daily_volumes, 5)) / volume_20
        if amount_20:
            amount_ratio = average_or_none(last_n(daily_amounts, 5)) / amount_20

    if monthly_trend != "up" or weekly_trend != "up":
        execution_hint = "watch_only"
    elif deviation_6m is not None and deviation_6m > 0.60:
        execution_hint = "too_extended"
    elif deviation_12m is not None and deviation_12m > 1.00:
        execution_hint = "too_extended"
    elif deviation_6m is not None and deviation_6m >= 0.40:
        execution_hint = "wait_for_pullback"
    elif distance_to_60d_high is not None and distance_to_60d_high <= -0.15:
        execution_hint = "high_level_divergence"
    elif daily_returns["ret_20d"] is not None and daily_returns["ret_20d"] > 0 and daily_returns["ret_60d"] is not None and daily_returns["ret_60d"] > 0:
        execution_hint = "trend_active"
    else:
        execution_hint = "wait_for_confirmation"

    data_gaps: list[str] = []
    if len(daily) < 61:
        data_gaps.append("daily_under_61_bars")
    if len(weekly) < 20:
        data_gaps.append("weekly_under_20_bars")
    if len(monthly) < 12:
        data_gaps.append("monthly_under_12_bars")

    return {
        "as_of": latest_date,
        "basis": {
            "monthly_deviation_basis": deviation_basis,
            "daily_bars": len(daily),
            "weekly_bars": len(weekly),
            "monthly_bars": len(monthly),
        },
        "monthly": {
            "trend": monthly_trend,
            "score": monthly_score,
            "reasons": monthly_reasons,
            "close": round_or_none(latest_month_close),
            "ma6": round_or_none(latest_ma6),
            "ma12": round_or_none(latest_ma12),
            "deviation_6m": round_or_none(deviation_6m),
            "deviation_12m": round_or_none(deviation_12m),
        },
        "weekly": {
            "trend": weekly_trend,
            "score": weekly_score,
            "reasons": weekly_reasons,
            "close": round_or_none(latest_week_close),
            "ma20w": round_or_none(latest_ma20w),
        },
        "daily": {
            "close": round_or_none(latest_close),
            "ret_5d": round_or_none(daily_returns["ret_5d"]),
            "ret_20d": round_or_none(daily_returns["ret_20d"]),
            "ret_60d": round_or_none(daily_returns["ret_60d"]),
            "ret_ytd": round_or_none(ytd_return),
            "distance_to_60d_high": round_or_none(distance_to_60d_high),
        },
        "volume_price": {
            "volume_ratio_5_20": round_or_none(vol_ratio),
            "amount_ratio_5_20": round_or_none(amount_ratio),
        },
        "levels": {
            "support_20d_low": round_or_none(support_20d),
            "resistance_60d_high": round_or_none(resistance_60d),
            "first_invalidation": round_or_none(support_20d),
        },
        "execution_hint": execution_hint,
        "data_gaps": data_gaps,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate technical metrics from stock K-line JSON.")
    parser.add_argument("--daily", required=True, help="Path to daily K-line JSON. Use - for stdin.")
    parser.add_argument("--weekly", help="Optional path to weekly K-line JSON.")
    parser.add_argument("--monthly", help="Optional path to monthly K-line JSON.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    daily_rows = unwrap_rows(load_json(args.daily))
    daily = normalize_rows(daily_rows)
    weekly = normalize_rows(unwrap_rows(load_json(args.weekly))) if args.weekly else aggregate_period(daily, "weekly")
    monthly = normalize_rows(unwrap_rows(load_json(args.monthly))) if args.monthly else aggregate_period(daily, "monthly")

    metrics = compute_metrics(daily, weekly, monthly)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
