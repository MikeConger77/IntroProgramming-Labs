
4/28/20

colors = ["red", "blue", "green", "pink", "purple"]

def showTitle():
    print("Color Preferance Evaluator")

def promptForColor():
    color = input("Enter a Color: ")
    color = color.strip()
    color = color.lower()
    return color

def praiseUser():
    print("Fantastic Choice!")

def ridiculeUser():
    print("Who likes that color?")

def confirmColor():
    x=0
    color = promptForColor()
    while x==0:
        usure = "You enterered {} Is this correct? (Y/N)\n".format(color)
        confirm = input(usure)
        confirm = confirm.lower()
        if confirm[0] == "y":
            x=1
        elif confirm[0] =="n":
            x=0
        else:
            x=0
        return color

def containsElement():
    x = 2
    color = confirmColor()
    while x==2:
        if color == colors[0] or color == colors[1] or color == colors[2] or color == colors[3] or color == colors[4]:
            x=1
            praiseUser()
        else:
            x=1
            ridiculeUser()

def main():
    showTitle()
    containsElement()

main()
    
