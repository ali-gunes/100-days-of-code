# On day 24, we are: Studying Fİles, Directories and Paths

# Project 24 - Mail Merge Project

# To write something somewhere so it can stay persistent, we can use file processes such as open, read and write
# We are going to open, read and write "sample_file.txt"

# file = open("sample_file.txt")  # Opened and saved it to variable
# contents = file.read()
# print(contents)
# file.close()  # We need to close the file when we are done, this saves resources and increase the performance

# With this line of code, we don't have to close the file, it will automatically close when the process is done
# This is a read only mode, if you want to write it you need to use some keywords for mode
# with open("sample_file.txt") as file:
#     contents = file.read()
#     print(contents)

# This will write to file but does not append, deletes everything and writes again,
# If file does not exist, write mode will create it for us
# with open("sample_file.txt", mode="w") as file:
#     file.write("I am a cat")

# This will append to file
# with open("sample_file.txt", mode="a") as file:
#     file.write("\nI am a cat")

with open("./Input/Names/invited_people.txt") as file:
    contents = file.read()
    people_list = contents.split("\n")

with open("./Input/Letter/mail_template.txt") as file:
    contents = file.read()
    for people in people_list:
        new_mail = contents.replace("[name]", people)
        with open(f"./Output/ReadyToSend/{people}.txt", mode="w") as file:
            file.write(new_mail)


print("It's Done!")