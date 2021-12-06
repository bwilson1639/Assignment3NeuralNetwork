import random


class Node:

    def __init__(self, type):

        if type == 'input':
            self.value = 0
            self.w1 = random.uniform(-1.0,1.0)
            self.w2 = random.uniform(-1.0, 1.0)
            self.w3 = random.uniform(-1.0, 1.0)
            self.w4 = random.uniform(-1.0, 1.0)
            self.w5 = random.uniform(-1.0, 1.0)
            self.w6 = random.uniform(-1.0, 1.0)
            self.w7 = random.uniform(-1.0, 1.0)
            self.w8 = random.uniform(-1.0, 1.0)
            self.w9 = random.uniform(-1.0, 1.0)
            self.w10 = random.uniform(-1.0, 1.0)
            self.weights = [self.w1, self.w2, self.w3, self.w4, self.w5, self.w6. self.w7, self.w8, self.w9, self.w10]

        elif type == 'hidden':
            self.value = 0
            self.w1 =random.uniform(-1.0 , 1.0)
            self.w2 = random.uniform(-1.0, 1.0)
            self.w3 = random.uniform(-1.0, 1.0)
            self.weights = [self.w1, self.w2, self.w3]

        elif type == 'biasI':
            self.value = 1
            self.w1 = random.uniform(-1.0, 1.0)
            self.w2 = random.uniform(-1.0, 1.0)
            self.w3 = random.uniform(-1.0, 1.0)
            self.w4 = random.uniform(-1.0, 1.0)
            self.w5 = random.uniform(-1.0, 1.0)
            self.w6 = random.uniform(-1.0, 1.0)
            self.w7 = random.uniform(-1.0, 1.0)
            self.w8 = random.uniform(-1.0, 1.0)
            self.w9 = random.uniform(-1.0, 1.0)
            self.w10 = random.uniform(-1.0, 1.0)
            self.weights = [self.w1, self.w2, self.w3, self.w4, self.w5, self.w6. self.w7, self.w8, self.w9, self.w10]

        else:
            self.value = 1
            self.w1 = random.uniform(-1.0, 1.0)
            self.w2 = random.uniform(-1.0, 1.0)
            self.w3 = random.uniform(-1.0, 1.0)
            self.weights = [self.w1, self.w2, self.w3]

def initializeNodeNetwork ():

    inputLayer = []
    hiddenLayer = []
    #output layer just numbers, doesn't need nodes

    temp = 0

    while temp < 257:

        if temp == 0:
            inputLayer[0] = Node('biasI')

        else:
            inputLayer[temp] = Node('input')

    temp = 0

    while temp < 11:

        if temp == 0:
            hiddenLayer[0] = Node('biasH')

        else:
            hiddenLayer[temp] = Node('hidden')


    return [inputLayer, hiddenLayer]