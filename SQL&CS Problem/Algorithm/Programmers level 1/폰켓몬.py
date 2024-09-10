def solution(nums):
    length = len(nums) // 2
    counts = [0 for i in range(0, 200001)]

    for i in nums:
        counts[i] += 1
    differentCount = len(counts) - counts.count(0)

    if differentCount > length:
        return length
    else:
        return differentCount
