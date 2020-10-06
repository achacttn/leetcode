import unittest

def fn(s):
	if not s:
		return 0
	sLen = len(s)
	maxLen = 0
	for i in range(sLen):
		if s[sLen-1-i] == " ":
			if sLen-i <= sLen-1 and s[sLen-i] != " ":
				return maxLen
		else:
			maxLen += 1
	return maxLen

class TestFunc(unittest.TestCase):
	def test_fn1(self):
		self.assertEqual(fn("Hello World"), 5)

	def test_fn2(self):
		self.assertEqual(fn(" "), 0)
	
	def test_fn3(self):
		self.assertEqual(fn(""), 0)
	
	def test_fn4(self):
		self.assertEqual(fn("Hello World   "), 5)

unittest.main()