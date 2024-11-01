# https://dodona.be/nl/courses/4157/series/46287/activities/368174997

######################################
###           Heartbeats           ###
######################################

######################################
###           My Solution          ###
######################################
creature = input('please input the name of the species: ')

heartBeat = int(input('please input the average number of heartbeats per minute of the species: '))
lifeTime = int(input('please input the average life expectancy of the species expressed in years: '))

allHeartBeat = heartBeat * 60 * 24 * 365 * lifeTime

result = allHeartBeat / (10**9)

print(f'{creature} have {result:.2f} billion heartbeats')


######################################
###         Sample Solution        ###
######################################

# # read creature features
# creatures = input() # name of a creature (plural)
# heart_rate = int(input()) # heart rate (per minute)
# longevity = int(input()) # longevity (in years)
# # determine number of heartbeats in a lifetime
# minutes_per_year = 60 * 24 * 365
# heartbeats = heart_rate * minutes_per_year * longevity
# # output number of heartbeats in a lifetime
# print(f'{creatures} have {heartbeats / 1e9:.2f} billion heartbeats')





