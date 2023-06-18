Name= input("what is your name?\n")
print("welcome" ,Name ,"to the Computer quiz game!")

quest =input("Do you want to play?\n").lower()

if quest != "yes":

  quit()
score =0
print("Okay!, lets begin\n")

ans =input("what is an AI?\n").lower()
if ans == "artificial intelligence":
  print("correct!")
  score+=1
else:
  print("incorrect!")
  
  ans = input("what is an ML?\n").lower()
if ans == "machine learning":
  print("correct!")
  score += 1
else:
  print("incorrect!")

ans = input("what is IP?\n").lower()
if ans == "internet protocol":
  print("correct!")
  score += 1
else:
  print("incorrect!")

ans = input("what is HTML?\n").lower()
if ans == "hypertext markup language":
  print("correct!")
  score += 1
else:
  print("incorrect!")

ans = input("what is an CSS?\n").lower()
if ans == "cascading style sheet":
  print("correct!")
  score += 1
else:
  print("incorrect!")
  
  print("you got" + str(score) + " questions correctly!")
  print("you got " + str((score / 5 ) *100) + "%")
  
