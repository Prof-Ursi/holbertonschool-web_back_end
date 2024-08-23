#!/usr/bin/env python3
""" Module that changes all topics of a school document based on the name. """


def update_topics(mongo_collection, name, topics):
    """
    Description:
    ------------
        Update topics in documents of the specified MongoDB collection.

    Args:
    -----
    mongo_collection:
        The MongoDB collection containing documents to update.
    name(string):
        The name identifying the documents to be updated.
    topics(list[string]):
        the list of topics approached in the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
