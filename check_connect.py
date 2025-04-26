import pymongo
import psycopg2
import pika
import redis
from typing import Dict

def test_connections() -> Dict[str, bool]:
    host = "hp.local"
    results = {}

    # MongoDB
    try:
        pymongo.MongoClient(f"mongodb://{host}:27017/").server_info()
        results["MongoDB"] = True
    except Exception as e:
        print(e)
        results["MongoDB"] = False

    # PostgreSQL
    try:
        psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="hp.local",
            port="5432"
        ).close()
        results["PostgreSQL"] = True
    except Exception as e:
        print(e)
        results["PostgreSQL"] = False

    # RabbitMQ
    try:
        pika.BlockingConnection(
            pika.ConnectionParameters(host='hp.local', port=5672)
        ).close()
        results["RabbitMQ"] = True
    except Exception as e:
        print(e)
        results["RabbitMQ"] = False

    # Redis
    try:
        redis.Redis(
                host='hp.local',
                port=6379,
                db=0,
                password='redis'
            ).ping()
        results["Redis"] = True
    except Exception as e:
        print(e)
        results["Redis"] = False

    return results

if __name__ == "__main__":
    results = test_connections()
    for service, status in results.items():
        print(f"{service}: {'Connected' if status else 'Failed'}")
