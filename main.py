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

def trainingAlgorithm (inputFile, outputFile) :

    trainingRate = 0.2

    trainingFile = open(inputFile, 'r')

    lineList = trainingFile.readlines()

    trainingFile.close()


    accuracy = 0
    epoch = 0

    nodeNetwork = initializeNodeNetwork()




    while accuracy < 95:

        accuracyTotal = 0
        totalTotal = 0

        targetValues = []
        actualValues = []

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

            error = []
            temp = 0
            while temp < 3:
                calculate = output[temp] - outputLayer[temp]
                error.append(calculate)
                temp += 1


            deltaoutput = []
            temp = 0
            while temp < 3:
                calculate = error[temp] * derivative(outputLayer[temp])
                deltaoutput.append(calculate)
                temp += 1


            temp = 0
            while temp < len(hiddenLayer):
                for i in range(3):
                    nodeNetwork[1][temp].weights[i] += trainingRate * nodeNetwork[1][temp].value * deltaoutput[i]
                temp += 1

            hiddenLayer.pop(0)

            deltaHidden = []
            temp = 0

            while temp < 10:
                calculate = 0
                calculate =  nodeNetwork[1][temp].weights[0] * deltaoutput[0]
                calculate += nodeNetwork[1][temp].weights[1] * deltaoutput[1]
                calculate += nodeNetwork[1][temp].weights[2] * deltaoutput[2]
                deltaHidden.append(calculate * derivative(hiddenLayer[temp]))
                temp += 1


            temp = 0
            while temp < len(nodeNetwork[0]):
                innerTemp = 0
                while innerTemp < 10:
                    nodeNetwork[0][temp].weights[innerTemp] += trainingRate * nodeNetwork[0][temp].value * deltaHidden[innerTemp]
                    innerTemp += 1
                temp += 1


            if float(output[0]) == 1.0 and outputLayer[0] >= outputLayer[1] and outputLayer[0] >= outputLayer[2]:
                accuracyTotal += 1
            elif float(output[1]) == 1.0 and outputLayer[1] > outputLayer[0] and outputLayer[1] >= outputLayer[2]:
                accuracyTotal += 1
            elif float(output[2]) == 1.0 and outputLayer[2] > outputLayer[0] and outputLayer[2] > outputLayer[1]:
                accuracyTotal += 1

            totalTotal += 1

            if output[0] > output[1] + output[2]:
                targetValues.append('1')

            elif output[1] > output[0] + output[2]:
                targetValues.append('8')

            else:
                targetValues.append('9')

            if outputLayer[0] > outputLayer[1] and outputLayer[0] > outputLayer[2]:
                actualValues.append('1')
            elif outputLayer[1] > outputLayer[0] and outputLayer[1] > outputLayer[2]:
                actualValues.append('8')
            else:
                actualValues.append('9')


        epoch += 1
        accuracy = (accuracyTotal/totalTotal) * 100
        print(str(accuracy) + " " + str(epoch))

        trainingStringFile = open(outputFile, 'w')

        trainingStringFile.write("my_predicted_digit target(correct_digit)\n")
        temp = 0

        while temp < len(actualValues):
            tempString = str(targetValues[temp]) + "                   " + str(actualValues[temp]) + "\n"
            trainingStringFile.write(tempString)
            temp += 1

        tempString = "Accuracy: " + str(accuracyTotal) + "/" + str(totalTotal) + "=" + str(round(accuracy, 4))

        trainingStringFile.write(tempString)
        trainingStringFile.close()


        #to save the data
        #line 1: weights of input: "w1,w2,w3,w4,w5,w6,w7,w8,w9,w10 ... wn8,wn9,wn10\n
        #line 2: weights of hidden input "w1,w2,w3 w1,w2,w3 w1,w2,w3"

        trainingOutputFile = open("neuralNetwork.txt", 'w')
        inputWeightLine = ""

        temp = 0
        while temp < len(nodeNetwork[0]):

            innerTemp = 0

            while innerTemp < 10:
                if innerTemp == 0:
                    inputWeightLine = inputWeightLine + str(nodeNetwork[0][temp].weights[innerTemp])

                else:
                    inputWeightLine = inputWeightLine + "," + str(nodeNetwork[0][temp].weights[innerTemp])
                innerTemp += 1

            inputWeightLine = inputWeightLine + " "

            temp += 1

        inputWeightLine = inputWeightLine + "\n"
        trainingOutputFile.write(inputWeightLine)

        hiddenWeightLine = ""

        temp = 0
        while temp < len(nodeNetwork[1]):

            innerTemp = 0

            while innerTemp < 3:
                if innerTemp == 0:
                    hiddenWeightLine = hiddenWeightLine + str(nodeNetwork[1][temp].weights[innerTemp])

                else:
                    hiddenWeightLine = hiddenWeightLine + "," + str(nodeNetwork[1][temp].weights[innerTemp])
                innerTemp += 1

            hiddenWeightLine = hiddenWeightLine + " "

            temp += 1

        trainingOutputFile.write(hiddenWeightLine)

        trainingOutputFile.close()


        #create output



trainingAlgorithm('train.txt', "train_output.txt")