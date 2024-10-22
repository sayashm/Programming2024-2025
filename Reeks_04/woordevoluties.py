# https://dodona.be/nl/courses/4157/series/46290/activities/1713291174

word = input('Word: ')
letter = input('Letter: ')


start_letter = word[0]
end_letter = letter

distance = (ord(end_letter) - ord(start_letter)) % 26

for char in word:
    start_pos = ord(char) - ord('A')
    end_pos = (start_pos + distance) % 26
    corresponding_letter = chr(end_pos + ord('A'))

    print(char, end="")

    i = start_pos + 1
    while i != end_pos:
        print(chr((i % 26) + ord('a')), end="")
        i = (i + 1) % 26

    print(corresponding_letter)






