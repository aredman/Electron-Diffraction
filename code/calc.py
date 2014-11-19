import math
import csvHandle

#find the mean of a given list
def mean(inList):
	return math.fsum(inList)/len(inList)

#expand a list into its component pieces
def expand(inList):
	inList = csvHandle.transp(inList)
	retList = []
	for row in inList:
		for n in xrange(int(row[1])):
			retList.append(row[0])
	return retList

#find the maximum of a given list
def maximum(indep, dep):
	index = indep[0]
	value = dep[0]
	for row in csvHandle.transp([indep, dep]):
		if row[1] > value:
			value = row[1]
			index = row[0]
	return [value, index]

#generate a column of data that is the moving average of the input
def mvavg(inList, size):
	top = len(inList) - 1
	size /= 2
	outList = []
	for i in xrange(len(inList)):
		if i - size < 0:    outList.append(mean(inList[0:i+size]))
		elif i + size >= top: outList.append(mean(inList[i-size:top]))
		else:               outList.append(mean(inList[i-size:i+size]))
	return outList

#find the standard deviation, return a list of [stdDev, N]
def deviation(indep, count, index):
	variance = 0
	sumCount = 0
	for row in csvHandle.transp([indep, count]):
		sumCount += row[1]
		variance += (row[0] - index)**2 * row[1]
	variance /= sumCount
	return [math.sqrt(variance), sumCount]

#return stdDev / sqrt(N)
def uncert(indep,count,index):
	[stdDev,count] = deviation(indep,count,index)
	return stdDev / math.sqrt(count)
