def multiply_even_numbers(nums):


    product = 1

    for num in nums:
        if num % 2 == 0:
            product = product * num

    return product
