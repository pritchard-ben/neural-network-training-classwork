import random

data = [(1,4,-1),(2,9,1),(5,6,1),(4,5,1),(6,0.7,-1),(1,1.5,-1)]

def adaline(data):
    for y in range(0,5000):
        w = [0,0,0]
        w[0] = random.random()
        w[1] = random.random()
        w[2] = random.random()
        P = 0.01
        for vector in data:
            s = (w[0] + w[1] * vector[0] + w[2] * vector[1])
            # difference = vector[2] - s
            # print(difference)
            for i in range(0,3):
                w[i] = w[i] + P * (vector[2] - s) * vector[i]
    return w
            
print(adaline(data))