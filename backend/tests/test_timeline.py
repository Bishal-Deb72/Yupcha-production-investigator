from app.services.timeline import reconstruct_timeline


sample = """

2026-06-21 10:15:20 INFO Payment Service Started

2026-06-21 10:17:31 ERROR Database Timeout

2026-06-21 10:18:05 ERROR Redis unavailable

2026-06-21 10:19:11 INFO Deployment v2.3 completed

"""


result = reconstruct_timeline(sample)


print(result)