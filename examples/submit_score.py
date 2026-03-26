from golden_records import GoldenRecord, ScoreDetails, DistanceScore

client = GoldenRecord(
    api_key="your-api-key",
    base_url="https://api.goldenrecords.com"
)

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

print(client.scores.submit_score(score))