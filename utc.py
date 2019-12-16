from datetime import datetime, timezone

# datetime utc
# https://blog.ganssle.io/articles/2019/11/utcnow.html

ts = 1571595618.0

x = datetime.fromtimestamp(ts, tz = timezone.utc)
x_ts = x.timestamp()

assert ts == x_ts, f"{ts} != {x_ts}" # it should succeed

# now() with timezone
now = datetime.now()
utc = datetime.now(tz=timezone.utc)

print(f"now={now}")
print(f"utc={utc}")