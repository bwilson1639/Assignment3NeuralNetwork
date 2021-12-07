import random


class Node:

    def __init__(self, type):

        if type == 'input':
            self.value = 0
            w1 = random.uniform(-1.0,1.0)
            w2 = random.uniform(-1.0, 1.0)
            w3 = random.uniform(-1.0, 1.0)
            w4 = random.uniform(-1.0, 1.0)
            w5 = random.uniform(-1.0, 1.0)
            w6 = random.uniform(-1.0, 1.0)
            w7 = random.uniform(-1.0, 1.0)
            w8 = random.uniform(-1.0, 1.0)
            w9 = random.uniform(-1.0, 1.0)
            w10 = random.uniform(-1.0, 1.0)
            self.weights = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10]

        elif type == 'hidden':
            self.value = 0
            w1 =random.uniform(-1.0 , 1.0)
            w2 = random.uniform(-1.0, 1.0)
            w3 = random.uniform(-1.0, 1.0)
            self.weights = [w1, w2, w3]

        elif type == 'biasI':
            self.value = 1
            w1 = random.uniform(-1.0, 1.0)
            w2 = random.uniform(-1.0, 1.0)
            w3 = random.uniform(-1.0, 1.0)
            w4 = random.uniform(-1.0, 1.0)
            w5 = random.uniform(-1.0, 1.0)
            w6 = random.uniform(-1.0, 1.0)
            w7 = random.uniform(-1.0, 1.0)
            w8 = random.uniform(-1.0, 1.0)
            w9 = random.uniform(-1.0, 1.0)
            w10 = random.uniform(-1.0, 1.0)
            self.weights = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10]

        else:
            self.value = 1
            w1 = random.uniform(-1.0, 1.0)
            w2 = random.uniform(-1.0, 1.0)
            w3 = random.uniform(-1.0, 1.0)
            self.weights = [w1, w2, w3]

def initializeNodeNetwork ():

    inputLayer = []
    hiddenLayer = []
    #output layer just numbers, doesn't need nodes

    temp = 0

    while temp < 257:

        if temp == 0:
            inputLayer.append(Node('biasI'))
            temp += 1

        else:
            inputLayer.append(Node('input'))
            temp += 1

    temp = 0

    while temp < 11:

        if temp == 0:
            hiddenLayer.append(Node('biasH'))
            temp += 1

        else:
            hiddenLayer.append(Node('hidden'))
            temp += 1


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

            values = case.split()
            temp = 0
            isBias = False
            for Node in nodeNetwork[0]:
                if isBias != True:
                    isBias = True
                else:
                    Node.value = float(values[temp])


            for Node in nodeNetwork[1]:

                hiddenValue = 0


                for INode in nodeNetwork[0]:
                    temp = 0
                    while temp < 10:
                        hiddenValue += INode.value * INode.weights[temp]
                        temp += 1

                Node.value = hiddenValue

            outputNode1 = 0
            outputNode8 = 0
            outputNode9 = 0

            for Node in nodeNetwork[1]:

                outputNode1 = outputNode1 + Node.value * Node.weights[0]
                print(outputNode1)
                outputNode8 = outputNode8 + Node.value * Node.weights[1]
                print(outputNode8)
                outputNode9 = outputNode9 + Node.value * Node.weights[2]
                print(outputNode9)

            if values[-3] == 1 and outputNode1 >= outputNode8 and outputNode1 >= outputNode9:
                accuracyTotal += 1
            elif values[-2] == 1 and outputNode8 > outputNode1 and outputNode8 >= outputNode9:
                accuracyTotal += 1
            elif values[-1] == 1 and outputNode9 > outputNode1 and outputNode9 > outputNode8:
                accuracyTotal += 1



        epoch += 1

trainingAlgorithm()