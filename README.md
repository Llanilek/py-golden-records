# Golden Records Python SDK

Unofficial Python SDK for the Golden Records API.

## `Installation`

```bash
pip install py-golden-records
```

## `Quick Start`

```python
from golden_records import GoldenRecord, ScoreDetails, DistanceScore

client = GoldenRecord(api_key="your-api-key")

score = ScoreDetails(
    age_group_id="adult",
    class_id="recurve",
    date_shot="2026-03-25",
    location="Bolton",
    member_id="123",
    qualifying=True,
    record_qualifying=False,
    record_status=False,
    round_id="portsmouth",
    score=550,
    status=1,
    distances=[
        DistanceScore(distance="20y", score=550)
    ]
)

response = client.scores.submit_score(score)
```


## `Features`

- Typed models via Pydantic
- Clean service-based architecture
- Easy-to-use client interface

## `LICENSE`

```text
MIT License

Copyright (c) 2026 Unstrung Archery
```