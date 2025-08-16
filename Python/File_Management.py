while True:
    File_Name = input('Enter file name: ')
    try:
        with open(File_Name, 'r') as file:
            content = file.read()
        print(content)

        user = input('Do you wish to edit this file? ').lower()


        while True:
            if user == 'y':
                add = input('What would you like to add: ')
                modified_name = 'Modified_' + File_Name
                with open(modified_name, 'w') as file:
                    file.write(content + '\n' + add)
                print(f'A modified file with name {modified_name} has been added.')
                break
            elif user == 'n':
                print('Exiting...')
                break

            else:
                print('Please enter a valid input.')
                break
        break


    except FileNotFoundError:
        print('File does not exist')
        Create = input('Do you wish to create this file? ').lower()
        if Create == 'y':
            with open (File_Name, 'w') as file:
                file.write('')
            print(f'A file with the name {File_Name} has been created.')
        else:
            print('Exiting...')
            break
