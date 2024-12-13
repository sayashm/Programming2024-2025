# https://dodona.be/nl/courses/4157/series/46292/activities/1031734873
from string import punctuation



sentence = input('sentence: ')
occurrences = input('occurrences: ')


special_char = punctuation+' '+'…'+'–'+"’"
line1 = ''
line2 = ''

for index , letter in enumerate(sentence):

    if letter not in special_char:

        if occurrences == 'past':
            letter_count = sentence.lower()[:index].count(letter.lower())

        elif occurrences== 'present':
            letter_count = sentence.lower().count(letter.lower())

        else:
            letter_count = sentence.lower()[index + 1:].count(letter.lower())


        if letter_count > 9:
            line1 += letter+'-'
            line2 += str(letter_count)

        else:
            line1 += letter
            line2 += str(letter_count)

    else:
        line1 += letter
        line2 += letter


print(line1)
print(line2)
