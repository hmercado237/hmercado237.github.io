

# --- Define your functions below! ---
def intro():
    print("HELLO, I AM CHATBORT")
    print("LET'S TALK!")
    print("[INSTRUCTIONS FOR USE]")
# RPS
# Different bort personalities

def choosePersonality():
    print("Choose a personality to talk to. You can choose:")
    choice = input("Mean, Nice, or Nervous")
    return choice

# --- Put your main program below! ---
def main():

    mean = ("Hi" : "CAN YOU LEAVE", "What's up" : " DON'T SPEAK TO ME FOOL!",
    "How are you?" : "TERRIBLE, NOW THAT I AM TALKING TO YOU." )

    nice = ("Hi :""HI, IT'S SO NICE TO MEET YOU!", "What's up" :
     "OH I'M JUST TALKING TO THE MOST INTERESTING PERSON IN THE WORLD.", "How are you?" :
     "OH I'M JUST LOVELY!")

     nervous = ( "Hi" : "", "What's up" : "...UM, HI.", "How are you?" : "NERVOUS!")


    userChoice = choosePersonality()

    intro()
    while True:
        answer = input("(What will you say?)")

        if userchoice = "Nice":
            print(userChoice[answer])
        elif userchoice = "Mean":
            print(userChoicer[answer])
        elif userChoice = "Nervous":
            print(userChoice[answer])

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
