#!/usr/bin/env python3

"""
Python function that returns all students sorted by average score:
"""


def top_students(mongo_collection):
    """
    :param mongo_collection: pymongo collection object
    :return: all students sorted by average score
    """
    result = mongo_collection.aggregate([
        {'$unwind': '$topics'},
        {
            "$group": {
                "_id": "$_id", "name": {'$first': '$name'}, "averageScore": {
                    "$avg":
                        "$topics.score"
                }
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return list(result)
