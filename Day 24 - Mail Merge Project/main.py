#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/names/invited_names.txt", "r") as name:
    names_list = name.readlines()

with open("input/letters/starting_letter.txt") as letter:
    letter_str = letter.read()


for n in names_list:
    new_name = n.strip()
    new_letter = letter_str.replace("[name]", new_name)
    with open(f"output/readyToSend/letter_for_{new_name}.txt", "w") as data:
        data.write(new_letter)
