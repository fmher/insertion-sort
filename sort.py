# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


iterations = 0
def insertion_sort(li):
    global iterations
    # iterate the list once in an outer loop
    # for current_index, current_value in enumerate(li):
    #     # inner loop that iterates backwards and plaes items where they need to be
    #     inner_loop_index = current_index - 1
    #     while inner_loop_index >= 0 and current_value < li[inner_loop_index]:
    #         li[inner_loop_index], li[inner_loop_index + 1] = li[inner_loop_index + 1], li[inner_loop_index]
    #         inner_loop_index -= 1
    for i in range(len(li)):
        # keep track of the current number for comparisons
        current_value = li[i]
        for j in range(i - 1, -1, -1):
            iterations += 1
            if current_value < li[j]:
                li[j], li[j + 1] = li[j + 1], li[j]
            else:
                break
            


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

# insertion_sort(li)
bubble_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
print(iterations)
print(len(li))
