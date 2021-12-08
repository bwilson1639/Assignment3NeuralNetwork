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

def sigmoidFuncion(value):
    output = 1 / (1 + math.exp(-value))
    return float(output)

def derivative(value):
    output = value * (1- value)
    return float(output)

def trainingAlgorithm () :

    trainingRate = 0.2

    trainingFile = open('train.txt', 'r')

    lineList = trainingFile.readlines()

    accuracy = 0
    epoch = 0

    nodeNetwork = initializeNodeNetwork()

    for line in lineList:

        binaryValue = line[-8:].split()
        line = line[:-8].split()

        line = [1.0] + line
        input = []
        output = []
        for value in line:
            value = float(value)
            input.append(value)

        for value in binaryValue:
            value = float(value)
            output.append(value)

        temp = 0
        while temp < (len(nodeNetwork[0])):
            nodeNetwork[0][temp].value = input[temp]
            temp += 1


        hiddenLayer = []
        temp = 0
        while temp < 10:
            sum = 0
            innerTemp = 0
            while innerTemp < len(nodeNetwork[0]):
                sum += (nodeNetwork[0][innerTemp].weights[temp] * nodeNetwork[0][innerTemp].value)
                innerTemp += 1
            hiddenLayer.append(sigmoidFuncion(sum))
            temp += 1
        hiddenLayer = [1.0] + hiddenLayer

        temp = 0
        while temp < len(nodeNetwork[1]):
            nodeNetwork[1][temp].value = hiddenLayer[temp]
            temp += 1

        outputLayer = []

        temp = 0
        while temp < 3:
            sum = 0
            innerTemp = 0
            while innerTemp < len(nodeNetwork[1]):
                sum += (nodeNetwork[1][innerTemp].weights[temp] * nodeNetwork[1][innerTemp].value)
                innerTemp += 1
            outputLayer.append(sigmoidFuncion(sum))
            temp += 1
        print(outputLayer)

        error = []
        temp = 0
        while temp < 3:
            calculate = output[temp] - outputLayer[temp]
            error.append(calculate)
            temp += 1

        print(error)

        deltaoutput = []
        temp = 0
        while temp < 3:
            calculate = error[temp] * derivative(outputLayer[temp])
            deltaoutput.append(calculate)
            temp += 1

        print(deltaoutput)

        temp = 0
        while temp < len(hiddenLayer):
            for i in range(3):
                nodeNetwork[1][temp].weights[i] += trainingRate * nodeNetwork[1][temp].value * deltaoutput[i]
            temp += 1

        hiddenLayer.pop(0)

        deltaHidden = []
        temp = 0
        print(deltaHidden)
        print()
        while temp < 10:
            calculate = 0
            calculate =  nodeNetwork[1][temp].weights[0] * deltaoutput[0]
            calculate += nodeNetwork[1][temp].weights[1] * deltaoutput[1]
            calculate += nodeNetwork[1][temp].weights[2] * deltaoutput[2]
            deltaHidden.append(calculate * derivative(hiddenLayer[temp]))
            temp += 1

        print(deltaHidden)

        temp = 0
        while temp < len(nodeNetwork[0]):
            innerTemp = 0
            while innerTemp < 10:
                nodeNetwork[0][temp].weights[innerTemp] += trainingRate * nodeNetwork[0][temp].value * deltaHidden[innerTemp]
                innerTemp += 1
            temp += 1

        

        break



trainingAlgorithm()