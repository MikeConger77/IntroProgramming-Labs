
4/28/20


def names():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    return firstname,lastname

def text():
    firstname, lastname = names()
    thename = str(firstname+"."+lastname)
    return thename

def secure():
    y = 0
    key =input("Create a password: ")
    notvalidsec = False
    if len(key)<8:
        notvalidsec = True
    while notvalidsec:
        print("The password must be at least 8 characters")
        key = input("Create a better password: ")
        if len(key)<8:
            notvalidsec = True
        else:
            notvalidsec = False
        while y==0:
            if (key.islower()) == False and (key.isupper()) == False:
                print("strong password")
                y=1
            if (key.isupper()) == True or (key.islower()) == True:
                y=0
                print("Password must contain both upper and lowercase letters")
                key=str(input("Please enter a new, stronger password"))

    return key

def main():
    thename=text()
    key = secure()
    print ("Great! Your new email is", thename.lower(),"1@marist.edu")

main()
        
    
    
    
