import random
import math


#Swap function for simple swapping operation on list.
def swapBoxes(boxList, index1, index2):
	firstBox = boxList.pop(index1);
	secondBox = boxList.pop(index2 - 1);

	boxList.insert(index1, secondBox)
	boxList.insert(index2, firstBox)

	return boxList
#Function that defines our main problem.
#Creates the boxes in a row then returns a list which has form desired position of boxes.
def boxProblem(boxCount):
	boxList = list();
	for x in range(boxCount // 2):
		boxList.append('b')
	for y in range(boxCount // 2):
		boxList.append('w')

	print("Input size of boxes: ", boxCount)
	print("Before swapping boxes: ", boxList)
	swapCount = 0;
	pivot_1 = 1
	pivot_2 = boxCount // 2
	for i in range(boxCount // 2, len(boxList)):
		swapCount += 1
		swapBoxes(boxList, pivot_1, pivot_2)
		pivot_1 += 2
		pivot_2 += 1
		print(boxList)
	print("After swapping boxes: ",boxList)
	print("Number of swaps: ", swapCount)


#Helper function for fake coin problem.
def getWeight(list,startPos, endPos):
	sum = 0
	for x in range(startPos, endPos):
		a = list[x]
		sum += a
	return sum	

#Assume that standart coin is 5 gr and fake one is 3 gr.
def fakeCoin(coinNumber):
	STANDART_COUNT = 5
	FAKE_COIN = 3

	#First create whole list with n standart coins.

	coinList = list();
	for x in range(coinNumber):
		coinList.append(STANDART_COUNT)

	#Then place the fake coin in random location.
	randomIndex = random.randrange(coinNumber)
	coinList[randomIndex] = FAKE_COIN

	print("Coin list is created as: ", coinList)


	while(len(coinList) > 1):
		startPoint1 = 0
		startPoint2 = math.ceil(coinNumber / 3)
		startPoint3 = math.ceil(2 * coinNumber / 3)
		#Split list into 3 sublist.
		coinList1 = coinList[startPoint1 : startPoint2]
		coinList2 = coinList[startPoint2 : startPoint3]
		coinList3 = coinList[startPoint3 : len(coinList)]
		#Split evenly if the mod 3 is 0.
		if coinNumber % 3 == 0:
			firstTuple = getWeight(coinList1, 0, math.ceil(coinNumber / 3))
			secondTuple = getWeight(coinList2, 0, math.ceil(coinNumber / 3))
			thirdTuple = getWeight(coinList3, 0, math.ceil(coinNumber / 3))	
			minTuple = min(firstTuple, secondTuple, thirdTuple)
			if(minTuple == firstTuple):
				coinList = coinList1
			elif(minTuple == secondTuple):
				coinList = coinList2
			elif(minTuple == thirdTuple):
				coinList = coinList3
		#Split n/3 n/3 n/3 + 1 if mod 3 is 1.
		elif coinNumber % 3 == 1:
			firstTuple = getWeight(coinList1, 0, math.ceil(coinNumber / 3))
			secondTuple = getWeight(coinList2, 0, math.ceil(coinNumber / 3) - 1)
			thirdTuple = getWeight(coinList3, 0, math.ceil(coinNumber / 3) - 1)	
			if secondTuple == thirdTuple:
				coinList = coinList1
			elif secondTuple < thirdTuple:
				coinList = coinList2
			elif secondTuple > thirdTuple:
				coinList = coinList3
		#Split n/3 n/3 + 1 n/3 + 1 if mod 3 is 2.
		elif coinNumber % 3 == 2:
			firstTuple = getWeight(coinList1, 0, math.ceil(coinNumber / 3))
			secondTuple = getWeight(coinList2, 0, math.ceil(coinNumber / 3))
			thirdTuple = getWeight(coinList3, 0, math.ceil(coinNumber / 3) - 1)
			if firstTuple == secondTuple:
				coinList = coinList3
			elif firstTuple < secondTuple:
				coinList = coinList1
			elif firstTuple > secondTuple:
				coinList = coinList2

		coinNumber = len(coinList)
		print("Sublist1: ",coinList1)
		print("Sublist2: ",coinList2)
		print("Sublist3: ",coinList3)
#####################################################################################################
def partition(l, low, high):
	counter = 0
	mid = (high + low) // 2
	pivot = high
	if l[low] < l[high]:
		pivot = low
	elif l[low] < l[mid]:
		if l[mid] < l[high]:
			pivot = mid


	index = pivot
	currentElement = l[index]
	l[index], l[low] = l[low], l[index]
	limit = low


	for x in range(low, high + 1):
		counter+=1;
		if l[x] < currentElement:
			limit += 1
			l[x], l[limit] = l[limit], l[x]
	l[low], l[limit] = l[limit], l[low]

	return limit,counter


def quickSort(l, low, high):
	counter = 0
	if low < high:
		limit, counter = partition(l, low, high)
		counter += quickSort(l, low, limit - 1)
		counter += quickSort(l, limit + 1, high)
	return counter



def insertionSort(l):
	counter = 0
	listLength = len(l)
	for x in range(1, listLength):
		pivot = l[x]
		pos = x

		while l[pos - 1] > pivot and pos > 0:
			counter += 1
			l[pos] = l[pos - 1]
			pos = pos - 1
		l[pos] = pivot
	return counter

def decreaseMedian(l):
	listLength = len(l)
	for x in range(1, listLength):
		pivot = l[x]
		pos = x

		while l[pos - 1] > pivot and pos > 0:
			l[pos] = l[pos - 1]
			pos = pos - 1
		l[pos] = pivot

	return l[listLength // 2]

#Source:
#https://stackoverflow.com/questions/26332412/python-recursive-function-to-display-all-subsets-of-given-set
#I copied that recursive code block in order to find all subsets of a list. I will be explaining it's complexity
#in my report
def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]
def exhaustiveSearch(n):
	exList = []
	for x in range(n):
		exList.append(random.randrange(n))

	minVal = min(exList)
	maxVal = max(exList)
	limit = (minVal + maxVal) * (n // 4)
	allSubsets = subs(exList)
	lenAllSubsets = len(allSubsets)
	specifiedSub = []
	minx = 99999
	for x in range(lenAllSubsets):
		sum = 0
		y = 0
		for y in range(len(allSubsets[x])):
			if sum < limit:
				specifiedSub.append(allSubsets[x])

	
	for x in range(len(specifiedSub)):
		sum = 1
		
		for y in range(len(specifiedSub[x])):
			sum = sum * specifiedSub[x][y]
			if(sum < minx):
				sum = minx
				index = x
	print("The optimal sub-array is", specifiedSub[x])
	



def testBoxes():
	print("BOX TEST START")
	boxProblem(8)
	print("BOX TEST END")
	print("BOX TEST START")
	boxProblem(4)
	print("BOX TEST END")
	print("BOX TEST START")
	boxProblem(6)
	print("BOX TEST END")

def fakeCoinTest():
	print("COIN TEST START")
	fakeCoin(8)
	print("COIN TEST END")
	print("COIN TEST START")
	fakeCoin(23)
	print("COIN TEST END")
	print("COIN TEST START")
	fakeCoin(234)
	print("COIN TEST END")	

def testSorts():
	myList1 = [9,8,7,6,5,4,3,2,1,0]
	myList2 = [9,8,7,6,5,4,3,2,1,0]
	quickCount = quickSort(myList1,0,9)
	insertCount = insertionSort(myList2)
	print(myList1 , "quickCount: " , quickCount)
	print(myList2 , "insertionCount: " , insertCount)

def medianTest():
	myList1 = [1,2,0,6,32,45,123]
	result = decreaseMedian(myList1)
	print("Median is ", result)

def testExhaustive():
	exhaustiveSearch[4]
print("#########################")
print("#########################")
print("#########################")
testBoxes()
print("#########################")
print("#########################")
print("#########################")
fakeCoinTest()
print("#########################")
print("#########################")
print("#########################")
testSorts()
print("#########################")
print("#########################")
print("#########################")
medianTest()
print("#########################")
print("#########################")
print("#########################")


exhaustiveSearch(4)


