def find_the_duplicate(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)
