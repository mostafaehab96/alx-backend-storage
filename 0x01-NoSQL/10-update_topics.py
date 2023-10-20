#!/usr/bin/env python3
"""Write a Python function that changes all topics of a school document based
on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    :param mongo_collection: will be the pymongo collection object
    :param name: (string) will be the school name to update
    :param topics: list of strings) will be the list of topics approached in
    the school
    """

    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
