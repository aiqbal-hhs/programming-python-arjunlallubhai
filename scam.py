#Ask for personal details
first_name = input("What is your first name?")
last_name = input("What is your last name?")
age = int(input("How old are you?"))
occupation = input("What is your occupation?")
house_number = int(input("What number house do you live in?"))
address = input("What street do you live in?")
#Print the scam message
print("Thank you for responding to our scam add {}. You have notified us that your name is {} {}, and you are {} years old. You have also informed us that you currently live at {} {} and work as a {}. Carry on to the next page to voluntarily enter your bank account details.".format(first_name, first_name, last_name, age, house_number, address, occupation))
print("Thanks, have a nice day!")
print("Wait {}, hold on".format(first_name))
#Find out opinion about apples
apples = input("Do you like eating apples?")
if apples == "yes":
    print("That's goood, I may reconsider making you bankrupt")
if apples == "no":
    print("Wrong choice, suckers! Say goodbye to your money!!!!")
