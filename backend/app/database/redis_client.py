import redis

redis_client = redis.Redis(
    # default db0 or db=0
    host="localhost",
    port=6379,
    decode_responses=True
)

print(redis_client.ping())
