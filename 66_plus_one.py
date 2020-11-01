import unittest

def fn(digits):
	nineCount = 0
	for i in range(len(digits)):
		if digits[len(digits)-1-i] == 9:
			digits[len(digits)-1-i] = 0
			nineCount += 1
		else:
			break
	if len(digits) == nineCount:
		return [1] + digits
	else:
		digits[len(digits)-1-nineCount] += 1
		return digits

# print(fn([9,9,9]))

# fn([1,9,9])

# print(fn([2,5,9,3,9]))

class TestFunc(unittest.TestCase):
	def test_fn(self):
		self.assertEqual(fn([1,2,3]), [1,2,4])
	
	def test_fn2(self):
		self.assertEqual(fn([2,9]), [3,0])

	def test_fn3(self):
		self.assertEqual(fn([2,5,9,3,9]), [2,5,9,4,0])

	def test_fn4(self):
		self.assertEqual(fn([0]), [1])

unittest.main()
