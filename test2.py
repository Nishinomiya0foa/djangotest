def quick_sort(alist, start, end):
    if start >= end:
        return
    low = start
    high = end
    mid = alist[low]

    while low < high:
        while low < high and mid < alist[high]:
            # 从右边开始找，如果元素小于基准，则把这个元素放到左边
            high -= 1
        alist[low] = alist[high]

        while low < high and mid > alist[low]:
            # 从左边开始找，如果元素大于基准，则把元素放到右边
            low += 1
        alist[high] = alist[low]

    # 循环退出，low==high，把基准元素放到这个位置
    alist[low] = mid

    # 递归调用，重新排列左边的和右边的序列
    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)

l = [3,2,56,3,41,5,6,1]
quick_sort(l, 8, 8)
print(l)


def bubble_sort(alist):
    length = len(alist)
    for i in range(length - 1):
        # i表示比较多少轮
        for j in range(length - i - 1):
            # j表示每轮比较的元素的范围，因为每比较一轮就会排序好一个元素的位置，
            # 所以在下一轮比较的时候就少比较了一个元素，所以要减去i
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

