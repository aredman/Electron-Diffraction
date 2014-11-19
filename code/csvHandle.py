import csv

#transpose a table from list of rows to list of columns
def transp(table): return map(list, map(None, *table))

#convert a list to floats; used for type safety
def convert(inList, func = float):
	retList = []
	for i in inList:
		try:
			retList.append(func(i))
		except:
			pass
	return retList

def getColumns(filename):
	with open(filename) as csvfile:
		table = transp(csv.reader(csvfile, delimiter=';'))
	return [convert(col,float) for col in table]
