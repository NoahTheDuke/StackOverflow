import timeit
from random import shuffle, randrange
from statistics import mean
from functools import partial
from collections import deque

def strand_sort_original_5(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        sublist = [unsorted.popleft()]
        leftovers = deque()
        sublist_append = sublist.append
        leftovers_append = leftovers.append
        for item in unsorted:
            if item > sublist[-1]:
                sublist_append(item)
            else:
                leftovers_append(item)
        result = merge(result, sublist)
        unsorted = leftovers
    return result

def strand_sort_original_4(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        sublist = [unsorted.pop(0)]
        leftovers = []
        last = sublist[-1]
        sublist_append = sublist.append
        leftovers_append = leftovers.append
        for item in unsorted:
            if item >= last:
                sublist_append(item)
                last = item
            else:
                leftovers_append(item)
        result = merge(result, sublist)
        unsorted = leftovers
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
        result = merge(result, sublist)
        unsorted = leftovers
    return result

def strand_sort_original_2(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        sublist = [unsorted.pop()]
        leftovers = []
        for item in unsorted:
            if item > sublist[-1]:
                sublist.append(item)
            else:
                leftovers.append(item)
        result = merge(result, sublist)
        unsorted = leftovers
    return result

def strand_sort_original_1(unsorted):
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
        result = merge(result, sublist)
    return result

def merge(left, right):
    i = 0
    j = 0
    merged_list = []
    len_left = len(left)
    len_right = len(right)
    while i < len_left and j < len_right:
        if left[i] > right[j]:
            merged_list.append(right[j])
            j += 1
        else:
            merged_list.append(left[i])
            i += 1
    merged_list += left[i:]
    merged_list += right[j:]
    return merged_list

def original():
    temp_shuffled = list(range(100))
    temp_sorted = sorted(temp_shuffled)
    temp_reversed = [x for x in reversed(temp_shuffled)]
    shuffle(temp_shuffled)
    ls_dict = {
            0: temp_sorted,
            1: temp_reversed,
            2: temp_shuffled
            }
    print(ls_dict)
    ls_words = {
            0: "Already sorted",
            1: "Reverse sorted",
            2: "Random order"
            }
    reps = 10
    num = 1000

    for x in range(3):
        ls  = ls_dict[x]
        ld = deque(ls)
        #print("\n    {}:\t{}".format(ls_words[x], ls))
        print("\n    {}:".format(ls_words[x]))

        print("    Name:\t\tMean:\t\t\tMin:\t\t\tMax:")

        times = timeit.Timer(partial(strand_sort_original_5, deque(ld))).repeat(reps, num)
        print("    5 \t\t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_original_4, list(ls))).repeat(reps, num)
        print("    4 \t\t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_original_3, list(ls))).repeat(reps, num)
        print("    3 \t\t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_original_2, list(ls))).repeat(reps, num)
        print("    2 \t\t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_original_1, list(ls))).repeat(reps, num)
        print("    1 \t\t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

temp = [
        [randrange(0, 1000) for _ in range(10)],
        [randrange(0, 1000) for _ in range(100)],
        [randrange(0, 1000) for _ in range(1000)],
        [randrange(0, 1000) for _ in range(10000)],
        #[randrange(0, 1000) for _ in range(100000)],
        ]

def main():
    reps = 2
    num = 2

    tests = [
            #'strand_sort_original_5',
            'strand_sort_original_4',
            'strand_sort_original_3',
            'strand_sort_original_2',
            'strand_sort_original_1',
            ]
    for l in range(len(temp)):

        print("\n    On a list of {} items:\tMean\t\t\tMin\t\t\tMax".format(len(temp[l])))

        for name in tests:

            test = '{}(temp[{}][:])'.format(name, l)
            setup = 'from __main__ import {}, temp'.format(name)

            t = timeit.Timer(test, setup)

            runs = t.repeat(reps, num)
            print('    {}: {}{}\t{}\t{}'.format(
                    name,
                    "\t" if len(name) > 20 else "\t\t",
                    mean(runs) / num,
                    min(runs) / num,
                    max(runs) / num,
                    ))

if __name__ == '__main__':
    main()
