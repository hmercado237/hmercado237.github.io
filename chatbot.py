class Personality():
    hiResponse = "HELLO"
    whatsupResponse = ""
    howAreYouResponse = ""

    def processInput(self, response):
        if response == "Hi":
            print(self.hiResponse)
        elif response == "Whats up?":
            print(self.whatsupResponse)
        elif response == "How are you?":
            print(self.howAreYouResponse)
        else:
            print(self.otherResponse)

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
    userChoice = choosePersonality()
    print(userChoice)

    niceRobot = Personality()
    niceRobot.hiResponse = "HI, IT'S SO NICE TO MEET YOU!"
    niceRobot.whatsupResponse = "OH I'M JUST TALKING TO THE MOST INTERESTING PERSON IN THE WORLD."
    niceRobot.howAreYouResponse = "OH I'M JUST LOVELY!"
    niceRobot.otherResponse = "TERRIBLY SORRY, BUT I DON'T UNDERSTAND."

    meanRobot = Personality()
    meanRobot.hiResponse = "CAN YOU LEAVE???"
    meanRobot.whatsupResponse = "DON'T SPEAK TO ME FOOL!"
    meanRobot.howAreYouResponse = "TERRIBLE, NOW THAT I AM TALKING TO YOU."
    meanRobot.otherResponse = "I DON'T UNDERTSAND YOUR GIBBERISH, SWINE!"

    nervousRobot = Personality()
    nervousRobot.hiResponse = ""
    nervousRobot.whatsupResponse = "...UM, HI."
    nervousRobot.howAreYouResponse = "NERVOUS!"
    nervousRobot.otherResponse = "THW WORLD IS LARGE AND CONFUSING AND I AM SMALL AND SCARED"

    intro()
    while True:
        answer = input("(What will you say?)")

        if (userChoice == "Nice"):
            niceRobot.processInput(answer)
        elif (userChoice == "Mean"):
            meanRobot.processInput(answer)
        elif (userChoice == "Nervous"):
            nervousRobot.processInput(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
