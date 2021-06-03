import timeit
from random import shuffle, randrange
from statistics import mean
from functools import partial
from collections import deque

def strand_sort_original_1(array):
    if len(array) < 2:
        return array
    result = []
    while array:
        i = 0
        sublist = [array.pop()]
        while i < len(array):
            num = array[i]
            if num > sublist[-1]:
                sublist.append(num)
                del array[i]
            else:
                i = i + 1
        result = merge_original_2(result, sublist)
    return result

def merge_original_1(left, right):
    i = 0
    j = 0
    merged_list = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged_list.append(right[j])
            j += 1
        else:
            merged_list.append(left[i])
            i += 1
    merged_list += left[i:]
    merged_list += right[j:]
    return merged_list

def strand_sort_original_2(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        i = 0
        sublist = [unsorted.pop()]
        while i < len(unsorted):
            item = unsorted[i]
            if item > sublist[-1]:
                sublist.append(item)
                del unsorted[i]
            else:
                i = i + 1
        result = merge_original_2(result, sublist)
    return result

def merge_original_2(left, right):
    if not left: return right
    if not right: return left

    if left[-1] > right[-1]:
        left, right = right, left

    it = iter(right)
    y = next(it)
    result = []

    for x in left:
        while y < x:
            result.append(y)
            y = next(it)
        result.append(x)
    result.append(y)
    result.extend(it)
    return result

def strand_sort_original_3(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        sublist = [unsorted.pop()]
        leftovers = []
        last = sublist[-1]
        for item in unsorted:
            if item >= last:
                sublist.append(item)
                last = item
            else:
                leftovers.append(item)
        result = merge_original_2(result, sublist)
        unsorted = leftovers
    return result

def strand_sort_original_4(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        sublist = [unsorted.pop(0)]
        leftovers = []
        last = sublist[0]
        sublist_append = sublist.append
        leftovers_append = leftovers.append
        for item in unsorted:
            if item >= last:
                sublist_append(item)
                last = item
            else:
                leftovers_append(item)
        result = merge_original_2(result, sublist)
        unsorted = leftovers
    return result

def strand_sort_gengisteve_1(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        sublist = [unsorted.pop()]
        sub_append = sublist.append
        leftovers = []
        left_append = leftovers.append
        for item in unsorted:
            if item > sublist[-1]:
                sub_append(item)
            else:
                left_append(item)
        result = merge_gengisteve(result, sublist)
        unsorted = leftovers
    return result

def strand_sort_gengisteve_2(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        sublist = [unsorted.pop()]
        last = sublist[0]
        sub_append = sublist.append
        leftovers = deque()
        left_append = leftovers.append
        for item in unsorted:
            if item >= last:
                sub_append(item)
                last = item
            else:
                left_append(item)
        result = merge_original_2(result, sublist)
        unsorted = leftovers
    return result

def strand_sort_gengisteve_3(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        if type(unsorted) is list:
            sublist = [unsorted.pop(0)]
        else:
            sublist = [unsorted.popleft()]
        last = sublist[0]
        sub_append = sublist.append
        leftovers = deque()
        left_append = leftovers.append
        for item in unsorted:
            if item >= last:
                sub_append(item)
                last = item
            else:
                left_append(item)
        result = merge_original_2(result, sublist)
        unsorted = leftovers
    return result


def merge_gengisteve(left, right):
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

def strand_sort_deque(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []

    while unsorted:
        sublist = [unsorted.popleft()]
        last = sublist[0]
        sub_append = sublist.append
        leftovers = deque()
        left_append = leftovers.append
        for item in unsorted:
            if item >= last:
                sub_append(item)
                last = item
            else:
                left_append(item)
        result = merge_gengisteve(result, sublist)
        unsorted = leftovers
    return result

def original():
    temp_shuffled = list(range(10))
    temp_sorted = sorted(temp_shuffled)
    temp_reversed = [x for x in reversed(temp_shuffled)]
    shuffle(temp_shuffled)
    ls_dict = {
            0: temp_sorted,
            1: temp_reversed,
            2: temp_shuffled
            }
    ls_words = {
            0: "Already sorted",
            1: "Reverse sorted",
            2: "Random order"
            }

    reps = 2
    num = 2

    for x in range(3):
        ls  = ls_dict[x]
        ld = deque(ls)
        #print("\n    {}:\t{}".format(ls_words[x], ls))
        print("\n    {}:".format(ls_words[x]))

        print("    Name \t\tMean\t\t\tMin\t\t\tMax")

        times = timeit.Timer(partial(strand_sort_original_1, list(ls))).repeat(reps, num)
        print("    original_1 \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_original_2, list(ls))).repeat(reps, num)
        print("    original_2 \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_gengisteve_1, list(ls))).repeat(reps, num)
        print("    gengisteve \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_gengisteve_2, list(ls))).repeat(reps, num)
        print("    gengisteve_2 \t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_deque, deque(ld))).repeat(reps, num)
        print("    deque \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

temp = [
        [randrange(0, 1000) for _ in range(10)],
        [randrange(0, 1000) for _ in range(100)],
        [randrange(0, 1000) for _ in range(1000)],
        [randrange(0, 1000) for _ in range(10000)],
        [randrange(0, 1000) for _ in range(100000)],
        ]

t = temp[4][:]
temp2 = [
        sorted(t)[:],
        [x for x in sorted(t)[::-1]][:],
        t[:],
        ]

def main():
    reps = 2
    num = 2

    tests = [
            'strand_sort_original_4',
            'strand_sort_deque',
            'strand_sort_gengisteve_2',
            'strand_sort_gengisteve_3',
            ]

    ls_words = {
            0: "already sorted",
            1: "reverse sorted",
            2: "random order"
            }

    for l in range(len(temp2)):

        print("\n    On a list of {} {} items:\tMean\t\t\tMin\t\t\tMax".format(len(temp2[l]), ls_words[l]))

        for name in tests:

            if name == 'strand_sort_deque':
                test = '{}(deque(temp2[{}][:]))'.format(name, l)
            else:
                test = '{}(temp2[{}][:])'.format(name, l)
            setup = 'from __main__ import {}, temp2; from collections import deque'.format(name)

            t = timeit.Timer(test, setup)

            runs = t.repeat(reps, num)
            print('    {}: {}{}\t{}\t{}'.format(
                    name,
                    '\t\t' if name == 'strand_sort_deque' else '\t',
                    mean(runs),
                    min(runs),
                    max(runs),
                    ))

t1 = temp[4][:]
t2 = temp[4][:]
temp1 = [
        sorted(t1)[:],
        [x for x in sorted(t1)[::-1]][:],
        t1[:],
        ]
temp2 = [
        sorted(t2)[:],
        [x for x in sorted(t2)[::-1]][:],
        t2[:],
        ]
def main2():
    reps = 2
    num = 2

    tests = [
            'merge_original_1',
            'merge_original_2',
            'merge_gengisteve',
            ]

    ls_words = {
            0: "already sorted",
            1: "reverse sorted",
            2: "random order"
            }

    for l in range(len(temp2)):

        print("\n    On a list of {} {} items:\tMean\t\t\tMin\t\t\tMax".format(len(temp2[l]), ls_words[l]))

        for name in tests:

            test = '{}(temp1[{}][:], temp2[{}][:])'.format(name, l, l)
            setup = 'from __main__ import {}, temp1, temp2; from collections import deque'.format(name)

            t = timeit.Timer(test, setup)

            runs = t.repeat(reps, num)
            print('    {}: {}{}\t{}\t{}'.format(
                    name,
                    '\t\t' if name == 'strand_sort_deque' else '\t',
                    mean(runs),
                    min(runs),
                    max(runs),
                    ))

if __name__ == '__main__':
    main2()
