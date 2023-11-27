def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE

    # for num in nums:
    #     return True if num == 7 else False
    # #         return True
    # # return False

    return True if nums.__contains__(7) else False




print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
