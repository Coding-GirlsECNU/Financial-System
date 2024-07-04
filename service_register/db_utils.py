import redis

r = redis.Redis(host='106.75.239.46', port=6379, decode_responses=True,
                password='zzh0117.', db=1)

def get_redis():
    try:
        yield r
    finally:
        r.close()

def get_model_url(model:str):
    r = next(get_redis())
    return r.get(model)

def set_model_url(model:str, url:str):
    try:
        r = next(get_redis())
        r.set(model,url)
        return True
    except Exception as e:
        return False




