# https://dodona.be/nl/courses/4157/series/46287/activities/1813154454

######################################
###      Timekeeping on Mars       ###
######################################

######################################
###           My Solution          ###
######################################

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


######################################
###         Sample Solution        ###
######################################

# # read number of sol
# sol = int(input())
# # express number of sol in seconds
# seconds = int(sol * (((24 * 60) + 39) * 60 + 35.244))
#
# # convert seconds into minutes and seconds
# minutes = seconds // 60
# seconds %= 60
# # convert minutes into hours and minutes
# hours = minutes // 60
# minutes %= 60
# # convert hours into days and hours
# days = hours // 24
# hours %= 24
# # output conversion of sol into days, hours, minutes and seconds
# print(f'{sol} sols = {days} days, {hours} hours, {minutes} minutes and {seconds} seconds')