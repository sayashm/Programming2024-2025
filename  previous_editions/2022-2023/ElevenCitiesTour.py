# https://dodona.be/en/courses/1659/series/18381/activities/1449404008/

cities=[]
str_cities = ''
while True:
    i = str(input(f'add number #{len(cities)+1} or "finish": '))
    if i == 'finish':
        break
    try:
        cities.append(str(i))
        str_cities += i
    except:
        print("Please enter a valid number or 'stop'.")

t = tuple(c.replace("🔘", "") for c in cities if "🔘" in c)
pt = f"({', '.join(t)})" if t else ""


# find in text
print(f'# stamps: {len(cities)}')
print(f'# holes: {str_cities.count("🔘")} {pt}'.rstrip())
print(f'cross earned: {"yes" if len(cities) == 11 and str_cities.count("🔘") == 3 else "no" }')

