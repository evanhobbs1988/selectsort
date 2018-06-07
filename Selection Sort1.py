import random
import datetime

t_start = datetime.datetime.now()

def selectionSort(arr): 
	for i in range(0, len(arr)/2): 
		minPos = i
		maxPos = i
		counter = 0
		for j in range(i + 1, len(arr) - counter): 
			print "j", arr[j]
			if arr[j] < arr[minPos]: 
				minPos = j

			if arr[j] > arr[maxPos]: 
				maxPos = j

		counter += 1

		print "Min", arr[minPos], "Max", arr[maxPos]

arr = [44, 3, 1, 2, 55, 11, 64, 34]
selectionSort(arr)
print(arr)

t_end = datetime.datetime.now()
runtime = t_end - t_start
print runtime