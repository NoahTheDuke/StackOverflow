import random
import timeit
from functools import partial

def strand_sort(array):
    if len(array) < 2:
        return array
    result = []

    while array:
        sublist = [array.pop()]
        leftovers = []
        for item in array:
            if item > sublist[-1]:
                sublist.append(item)
            else:
                leftovers.append(item)
        result = merge(result, sublist)
        array = leftovers
    return result

#def merge(left, right):
    #i = 0
    #j = 0
    #merged_list = []
    #while i < len(left) and j < len(right):
        #if left[i] > right[j]:
            #merged_list.append(right[j])
            #j += 1
        #else:
            #merged_list.append(left[i])
            #i += 1
    #merged_list += left[i:]
    #merged_list += right[j:]
    #return merged_list

def merge(left, right):
    merged_list = []
    it_left = iter(left)
    it_right = iter(right)
    left = next(it_left, None)
    right = next(it_right, None)

    while left is not None and right is not None:
        if left > right:
            merged_list.append(right)
            right = next(it_right, None)
        else:
            merged_list.append(left)
            left = next(it_left, None)
    if left:
        merged_list.append(left)
        merged_list.extend(i for i in it_left)
    else:
        merged_list.append(right)
        merged_list.extend(i for i in it_right)
    return merged_list


#@profile
def merge2(l1, l2):
    if not l1: return l2
    if not l2: return l1

    if l1[-1] > l2[-1]:
        l1, l2 = l2, l1

    it = iter(l2)
    y = next(it)
    result = []

    for x in l1:
        while y < x:
            result.append(y)
            y = next(it)
        result.append(x)
    result.append(y)
    result.extend(it)
    return result

def strand_sort_reddit(array):
    if len(array) < 2:
        return array
    result = []
    while array:
        sublist = [array.pop()]
        sub_append = sublist.append
        leftovers = []
        left_append = leftovers.append
        for item in array:
            if item > sublist[-1]:
                sub_append(item)
            else:
                left_append(item)
        result = merge_reddit(result, sublist)
        array = leftovers
    return result

def merge_reddit(left, right):
    merged_list = []
    merged_list_append = merged_list.append

    it_left = iter(left)
    it_right = iter(right)

    left = next(it_left, None)
    right = next(it_right, None)

    while left is not None and right is not None:
        if left > right:
            merged_list_append(right)
            right = next(it_right, None)
        else:
            merged_list_append(left)
            left = next(it_left, None)

    if left:
        merged_list_append(left)
        merged_list.extend(i for i in it_left)
    else:
        merged_list_append(right)
        merged_list.extend(i for i in it_right)

    return merged_list

#ls = list(range(10))
#random.shuffle(ls)
#print(strand_sort2(list(ls)))
#print(strand_sort3(list(ls)))

if __name__ == '__main__':
    ls  = list(range(10))
    random.shuffle(ls)
    times = timeit.Timer(partial(strand_sort, list(ls))).repeat(3, 10000)
    print("strand merge {}".format(min(times) / 100))
    print(sorted(list(ls)) == strand_sort(list(ls)))
    times = timeit.Timer(partial(strand_sort_reddit, list(ls))).repeat(3, 10000)
    print("strand merge {}".format(min(times) / 100))
    print(sorted(list(ls)) == strand_sort_reddit(list(ls)))
