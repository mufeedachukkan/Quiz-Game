print("Welcome to the QUIZ!!")

playing = input("Do you want to play the game? (yes/no)  ")

if playing.lower() != "yes":
    quit()

print("")
print("Okay!! Let's play the game!") 
print("")
print("RULES")
print("")
print("1. Each question carries 2 scores")
print("2. Each wrong answer will have a negative mark")
print("")
score = 0   

answer = input("Who invented computer?  ")
if answer.lower() == "Charles Babbage" or answer == "charles babbage" or answer == "CHARLES BABBAGE":
    print("Correct answer!")
    score = score+2
else:
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Second question!")
print("")

answer = input("What does CPU stand for?  ")
if answer.lower() == "Central Processing Unit" or answer == "central processing unit" or answer == "CENTRAL PROCESSING UNIT" or answer == "Central processing unit":
    print("Correct answer!")
    score += 2
else:
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Third question!")
print("")

answer = input("The first web browser is?  ")
if answer.lower() == "Mosaic" or answer == "mosaic" or answer == "MOSAIC":
    print("Correct answer!")
    score += 2

else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Fourth question!")
print("")

answer = input("What does CD stand for?  ")
if answer.lower() == "Compact Disk" or answer == "compact disk" or answer == "COMPACT DISK" or answer == "Compact disk":
    print("Correct answer!")
    score += 2
else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Fifth question!")
print("")

answer = input("What does FTP stand for?  ")
if answer.lower() == "File Transfer Protocol" or answer == "file transfer protocol" or answer == "FILE TRANSFER PROTOCOL" or answer == "File stansfer protocol":
    print("Correct answer!")
    score += 2
else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Sixth question!")
print("")

answer = input("The common name for the crime of stealing passwords is?  ")
if answer.lower() == "Spoofing" or answer == "spoofing" or answer == "SPOOFING":
    print("Correct answer!")
    score += 2
else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Seventh question!")
print("")

answer = input("Name of 1st electronic computer?  ")
if answer.lower() == "ENIAC" or answer == "eniac" or answer == "Eniac":
    print("Correct answer!")
    score += 2
else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Eighth question!")
print("")

answer = input("What does RAM stand for?  ")
if answer.lower() == "Random Access Memory" or answer == "random access memory" or answer == "RANDOM ACCESS MEMORY" or answer == "Random access memory":
    print("Correct answer!")
    score += 2
else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Ninth question!")
print("")

answer = input("What does GPU stand for? ")
if answer.lower() == "Graphics Processing Unit" or answer == "graphics processing unit" or answer == "GRAPHICS PROCESSING UNIT" or answer == "Graphics processing unit":
    print("Correct answer!")
    score += 2
else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("")
print("Last question!")
print("")

answer = input("What is the scientific name of the computer?  ")
if answer.lower() == "Sillico Sapiens" or answer == "silico sapiens" or answer == "SILICO SAPIENS" or answer == "Silico sapiens":
    print("Correct answer!")
    score += 2
else: 
    print("Sorry! The answer is wrong!")
    score = score-1

print("You got " + str(score) + " score out of 20")
print("You got " + str((score/20) * 100) + "%")