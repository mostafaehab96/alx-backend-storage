#!/usr/bin/env python3
"""Write a Python function that returns the list of school having a specific
topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    :param mongo_collection: the pymongo collection object
    :param topic: (string) will be topic searched
    :return: (list) of schools having a specific topic
    """

    result = mongo_collection.find({"topics": topic})
    schools = []

    for school in result:
        schools.append(school)

    return schools
