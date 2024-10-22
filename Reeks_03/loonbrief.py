# https://dodona.be/nl/courses/4157/series/46289/activities/990750894

s = 0
n = 1

large_number = int(input('the large random number chosen by the first worker: '))
l = large_number

while s != 'stop':
    s = str(input(f'salary of worker #{n}: '))
    if s == 'stop':
        break
    else:
        large_number = large_number + int(s)
        print(f'worker #{n} whispers €{large_number}')
        n += 1


avg = ( large_number - l ) / (n-1)
print(f'average salary: €{avg :.2f}')


