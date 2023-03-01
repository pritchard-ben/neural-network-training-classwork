data = [(1,4,-1),(2,9,1),(5,6,1),(4,5,1),(6,0.7,-1),(1,1.5,-1)]
def TrainingAlg(data):
    w = (0,0,0)
    change = True
    while change:
        change = False
        for vector in data:
            s = (w[0] + w[1] * vector[0] + w[2] * vector[1])
            if (vector[2]) == 1: #will be correct if positive
                if s <= 0:
                    w = (w[0] + 1, w[1] + vector[0], w[2] + vector[1])
                    change = True
            else: #will be correct if negative
                if s >= 0:
                    w = (w[0] - 1, w[1] - vector[0], w[2] - vector[1])
                    change = True
    return w
print(TrainingAlg(data))