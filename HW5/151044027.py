#Helper.
def getMemoryContent(memoryCost):
    sum = 0
    for x in range (len(memoryCost)):
        sum = sum + memoryCost[x]


    return sum
#part5
def ancientCPUGreedy(ancientMemory):

    ancientMemory.sort()
    memoryCost = []

    for x in range (len(ancientMemory) - 1):
        memoryRegister = ancientMemory[x] + ancientMemory[x + 1]
        memoryCost.append(memoryRegister)

    

    sum = getMemoryContent(memoryCost)
    #print(memoryCost)
    return sum


#part1
def dpMinCost(NY, SF, n, M):

    NYCost = []
    SFCost = []

    for x in range (n):
        if(x == 0):
            NYCost.append(NY[0])
            SFCost.append(SF[0])
        else:
            NYCost.append(NY[x] + min(M + SFCost[x-1],NYCost[x-1]))
            SFCost.append(SF[x] + min(M + NYCost[x-1],SFCost[x-1]))
    
    return min(NYCost[n-1], SFCost[n-1])




#part4
def alignmentProblem(match,miss,space,seqA,seqB):
    
    #Create 2d string array.
    string = [[0 for x in range(len(seqA) + 1)] for y in range(len(seqB) + 1)] 
    stringSpace = (len(seqA) + len(seqB)) // 2
    for a in range (stringSpace):
        x = 0
        while( x < len(seqB) + 1):
            string[x][0] = space*x
            x = x + 1
        x = 0
        while( x < len(seqA) + 1):
            string[0][x] = space*x
            x = x + 1
        stringSpace = x + 1
    x = 1
    y = 1
    while(x < (len(seqB) + 1)):
        while(y < (len(seqA) + 1)):
            gapMiss = miss
            if seqA[y-1] != seqB[x-1]:
                stringSpace = 0
            else:
                gapMiss = match
            string[x][y] = max(string[x-1][y-1] + gapMiss, string[x-1][y] + space, string[x][y-1] + space) 
            y = y + 1   
        x = x + 1
        y = stringSpace + 1
    return max(*[string[x][len(seqA)] for x in range(len(seqB) + 1)], *[string[len(seqB)][x] for x in range(len(seqA) + 1)])
    


#part3
#Source: https://www.studytonight.com/data-structures/activity-selection-problem
def printMaxActivities(start, finish): 
    schedule = []
    i = 0
    schedule.append(i)
    
    currentInterval = len(finish) 

    for j in range(currentInterval): 
        if (start[j] < finish[i]):
            print("non-append", schedule)
        else: 
            schedule.append(j)
            i = j 
        

    return schedule
print("Alignment Problem:")
print(alignmentProblem(2,-2,-1,"ALIGNMENT","SLIME"))









SF = [50, 20, 2, 4]
NY = [1, 3, 20, 30]
M = 10
n = 4
print("MinCost:")
print(dpMinCost(NY,SF,4,10))










ancientMemory = [2,1,30,12,34,4]


print("With greedy method operation count is:", ancientCPUGreedy(ancientMemory))

  
s = [1 , 3 , 0 , 5 , 6 , 8] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
print(printMaxActivities(s , f)) 
  