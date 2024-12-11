# https://dodona.be/en/courses/4157/series/46294/activities/638581913/

# Take input
key = input('Enter the Key')
ciphertext = input('Enter the Ciphertext')

# Make a dictionary to locate each letters number
dictionary = {}
for idx , number in enumerate(key):
    if number.isdigit(): # the condition to avoid element if it is not digit
        if number in  dictionary: # Add it to the list of value of dictionary if it is availabe
            dictionary[number].append(ciphertext[idx])
        else: # Create the Key and Value for the element then Add it to the list of value of dictionary if it is not availabe
            dictionary[number] = [ciphertext[idx]]


# Make a final string by using dictionary of location and letters
print(''.join(letter for pos in range(10) if str(pos) in dictionary for letter in dictionary[str(pos)]  ))

















