import random
import re

abc123 = ['2', 'b', 'c','w','2','x','t','R','m','A','K','0','5','3','V','W','x','V','s','a','LK','Ma','ra','la','sL','f','F','8','12','78']

def gettoken(characters=20):
    token = ''
    for i in range(0, characters):
        getrandom = random.choice(abc123)
        token += getrandom
    return token
        

class count():
    def __init__(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        self.question = f"{num1} + {num2}"
        self.response = num1 + num2
            
            
class words():
    def __init__(self):
        lista = {'blue planet':'Our planet is known as the?...','water':'Fish live in the?...','blue':'The sky is?...', 'green':'Blue + Yellow is?...', 'Excalibur':'The legend of King Arthur and the sword?...'}
        
        self.question = random.choice(list(lista.items()))
        self.ask = self.question[0]
        self.answer = self.question[1]
            
print(gettoken(10))
            
number = count()
print(number.question)
print(number.response)

word = words()
print(word.ask)
print(word.answer)