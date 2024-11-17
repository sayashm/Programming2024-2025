# https://dodona.be/nl/courses/4157/series/46295/activities/668293311


def emergency_plan(n: int, m:int):
    '''
    >>> emergency_plan(17, 5)
    [1, 6, 11, 16, 5, 12, 2, 9, 17, 10, 4, 15, 14, 3, 8, 13, 7]
    >>> emergency_plan(16, 11)
    [1, 12, 8, 5, 3, 2, 4, 7, 11, 16, 14, 15, 10, 6, 9, 13]
    '''
    nums = [i + 1 for i in range(n)]
    res = []
    index = 0
    while nums:

        res.append(nums.pop(index))
        if not nums:
            break
        index = (index + m - 1) % len(nums)
    return res



def valid_jump(length: int):
    '''
    >>> valid_jump(17)
    7
    >>> valid_jump(14)
    '''

    return next((jump for jump in range(1, length+1) if emergency_plan(length, jump)[-1] == 13), None)

