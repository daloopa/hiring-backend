"""
Seed data helper for the backend coding challenge.

`generate_company_data()` returns a flat list of ~4,000 dicts representing
500 companies × 8 quarterly snapshots. Each dict has both company and
snapshot fields — i.e. company info (`ticker`, `name`) is repeated across
each company's 8 records.

The data is deterministic (seeded RNG) so it's reproducible across runs.
"""

import random
from datetime import date


_ADJ = [
    "Apex",
    "Vertex",
    "Stellar",
    "Pinnacle",
    "Quantum",
    "Beacon",
    "Orion",
    "Atlas",
    "Polaris",
    "Solstice",
    "Horizon",
    "Ridge",
    "Summit",
    "Crescent",
    "Aurora",
    "Cipher",
    "Helio",
    "Nexus",
    "Pulse",
    "Vortex",
]
_NOUN = [
    "Tech",
    "Health",
    "Energy",
    "Capital",
    "Logistics",
    "Bio",
    "Materials",
    "Pharma",
    "Media",
    "Foods",
    "Auto",
    "Chem",
    "Telecom",
    "Financial",
    "Industrial",
    "Robotics",
    "Networks",
    "Resources",
    "Solutions",
    "Systems",
]
_SUFFIX = [
    "Inc.",
    "Corp.",
    "Holdings",
    "Group",
    "& Co.",
    "Industries",
    "Ltd.",
    "Partners",
    "",
]

_PERIODS = [
    ("2023Q1", date(2023, 4, 15)),
    ("2023Q2", date(2023, 7, 15)),
    ("2023Q3", date(2023, 10, 15)),
    ("2023Q4", date(2024, 1, 15)),
    ("2024Q1", date(2024, 4, 15)),
    ("2024Q2", date(2024, 7, 15)),
    ("2024Q3", date(2024, 10, 15)),
    ("2024Q4", date(2025, 1, 15)),
]


def generate_company_data():
    """Return a deterministic list of ~4,000 company-snapshot dicts."""
    rng = random.Random(424242)
    used_tickers = set()
    records = []

    for _ in range(500):
        adj = rng.choice(_ADJ)
        noun = rng.choice(_NOUN)
        suffix = rng.choice(_SUFFIX)
        name = f"{adj} {noun} {suffix}".strip()

        ticker = (adj[:2] + noun[:2]).upper()
        dedup = 0
        while ticker in used_tickers:
            dedup += 1
            ticker = (adj[:2] + noun[:2]).upper() + str(dedup)
        used_tickers.add(ticker)

        revenue = 50_000_000 + rng.random() * 50_000_000_000
        base_margin = -0.30 + rng.random() * 0.55

        for period, reported in _PERIODS:
            growth = -0.10 + rng.random() * 0.30
            revenue *= 1 + growth

            margin_drift = (rng.random() - 0.5) * 0.05
            current_revenue = round(revenue, 2)
            current_margin = round(base_margin + margin_drift, 4)
            current_net_income = round(current_revenue * current_margin, 2)

            record = {
                "ticker": ticker,
                "name": name,
                "period": period,
                "revenue": current_revenue,
                "net_income": current_net_income,
                "margin": current_margin,
                "reported_at": reported,
            }

            r = rng.random()
            if r < 0.02:
                record["margin"] = None
            elif r < 0.04:
                record["net_income"] = None

            records.append(record)

    return records
