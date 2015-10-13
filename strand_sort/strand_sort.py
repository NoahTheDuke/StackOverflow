import timeit
from random import shuffle
from statistics import mean
from functools import partial
from collections import deque

def strand_sort_original(unsorted):
    if len(unsorted) < 2:
        return unsorted
    result = []
    while unsorted:
        #i = 0
        sublist = [unsorted.pop()]
        leftovers = []
        for item in unsorted:
        #while i < len(unsorted):
            #item = unsorted[i]
            if item > sublist[-1]:
                sublist.append(item)
                #del unsorted[i]
            else:
                leftovers.append(item)
                #i = i + 1
        result = merge_original(result, sublist)
        unsorted = leftovers
    return result

def merge_original(list_1, list_2):
    i = 0
    j = 0
    merged_list = []
    len_left, len_right = len(list_1), len(list_2)
    while i < len_left and j < len_right:
    #while i < len(list_1) and j < len(list_2):
        if list_1[i] > list_2[j]:
            merged_list.append(list_2[j])
            j += 1
        else:
            merged_list.append(list_1[i])
            i += 1
    merged_list += list_1[i:]
    merged_list += list_2[j:]
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
        result = merge_original(result, sublist)
    return result

def merge_original_2(l1, l2):
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

def strand_sort_gengisteve(unsorted):
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
        result = merge_gengisteve(result, sublist)
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
        result = merge_deque(result, sublist)
        unsorted = leftovers
    return result

def merge_deque(left, right):
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

#temp = list(range(10))
#shuffle(temp)
#print(strand_sort_original(temp))

def main():
    temp_shuffled = list(range(10))
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

    reps = 2
    num = 2

    for x in range(3):
        ls  = ls_dict[x]
        ld = deque(ls)
        #print("\n    {}:\t{}".format(ls_words[x], ls))
        print("\n    {}:".format(ls_words[x]))

        print("    Name \t\tMean\t\t\tMin\t\t\tMax")

        times = timeit.Timer(partial(strand_sort_original, list(ls))).repeat(reps, num)
        print("    original \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_original_2, list(ls))).repeat(reps, num)
        print("    original_2 \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_gengisteve, list(ls))).repeat(reps, num)
        print("    gengisteve \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_gengisteve_2, list(ls))).repeat(reps, num)
        print("    gengisteve_2 \t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))

        times = timeit.Timer(partial(strand_sort_deque, deque(ld))).repeat(reps, num)
        print("    deque \t\t{}\t{}\t{}".format(mean(times) / num, min(times) / num, max(times) / num))
