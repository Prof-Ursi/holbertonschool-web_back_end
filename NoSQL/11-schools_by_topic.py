#!/usr/bin/env python3
""" Module that returns the list of school having a specific topic. """


def schools_by_topic(mongo_collection, topic):
    """
    Description:
    ------------
        Retrieve a list of schools from the specified
        MongoDB collection that have a specific topic.

    Args:
    -----
    mongo_collection:
        The MongoDB collection to search for schools.
    topic(string):
        The specific topic to filter schools by.

    Returns:
    --------
        An object containing the schools with the specified topic.
    """
    return mongo_collection.find({"topics": topic})
