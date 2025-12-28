# example of using a for loop to iterate through a list and print each item to the console
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

for char in 'code':
    print(char)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

# Another type of loop you can use in Python is the while loop.
#  This type of loop will repeat a block of code until the condition is False
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

# The break statement is used to stop the execution of a loop. 
# Here is an example of using the break statement for a list of developer_names
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

# The continue statement is used to skip the current iteration of a loop and move onto the next iteration.
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

# Both for and while loops can be combined with an else clause, 
# which is executed only when the loop is not terminated by a break statement
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")