mood = int(input("How is your mood today?\n"))

def test_mood():
    if mood == "Happy":
        print("So nice to hear that.")
    elif mood == "Sad":
        print("What can I do to lighten up your mood?")
    else:
        print("I do not understand the words coming out of your mouth.")

test_mood()