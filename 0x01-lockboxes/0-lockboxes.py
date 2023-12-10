#!/usr/bin/python3
'''
    lockboxes interview challenge.
'''


def canUnlockAll(boxes):
    '''
        method that determines if all the boxes can be opened
    ''''
    n = len(boxes)
    keys = boxes[0]
    Locked_box = [False] + [True] * (n - 1)
    for key in keys:
        if ((key < n)) and (Locked_box[key] is True):
            Locked_box[key] = False
            keys.extend(boxes[key])
    return not any(Locked_box)
