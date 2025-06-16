print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower() !='yes':
    quit()

print("Okay! Let's play :")

sore = 0
answer=input('What does CPU stand for? ').lower()
if answer =='central processing unit':
      print('Correct!')
      sore +=1
else:
     print('Incorrect!')

answer=input('What does GPU stand for? ').lower()
if answer=='graphics processing unit':
      print('Correct!')
      sore +=1
else:
     print('Incorrect!')

answer=input('What does RAM stand for? ').lower()
if answer=='random access memeory':
      print('Correct!')
      sore +=1
else:
     print('Incorrect!')

answer=input('What does PSU stand for? ').lower()
if answer=='power supply':
      print('Correct!')
      sore +=1
else:
     print('Incorrect!')

print('Yor got ' + str(sore) +' qeustions correct!')
print('Yor got ' + str(sore/4 * 100) +'%.')




#FROM ME 
print("Welcome to quiz game :>)!")

playing=input("Do you want to play? ")

if playing.lower() !='yes':
    quit()

print("Okay! Let's play :")
print()
sore = 0
answer=input('What does CPU stand for?\nA: Graphic processing unit\nB: Central processing unit\nC: Processing unit\nD: Random acess memeory :').lower()
print()
if answer =='b':
      sore +=1


answer=input('What does GPU stand for?\nA: Graphics processing unit\nB: Central processing unit\nC: Processing unit\nD: Random acess memeory :').lower()
if answer=='a':
      sore +=1


answer=input('What does RAM stand for?\nA: Graphic processing unit\nB: Central processing unit\nC: Processing unit\nD: Random acess memeory :').lower()
if answer=='d':
      sore +=1


answer=input('What does PSU stand for?\nA: Graphic processing unit\nB: Power Supply\nC: Processing unit\nD: Random acess memeory :').lower()
if answer=='b':
      sore +=1


answer=input('What does IS stand for?\nA: Graphic processing unit\nB: Power Supply\nC: Information system\nD: Random acess memeory :').lower()
if answer=='c':
      sore +=1



print('Yor got ' + str(sore) +' qeustions correct!')
print('Yor got ' + str(sore/5 * 100) +'%.')