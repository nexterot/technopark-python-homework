import time
import json

# 1
def log_duration(func):
	def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print("*** function '{}' ran in {} seconds ***".format(func.__name__, time.time() - start_time))
        return res
    return inner

# 2        
def to_json(func):
	def inner(*args, **kwargs):
		result = func(*args, **kwargs)
		if isinstance(res, dict):
			result = json.dumps(result, indent=4, sort_keys=True)
		return result
	return inner   
        
# 3
def ignore_exceptions(exception):
	def wrapper(func):
		def inner(*args, **kwargs):
			try:
				result = func(*args, **kwargs)
			except exception:
				result = None
			return result
		return inner
	return wrapper
        
# 4
class PascalArray:
	"""PascalArray(2, 5) -> Pascal-like array with indices\nfrom 2 to 5\n"""
	def __init__(self, start, end):
		self.start = start
		self.end = en
		self.container = [None] * (end-start+1)
		
	def __getitem__(self, index):
		if self.start <= index <= self.end:
			return self.container[index - self.start]
		raise IndexError("PascalArray index out of range")
		
	def __setitem__(self, index, value):
		if self.start <= index <= self.end:
			self.container[index - self.start] = value
			return
		raise IndexError("PascalArray assignment index out of range {}-{}, got {}".format(self.start, self.end, index))
        
        
def main():
	# test 1
	print(">>> Test 1")
	@log_duration
	def pow(x, y):
		return x ** y
	print('evaluating 3**5000000')
	x = pow(3, 5000000)
	
	
	# test 2
	print("\n>>> Test 2")
	@to_json
	def pow(x, y):
		return x ** y
	print(pow(2, 12))
	@to_json
	def sample_dict():
		return {"json" : "is", "awesome" : ("js" , 2017)}
	print(sample_dict())
	
	
	# test 3
	print("\n>>> Test 3")
	@ignore_exceptions(ZeroDivisionError)
	def div(x, y):
		return x // y
	print("div 100 by 3: {}".format(div(100, 0)))
	print("div 10 by 3: {}".format(div(10, 3)))


	# test 4
	print("\n>>> Test 4")
	print(PascalArray.__doc__)
	array = PascalArray(1, 100)
	print(array[100])
	array[100] = 99
	print(array[100])
	#print(array[0]) # Exception!
	
	
if __name__ == "__main__":
	main()
