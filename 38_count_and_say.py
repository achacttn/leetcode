import unittest

# "1211221"

def countAndSay(n: int, d={1:"1"}) -> str:
    if n in d:
        return d[n]
    else:
        valueToRead = countAndSay(n-1)
        output = ""
        curVal = valueToRead[0]
        curValCount = 1
        i = 1
        while i < len(valueToRead):
            if valueToRead[i] == curVal:
                curValCount += 1
                i += 1
            else:
                output += str(curValCount) + curVal
                curVal = valueToRead[i]
                curValCount = 0
        output += str(curValCount) + curVal

        d[n] = output
        return d[n]

class TestFunc(unittest.TestCase):
    def test_countAndSay1(self):
        self.assertEqual(countAndSay(1), "1")
    
    def test_countAndSay2(self):
        self.assertEqual(countAndSay(2), "11")

    def test_countAndSay3(self):
        self.assertEqual(countAndSay(3), "21")
    
    def test_countAndSay4(self):
        self.assertEqual(countAndSay(4), "1211")
    
    def test_countAndSay5(self):
        self.assertEqual(countAndSay(5), "111221")

    def test_countAndSay6(self):
        self.assertEqual(countAndSay(6), "312211")

unittest.main()
