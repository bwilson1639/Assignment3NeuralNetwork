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

def trainingAlgorithm () :

    trainingFile = open('test.txt', 'r')

    lineList = trainingFile.readlines()

    accuracy = 0
    epoch = 0

    nodeNetwork = initializeNodeNetwork()

    while accuracy < 90:

        accuracyTotal = 0

        for case in lineList:

            values = lineList.split()
            temp = 0

            for Node in nodeNetwork[0]:
                if Node.value != 0:

                    Node.value = values[temp]

            temp = 0
            for Node in nodeNetwork[1]:

                hiddenValue = 0
                if Node.value != 0:

                    for INode in nodeNetwork[0]:

                        hiddenValue = hiddenValue + INode.value * INode.weights[temp]

                temp += 1
                Node.value = hiddenValue

            outputNode1 = 0
            outputNode8 = 0
            outputNode9 = 0

            for Node in nodeNetwork[1]:

                outputNode1 = outputNode1 + Node.value * Node.weights[0]
                outputNode8 = outputNode8 + Node.value * Node.weights[1]
                outputNode9 = outputNode9 + Node.value * Node.weights[2]

            if values[-3] == 1 and outputNode1 >= outputNode8 and outputNode1 >= outputNode9:
                accuracyTotal += 1
            elif values[-2] == 1 and outputNode8 > outputNode1 and outputNode8 >= outputNode9:
                accuracyTotal += 1
            elif values[-1] == 1 and outputNode9 > outputNode1 and outputNode9 > outputNode8:
                accuracyTotal += 1
            else:
                continue
                #backwards propagate

        epoch += 1