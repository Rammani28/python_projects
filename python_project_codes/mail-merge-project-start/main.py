# TODO: Create a letter using starting_letter.txt
with open('Input/Names/invited_names.txt') as file:
    name_list = file.readlines()

new_list = []
for name in name_list:
    new_list.append(name.strip('\n'))


with open('Input/Letters/starting_letter.txt') as starting_letter:
    for name in new_list:
        content = starting_letter.read()
        new_content = content.replace('[name]', name)
        with open(f'Output/ReadyToSend/letter_to_{name}.txt', 'w') as new_letter:
            new_letter.write(new_content)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
