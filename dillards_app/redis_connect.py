"""Redis instance with connection settings."""
import redis


redis_inst = redis.Redis(host='localhost', port=6379, db=0)
