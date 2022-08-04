#!/usr/bin/python3
""" lockboxes challenge """


def canUnlockAll(boxes):
    """this function return True if each array has the key
        that permit to get into the respective array.
    """

    array = []
    for x in boxes[0]:
        array.append(x)

    for date in array:
        for y in boxes[date]:
            if y in array or y > len(boxes):
                pass
            else:
                array.append(y)
        i = 0
        for vacio in boxes:

            if not vacio:
                i = i + 1
        pass
    print(array)
    if len(boxes) - i == len(array):
        return True
    return False
