import random
import timeit
from functools import partial

def strand_sort(array):
    if len(array) < 2:
        return array
    result = []
    while array:
        i = 0
        sublist = []
        sublist.append(array.pop())
        while i < len(array):
            num = array[i]
            if num > sublist[-1]:
                sublist.append(num)
                del array[i]
            else:
                i = i + 1
        result = merge(list(result), sublist)
    return result

def merge(list_1, list_2):
    i = 0
    j = 0
    merged_list = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] > list_2[j]:
            merged_list.append(list_2[j])
            j += 1
        else:
            merged_list.append(list_1[i])
            i += 1
    merged_list += list_1[i:]
    merged_list += list_2[j:]
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

#ls = list(range(10))
#random.shuffle(ls)
#print(strand_sort2(list(ls)))
#print(strand_sort3(list(ls)))

if __name__ == '__main__':
    ls  = list(range(100000))
    random.shuffle(ls)
    times = timeit.Timer(partial(strand_sort, list(ls))).repeat(3, 10000)
    print("strand merge {}".format(min(times) / 10000))
    print(sorted(list(ls)) == strand_sort(list(ls)))
