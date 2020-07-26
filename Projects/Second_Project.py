#Second Project
#Removing Vowels from sentences

remove = ("a","e","i","o","u")

message = input("Enter the message :")
new_message = ""

for letters in message:
    if letters not in remove:
        new_message = new_message + letters

print(new_message)
