#https://dodona.be/en/activities/1228419728/

mass = int(input('mass: '))
height = int(input('input: '))

BMI = mass / ((height/ 100) ** 2)

if BMI < 18:
    diagnosis = 'underweight'
elif BMI < 25:
    diagnosis = 'normal weight'
elif BMI < 27:
    diagnosis = 'overweight'
elif BMI < 30:
    diagnosis = 'moderate overweight'
elif BMI < 40:
    diagnosis = 'severe overweight'
else:
    diagnosis = 'very severe overweight'

print(f'A person weighing {mass} kg and measuring {height} cm has {diagnosis}.')