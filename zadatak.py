dictionary = {'treba': ['trebati'], 'radi': ['raditi', 'rad']}


def chooseOptions():
    while True:
        options = """
        1. Create
        2. Read
        3. Delete
        4. Update
        5. Quit 
        """
        print(options)
        option = int(input("\nChoose option: "))
        
        if option == 1:
            create()
        elif option == 2:
            read()
        elif option == 3:
            delete()
        elif option == 4:
            update()
        elif option == 5:
            print("Quit")
            break
        else:
            print(f"\nChoose number from 1 to 5!\n")


def create():
    word = input("\nWord: ")
    meaning = input(f"Meaning for word {word}: ")
    
    if word in dictionary:
        if meaning not in dictionary[word]:
            # if word is already in dictionary just add another meaning for the same word
            dictionary[word].append(meaning)
        else:
            # if meaning is already in dictionary print message
            print(f"\nMeaning {meaning} already added\n")
    else:
        # if word is not in dictionary add new word and new meaning for that word
        dictionary[word] = [meaning]


def read():
    print("\n----------------------")
    for word, meaning in dictionary.items():
        print(f"{word} - {meaning}")
    print("----------------------\n")


def delete():
    opt = """
    1. Delete one word
    2. Delete all
    """
    print(opt)
    del_option = int(input("\nChoose what to delete: "))

    if del_option == 1:
        read()
        del_word = input("\nWord to delete: ")
        del dictionary[del_word]
    elif del_option == 2:
        for word in dictionary.copy(): # if we want to iterate through dictionary and delete elements we must add .copy
            del dictionary[word]


def update():
    edit_word = input("\nWhat word do you want to edit: ")
    
    if edit_word in dictionary.keys():
        new_meaning = input(f"New meaning for the word {edit_word}: ")
        dictionary[edit_word].append(new_meaning)
        print("--Dictionary updated successfuly--")
    else:
        print("    \nWord doesn't exist")
        update()


chooseOptions()



