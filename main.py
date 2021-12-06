import random


class Node:

    def __init__(self, type):

        if type == 'input':
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

        elif type == 'hidden':
            self.w1 =random.uniform(-1.0 , 1.0)
            self.w2 = random.uniform(-1.0, 1.0)
            self.w3 = random.uniform(-1.0, 1.0)

        elif type == 'biasI':
            self.w1 = 1.0
            self.w2 = 1.0
            self.w3 = 1.0
            self.w4 = 1.0
            self.w5 = 1.0
            self.w6 = 1.0
            self.w7 = 1.0
            self.w8 = 1.0
            self.w9 = 1.0
            self.w10 = 1.0

        else:
            self.w1 = 1.0
            self.w2 = 1.0
            self.w3 = 1.0