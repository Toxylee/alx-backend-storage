#!/usr/bin/env python3
'''Module: Task 10
'''


def update_topics(mongo_collection, name, topics):
    '''changes all topics of a collection's document based on the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
