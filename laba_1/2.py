def selection_sort(nums):  
    for i in range(len(nums)):
        l = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[l]:
                l = j
        nums[i], nums[l] = nums[l], nums[i]