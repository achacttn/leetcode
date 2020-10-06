import unittest

# def fn(nums):
# 	totalMax = 0
# 	for i in range(len(nums)):
# 		loopMax = 0
# 		loopSum = 0
# 		for j in nums[i:]:
# 			loopSum += j
# 			loopMax = max(loopSum, loopMax)
# 		totalMax = max(loopMax, totalMax)
# 	return totalMax

def fn(nums):
	print('=====')
	print(nums)
	print('=====')
	curMax, totalMax = nums[0], nums[0]
	for i in range(1, len(nums)):
		curMax = max(nums[i], curMax+nums[i])
		totalMax = max(totalMax, curMax)
		print('curMax, totalMax: ', curMax, totalMax)
	return totalMax


fn([-2,1,-3,4,-1,2,1,-5,4])


# class TestFunc(unittest.TestCase):
# 	def test_fn(self):
# 		self.assertEqual(fn([-2,1,-3,4,-1,2,1,-5,4]), 6)

# unittest.main()
