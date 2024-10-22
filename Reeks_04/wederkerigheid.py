# https://dodona.be/nl/courses/4157/series/46290/activities/1936429631

nums =[str(input(f'number #{i+1}: ')) for i in range(3)]

for i in range(3):
    test = nums[:i] + nums[i + 1:]
    test = test[0]+test[1]
    result = ''
    for j in range(10):
        Count = test.count(str(j))

        if int(nums[i][j]) != Count:
            result += 'X'
        else:
            result += nums[i][j]

    print(result)
