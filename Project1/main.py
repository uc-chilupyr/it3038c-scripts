class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'





if(1==1):
    userString = input('Enter the string/phrase to count the characters: ')
    userChar = input('Enter the character you want counted: ')
    while True:
        if(len(userChar)>1):
            print('Please enter only 1 character!!')
            print('Please enter again: ')
            userChar = input()
        else:
            break
    print("The number of times '" +(color.BOLD+userChar+color.END) + "' occurs in '" +userString + "' is ")
    print((userString.count(userChar)))

