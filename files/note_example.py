# Create a Python program that allows users to write, read, and manage their notes
def create_note(note):
    file = open("notes.txt", "a")
    file.write(note + "\n")
    file.close()

def read_notes():
    file = open("notes.txt", "r")
    content = file.read()
    print("Your notes:\n")
    print(content)
    file.close()
    

while True:
    option = input("\n1.read\n2.write\n3.exit\nEnter your choice:")
    if option == "write":
        # read note
        note = input("Enter Your note: ")
        create_note(note)
    elif option == "read":
        # take note from user and save it
        read_notes()
    elif option == "exit":
        # exit
        print("Bye!!")
        break
    

