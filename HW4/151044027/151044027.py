import queue
#PART2 START
def kthElem(list1, list2, k, m, n):

	if k == 1:
		if list1[0] > list2[0]:
			return list2[0]
		else:
			return list1[0]


	if(m <= k // 2):
		firstPivot = m
	else:
		firstPivot = k // 2


	if(n <= k // 2):
		secondPivot = n
	else:
		secondPivot = k // 2


	if(list1[firstPivot - 1] <= list2[secondPivot - 1]):
		return kthElem(list1[firstPivot:], list2, k - firstPivot,  m - firstPivot, n)
	else:
		return kthElem(list1, list2[secondPivot:], k - secondPivot, m,  n - secondPivot)

#PART2 END



#PART3 START
	
def maxContSubArray(mylist, lowBound, highBound):
    
    if(highBound == lowBound):
        return mylist[0]

    mid = (lowBound + highBound) // 2

    leftLimit = -999999
    sum = 0

    counter = mid

    while(counter >= lowBound):
        sum = sum + mylist[counter]
        if(sum > leftLimit):
            leftLimit = sum
        counter = counter - 1


    rightLimit = -999999
    sum = 0
    counter = mid + 1
    while(counter <= highBound):
        sum = sum + mylist[counter]
        if(sum > rightLimit):
            rightLimit = sum

        counter = counter + 1

    leftOne = maxContSubArray(mylist, lowBound, mid)
    rightOne = maxContSubArray(mylist, mid + 1, highBound)


    if(leftOne > rightOne):
        max_left_right = leftOne
    else:
        max_left_right = rightOne


    if(max_left_right > leftLimit + rightLimit):
        return max_left_right
    else:
        return leftLimit + rightLimit


#PART3 END


#PART4 START

def findBipartite(graph, src):
	colorList = []
	for counter in range(len(graph)):
		colorList.append(-1)


	colorList[src] = 1


	Q = queue.Queue(maxsize=16)
	Q.put(src) 


	while(not Q.empty()):
		top = Q.get()

		if(graph[top][top] == 1):
			return False

		for vertice in range (len(graph)):
			if(graph[top][vertice] != 0):
				if(colorList[vertice] == -1):		
					colorList[vertice] = -2
					Q.put(vertice)
			elif(graph[top][vertice] != 0):
				if(colorList[vertice] == colorList[top]):
					return False
				
	return True


#PART4 END





#PART5 START 



def partition (mylist, left, right):
	pivot = mylist[right]
	pivotloc = left

	counter = left

	for counter in range (right + 1):
		if(mylist[counter] < pivot):
			tempElem = mylist[counter]
			mylist[counter] = mylist[pivotloc]
			mylist[pivotloc] = tempElem
			pivotloc = pivotloc + 1


	tempElem = mylist[right]
	mylist[right] = mylist[pivotloc]
	mylist[pivotloc] = tempElem

	return pivotloc





def quickSelect(mylist, left, right, rank):

	part = partition(mylist, left, right)

	if(part < rank):
		return quickSelect(mylist,part + 1, right, k)
	elif(part == rank):
		return mylist[part]
	else:
		return quickSelect(mylist, left, part - 1, rank)


def wareHouseProfit():
	C = [5, 11, 2, 21, 5, 7, 8, 12, 13, 0]
	P = [0, 7, 9, 5, 21, 7, 13, 10, 14, 20]


	differences = []


	for x in range (len(C)- 1):
		if((P[x + 1] - C[x]) == 0):
			print("Can't sell for day:", x + 1)
		differences.append(P[x + 1] -C[x])

	print("Differences: " , differences)
	res = quickSelect(differences, 0, len(differences) - 1, len(differences) - 1)
	day=differences.index(res)
	return day + 1


#PART5 END
def specialArrayConstruct():
	specialArr = [[10,17,13,28,23],
				  [17,22,16,29,23],
				  [24,28,22,34,24],
				  [11,13,6,17,7],
				  [45,44,32,37,23],
				  [36,33,19,21,6],
				  [75,66,51,53,34]]

	rowList = []
	colList = []
	counter = 0
	for x in range (len(specialArr) - 1):

		for y in range (len(specialArr[0]) - 1):
			if((specialArr[x][y] + specialArr[x + 1][y + 1]) < (specialArr[x][y + 1] + specialArr[x+1][y])):
				colList.append(specialArr[x][y])
			else:
				counter = counter + 1
				specialArr[x][y] = (specialArr[x][y + 1] + specialArr[x+1][y])


		rowList.append(colList)
		colList = []
	if(counter == 1):
		return rowList
	else:
		rowList = []
		return rowList

print("\n\n*****Special array problem test starts.*****\n\n")

myArr = []
myArr = specialArrayConstruct();
if(len(myArr) == 0):
	print("Can't construct an array.")
else:
	print("Array constructed as:", myArr)

print("\n\n*****Special array test ends.*****\n\n")

print("\n\n*****Warehouse problem test starts.*****\n\n")
#if you want to change the input values for wareHouse problem please change
#inside wareHouseProfit function.
print("Best day to sell is:",wareHouseProfit())
print("\n\n*****Warehouse problem test ends.*****\n\n")



print("\n\n*****Bipartite problem test starts.*****\n\n")
graph = [[0, 1, 0, 1],
		 [1, 0, 1, 1],
		 [0,1, 0, 1],
		 [1, 1, 1, 0]
		]

if(findBipartite(graph, 0) == True):
	print("Graph is bipartite.")
else:
	print("Graph is not bipartite.")


print("\n\n*****Bipartite problem test ends.*****\n\n")




print("\n\n*****Contiguous subset problem test starts.*****\n\n")

myList3 = [2,-4,1,9,-6,7,-3]

print(maxContSubArray(myList3, 0, 6))

print("\n\n*****Contiguous subset problem test ends.*****\n\n")



print("\n\n*****kth element of two sorted arrays problem test starts.*****\n\n")
myList1 = [1,3,5,7,9,10,21,324]
myList2 = [0,2,4,6,8,123,344,1111]


print(kthElem(myList1, myList2, 12, 8, 8 ))

print("\n\n*****kth element of two sorted arrays problem test ends.*****\n\n")