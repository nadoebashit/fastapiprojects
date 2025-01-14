from redis import Redis

redis = Redis(host="localhost", port=6379, decode_responses=True)

def get_from_cache(key):
    return redis.get(key)

def set_to_cache(key, value, ttl=3600):
    redis.set(key, value, ex=ttl)
