# https://dodona.be/nl/courses/4157/series/46287/activities/368174997


creature = input('please input the name of the species: ')

heartBeat = int(input('please input the average number of heartbeats per minute of the species: '))
lifeTime = int(input('please input the average life expectancy of the species expressed in years: '))

allHeartBeat = heartBeat * 60 * 24 * 365 * lifeTime

result = allHeartBeat / (10**9)

print(f'{creature} have {result:.2f} billion heartbeats')





