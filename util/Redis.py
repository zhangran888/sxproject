import redis

# 建立链接，链接redis服务
def redisVerfiy():
    POOL = redis.ConnectionPool(host="172.18.1.41", password="KFIRcQNRbvJb", port=6379, db=3, decode_responses=True)
    rs = redis.Redis(connection_pool=POOL)
    return rs


