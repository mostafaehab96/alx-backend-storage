#!/usr/bin/env python3
"""Write a Python script that provides some stats about Nginx logs stored in
MongoDB

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT",
"PATCH", "DELETE"] in this order (see example below - warning: it’s a
tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
"""

from pymongo import MongoClient

if __name__ == "__main__":
    list_all = __import__('8-all').list_all
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    count = len(list_all(collection))
    print(f"{count} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = len(list(collection.find({"method": method})))
        print(f"\tmethod {method}: {method_count}")
    status = collection.find({"method": "GET", "path": "/status"})
    print(f"{len(list(status))} status check")

    pipeline = [
        {
            '$group': {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'count': -1},
        },
        {'$limit': 10}
    ]
    ips = list(collection.aggregate(pipeline))
    print("IPs:")
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
