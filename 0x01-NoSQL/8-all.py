#!/usr/bin/env python3
"""First commit."""


def list_all(mongo_collection):
    """Returns a list of all documents in a collection"""
    documents = mongo_collection.find()
    all_documents = []

    for document in documents:
        all_documents.append(document)

    return all_documents
