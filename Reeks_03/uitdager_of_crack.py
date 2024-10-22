# https://dodona.be/nl/courses/4157/series/46289/activities/438287311

n = int(input('the number of questions in the round: '))

crack, challenger = 0, 0

for i in range(n):
    correct_answer = str(input('the correct answer to the question: A, B or C?'))
    given_answer = str(input('the given answer to the question: A, B or C?'))
    assessment = str(input('the assessment of the crack on the answer given by the challenger: correct or wrong? '))

    if correct_answer == given_answer:
        challenger += 1
    if (correct_answer == given_answer and assessment =='correct') or (correct_answer != given_answer and assessment == 'wrong'):
        crack+=1

if crack < n/2:
    print(f'challenger wins {challenger} points against {crack}')
else:
    if crack > challenger:
        print(f'crack wins {crack} points against {challenger}')
    elif crack == challenger:
        print(f'ex aequo: both contestants score {crack} points')
    else:
        print(f'challenger wins {challenger} points against {crack}')

