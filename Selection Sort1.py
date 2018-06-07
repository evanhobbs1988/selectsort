# If you're given a list with a bunch of numbers and you're supposed to sort the numbers(with the smallest number on the left and the largest number on the right), how would you do this?
# There are numerous sorting algorithms to sort numbers in the list.
# We'll introduce one of the simplest sorting algorithm called selection sort.


def selection_sort(my_list):
 len_list = len(my_list)
 for i in range(len_list):
  min_index = i
  for j in range(i+1, len_list):
   if my_list[j] < my_list[min_index]:
                min_index = j
				if min_index != i:
				(my_list[i], my_list[min_index]) = (my_list[min_index], my_list[i])
				return my_list
	print selection_sort(x)
