#!/usr/bin/env python3
"""
Module with a function that inserts a new document in a collection
base on specified keyword arguments.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Description:
    ------------
        Insert a new document into the specified MongoDB collection.

    Args:
    -----
    mongo_collection:
        The MongoDB collection to insert the document into.
    **kwargs:
        Keyword arguments representing the fields and values
        of the new document.

    Returns:
    --------
        The ObjectId of the newly inserted document.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
