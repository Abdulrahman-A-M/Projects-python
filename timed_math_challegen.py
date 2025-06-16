import random
import time

OPERATORS=['+','-','*']
MIN_OPERATOR=1
MAX_OPERATOR=10
TOTAL_PROBMLES=10
def generator_problmes():
    left=random.randint(MIN_OPERATOR,MAX_OPERATOR)
    right=random.randint(MIN_OPERATOR,MAX_OPERATOR)
    choice=random.choice(OPERATORS)
    eprx= str(left) + ' ' + choice +' '+str(right)
    answer=eval(eprx)
    return eprx ,answer


wrong=0
input('Enter to start: ')
start=time.time()
print(20*'-')

for i in range(TOTAL_PROBMLES):
    epxr, answer=generator_problmes()
    while True:
        guess=input('Promble #'+ str(i+1)+': ' +epxr +'=')
        if guess == str(answer):
            break
        wrong +=1

end=time.time()

total_time=end-start
print(20*'-')
print('Nice work you tak time',round(total_time),'s\nand you wrog',wrong)