#!/usr/bin/env python3
""" Module with a function that lists all documents in a collection. """


def list_all(mongo_collection):
    """
    Description:
    ------------
        Retrieve all documents from the specified MongoDB collection.

    Args:
    -----
    mongo_collection:
        The MongoDB collection to retrieve documents from.

    Returns:
    --------
        An object containing all documents in the collection.
    """
    return mongo_collection.find()
