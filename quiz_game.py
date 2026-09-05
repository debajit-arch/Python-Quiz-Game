print("Welcome to my Computer quiz!")

playing = input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()

print("Okey! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which component acts as the main permanent storage device? ")
if answer.lower() == "hard drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the basic unit of digital information that consists of a 0 or 1? ")
if answer.lower() == "bit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many bits are in a byte? ")
if answer.lower() == "8":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What unique string of numbers identifies a device on a network? ")
if answer.lower() == "ip address":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the main circuit board of a computer called? ")
if answer.lower() == "motherboard":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What type of software is used to access and view web pages? ")
if answer.lower() == "web browser":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")

if score == 10:
    print("Congratulations! You are a computer genius!")
elif score >= 7:
    print("Great job! You have a good understanding of computer basics!")
elif score >= 2:
    print("No worries! Keep learning and you'll get better!")
else:
    print("Don't be discouraged! Keep studying and you'll improve!")