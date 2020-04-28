#Name: Michael Conger
#Date: February 10, 2020

def juice():
    print('Death Race for Love, The Game')

    name=input("Enter your rapper name")
    age=input("Enter your age")
    m=("Press Enter to continue...")
    c=("Score:")
    w=("Congratualtions,",name,"! Juice Wrld has just invited you to a booth session after",
          "you posted an instagram video of you performing one of his songs.")
    x=("You and Juice Wrld are perfect together. Your song is made and his record",
          "label approaches you with a deal. You sign the deal and make $100,000 every song at",age,"years of age.")
    y=("Your song is released and it shoots up the charts. The record label loves the",
          "chemistry you two have and they want you to make an album together.")
    z=("Everything is going great with the album but sadly Juice Wrld has passed",
          "away. The record label is stunned but still wants a complete album so they",
          "assign you,",name,", to finish the album to honor his legacy.")
    b=("The album is finished and reaches the number one spot on the Billboard top 100",
          "charts. Congratualtions you have won the Death Race for Love! You are only",age,"and you already have a number one hit!")
    e=("Citations: I worked with Sarah Bradford and Jadyn Kennedy and I also used the iLearn template.")
   
 

    print() # Prints a blank line
    print(w)
    print(c, 100)
    input(m)
    print()

    print(x)
    print(c, 200)
    input(m)
    print()

    print(y)
    print(c, 300)
    input(m)
    print()

    print(z)
    print(c, 400)
    input(m)
    print()

    print(b)

    print() # Prints a blank line
    print(e)
def main(wrld):
    wrld()
    
main(juice)

