print("Hello, stranger")
communist = input("Tell me, are you a communist? ")

if communist == "yes":
    print("That is great, you are my star pupil.")
elif communist == "no":
    print("Off with your head!! ")
else:
    print("Hmmm... give me a proper answer next time")

print("Moving on, next question")
name = input("What do you think our country should be called? The USSR, Russia, Soviet Union, or somehting else? ")

if name == "Soviet Union":
    print("Well done, just what I think as well.")
elif name == "USSR":
    print("Maybe. I'll think about it")
elif name == "Russia":
    print("Ha! Boring")
else:
    print("You think you're funny do you?")

print("Last question.")
state= int(input("How many communist countries or states have you been to? (numbers only) "))

if state <= 3:
    print("Far too less. Do some more travelling.")
elif state > 4 and state < 15:
    print("Goog, good")
elif state >16:
    print("Wow! Amazing!")
else:
    print("no")


print("These answers were supported and sponsered by Vladimir Lenin")
