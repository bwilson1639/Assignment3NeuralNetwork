import math
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

    trainingRate = 0.3

    trainingFile = open('train.txt', 'r')

    lineList = trainingFile.readlines()

    accuracy = 0
    epoch = 0

    nodeNetwork = initializeNodeNetwork()

    while accuracy < 90:

        accuracyTotal = 0
        totalTotal = 0
        for case in lineList:

            values = case.split()
            temp = 0
            isBias = False
            for Node in nodeNetwork[0]:
                if isBias != True:
                    isBias = True
                else:
                    Node.value = float(values[temp])

            isBias = False
            for Node in nodeNetwork[1]:

                if isBias !=True:
                    isBias = True
                else:
                    hiddenValue = 0

                    for INode in nodeNetwork[0]:
                        temp = 0
                        while temp < 10:
                            hiddenValue += INode.value * INode.weights[temp]
                            temp += 1

                    Node.value = 1 / (1 + math.exp(-hiddenValue))


            nodeOutput1 = 0.0
            nodeOutput8 = 0.0
            nodeOutput9 = 0.0

            for Node in nodeNetwork[1]:

                nodeOutput1 = nodeOutput1 + Node.value * Node.weights[0]

                nodeOutput8 = nodeOutput8 + Node.value * Node.weights[1]

                nodeOutput9 = nodeOutput9 + Node.value * Node.weights[2]


            sigNode1 = 1/(1 + math.exp(-nodeOutput1))
            sigNode8 = 1/(1 + math.exp(-nodeOutput8))
            sigNode9 = 1/(1 + math.exp(-nodeOutput9))

            if float(values[-3]) == 1.0 and sigNode1 >= sigNode8 and sigNode1 >= sigNode9:
                accuracyTotal += 1
            elif float(values[-2]) == 1.0 and sigNode8 > sigNode1 and sigNode8 >= sigNode9:
                accuracyTotal += 1
            elif float(values[-1]) == 1.0 and sigNode9 > sigNode1 and sigNode9 > sigNode8:
                accuracyTotal += 1

            #backwards propagation for output nodes
            deltaOne = (sigNode1 * (1.0 - sigNode1)) * (sigNode1 - float(values[-3]))

            for Node in nodeNetwork[1]:
                Node.weights[0] = Node.weights[0] + trainingRate * Node.value * deltaOne

            deltaEight = (sigNode8 * (1 - sigNode8)) * (sigNode8 - float(values[-2]))

            for Node in nodeNetwork[1]:
                Node.weights[1] = Node.weights[1] + trainingRate * Node.value * deltaEight

            deltaNine = (sigNode9 * (1 - sigNode9)) * (sigNode9 - float(values[-1]))

            for Node in nodeNetwork[1]:
                Node.weights[2] = Node.weights[2] + trainingRate * Node.value * deltaNine


            #calculate the product of weights times value
            temp = 0

            inputFunction = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            sigmaList = inputFunction
            deltaHidden = inputFunction
            for Node in nodeNetwork[0]:
                temp = 0

                while temp < len(nodeNetwork[1]):
                    inputFunction[temp] = inputFunction[temp] + Node.value * Node.weights[temp]
                    temp += 1

            temp = 0
            while temp < len(nodeNetwork[1]):
                sigmaList[temp] = 1/(1 + math.exp(-inputFunction[temp]))
                temp += 1


            temp = 0
            while temp < 11:
                derivative = sigmaList[temp] * (1 - sigmaList[temp])
                deltaHidden[temp] = derivative * nodeNetwork[1][temp].weights[0] * deltaOne
                deltaHidden[temp] += derivative * nodeNetwork[1][temp].weights[1] * deltaEight
                deltaHidden[temp] += derivative * nodeNetwork[1][temp].weights[2] * deltaNine
                temp += 1

            for Node in nodeNetwork[0]:
                temp = 0

                while temp < 11:
                    Node.weights[temp] = Node.weights[temp] + trainingRate + deltaHidden[temp]
                    temp += 1

            totalTotal += 1
        #end of for cae in lineList

        accuracy = (accuracyTotal / totalTotal) * 100
        print("accuracy is:" + str(accuracy))

        epoch += 1

trainingAlgorithm()