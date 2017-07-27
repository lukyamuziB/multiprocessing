import multiprocessing


def factorial(a):
	if a is 1:
		return 1
	return a * factorial(a-1)

def factorial_list(b,queue):
	for number in b:
		queue.put(factorial(number))
	print("inside", queue.get())
# 
if __name__ == '__main__':
	num = [x for x in range(1,10,2)]
	queue = multiprocessing.Queue()
	process = multiprocessing.Process(target=factorial_list, args=(num,queue))

	process.start()
	process.join()

	while queue.empty() is False:
		print("Outside",queue.get())
