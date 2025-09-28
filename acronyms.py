# look_up = input("Enter acronym to look up: ").upper()

# with open("input.txt") as file:
#     for line in file:
#         if line.startswith(look_up):
#             print(line.strip())
#             break
#     else:
#         print("Acronym not found.")

# ADDING NEW ACRONYMS:
# new_acronym = input("Enter new acronym: ").upper()
# new_definition = input("Enter definition: ")

# with open("input.txt", "a") as file:
#      file.write(new_acronym + " - " + new_definition + "\n")

def find_acronym():
    find = input("Which acronym are you after?\n")

    with open('input.txt') as file:
        for line in file:
            if find in line:
                print(line)
                found = True
                break
            else: 
                print('Acronym not found')

def remove_acronym():
    remove = input('Which acronym do you want to remove?\n')
    with open('input.txt') as file:
        lines = file.readlines()
    with open('input.txt', 'w') as file:
        for line in lines:
            if remove not in line:
                file.write(line)

def add_acronym():
     acronym = input('What acronym do you want to add?\n')
     definition = input('What is the definition?')
     with open(input.txt) as file:
          file.write(acronym + '-' + definition + '\n')

def main():
    option = input("Do you want to find(F), add(A) or remove(R) an acronym?")
    if option == 'F':
        find_acronym()
    elif option == 'R':
        remove_acronym()
    elif option == 'A':
        add_acronym()
    else:
        print('You numpty!')

main()
