#!/usr/bin/env python

def binary_search(values, key):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) / 2
        
        if key < values[mid]:
            high = mid - 1
        elif key > values[mid]:
            low = mid + 1
        else:
            return mid

    return -1

if __name__ == '__main__':
    test_data = [
    ([1, 2, 3, 4, 5], 1, 0),
    ([1, 2, 3, 4, 5], 5, 4),
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 6, -1),
    ([], 1, -1),
    ]
    for item in test_data:
        values, key, expected = item
        real = binary_search(values, key)
        if real == expected:
            print 'PASS: {item}'.format(item=item)
        else:
            print 'FAIL: {item}'.format(item=item)

    print 'DONE.'


    