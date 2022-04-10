import numpy as np
import random

data = []
dataRepre = []
dataGroup = []
groupCount = []

# data의 group을 할당해주는 메소드
def clusterAssign(k) :
    global data, dataRepre, dataGroup, groupCount
    
    groupCount = [0] * k
    for i in range(len(data)) :
        groupIdx = 0
        mn = np.linalg.norm(data[i] - dataRepre[0], 2)
        for j in range(1, len(dataRepre)) :
            temp = np.linalg.norm(data[i] - dataRepre[j], 2)
            if mn > temp :
                mn = temp
                groupIdx = j
        dataGroup[i] = groupIdx                             # i번째 data가 몇번째 group인지 갱신
        groupCount[groupIdx] += 1
        
# group의 representatives를 재설정하는 메소드
def choiceRepre() :
    global data, dataRepre, dataGroup, groupCount
    
    for groupIdx in range(len(dataRepre)) :
        temp = np.array([0] * len(data[0]))                 # 빈 np.array 생성
        for i in range(len(data)) :
            if dataGroup[i] == groupIdx :
                temp += data[i]
        dataRepre[groupIdx] = temp / groupCount[groupIdx]
    
# 초기 설정 메소드
def initRepre(k) :
    global data, dataRepre, dataGroup, groupCount
    
    groupCount = [0] * k
    dataGroup = [0] * len(data)
    s = set()
    while len(s) != k :
        idx = int(random.random() * len(data))
        s.add(idx)
    for i in range(len(s)) :
        dataRepre.append(data[s.pop()])

# main method
def main() :
    dataFile = open("inputVectors10.txt", 'r')
    global data, dataRepre, dataGroup, groupCount
    
    while True :
        line = list(map(int, dataFile.readline().split()))
        if not line :
            break
        data.append(np.array(line))
        
    k = int(input())        # group num
    iter = int(input())     # iteration
    
    initRepre(k)

    for i in range(iter) :
        print("Representatives: ", end='')
        for j in range(len(dataRepre)) :
            if j == k - 1 :
                print(dataRepre[j])
                break
            print(dataRepre[j], end=', ')
        clusterAssign(k)
        print("vecters: ", groupCount)
        print()
        choiceRepre()
    
    # for i in range(iter) :
    #     clusterAssign(k)
    #     choiceRepre()
    # for i in range(len(dataRepre)) :
    #         if i == k - 1 :
    #             print(dataRepre[i])
    #             break
    #         print(dataRepre[i], end=', ')
    # print("vecters: ", groupCount)
        
    dataFile.close()

main()