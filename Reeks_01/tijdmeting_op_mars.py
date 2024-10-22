# https://dodona.be/nl/courses/4157/series/46287/activities/1813154454

sol = int(input('please input how many sol do you want to calculate? '))

eachSolInSecond = (24*60*60)+(39*60)+35.244
solInSecond = eachSolInSecond * sol

minutes = int(solInSecond // 60)
second = int(solInSecond % 60)

hours = int(minutes // 60)
minute = minutes % 60

days = int(hours // 24)
hour = hours % 24


print(f'{sol} sols = {days} days, {hour} hours, {minute} minutes and {second} seconds')
