VOWELS = ('a','e','i','o','u','A','E','I','O','U')

message = input ('Digite alguma palavra e eu removerei as vogais : ')

new_message = ''

for letter in message:
    if letter in VOWELS:
        print(letter, 'é uma vogal, removendo...')

    if letter not in VOWELS:
        new_message += letter


print(message,'sem vogais se fica:',new_message)
