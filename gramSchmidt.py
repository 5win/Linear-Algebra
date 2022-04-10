import numpy as np

data = []
orthonormal = []

def gramSch() :
    global data, orthonormal
    
    for i in range(len(data)) :
        rhs = np.array([0.0] * len(data[0]))
        for j in range(i) :
           rhs += np.inner(orthonormal[j], data[i]) * orthonormal[j]
        qTilde = data[i] - rhs
        qTildeNorm = np.linalg.norm(qTilde, 2)
        if qTildeNorm < 3e-10 :
            return False
        q = qTilde / qTildeNorm
        orthonormal.append(q)
        for k in range(len(orthonormal)) :
            if k == len(orthonormal) - 1 :
                print(orthonormal[k])
                break
            print(orthonormal[k], end=", ")
            
    return True

def main() :
    global data
    
    dataFile = open("inputGram.txt", 'r')
    while True :
        line = list(map(int, dataFile.readline().split()))
        if not line :
            break
        data.append(np.array(line))
        
    if gramSch() :
        print("Linearly independent", end="\n\n")
    else :
        print("Linearly dependent", end="\n\n")

main()