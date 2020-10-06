import sys

newFileName = sys.argv[1]

with open(newFileName+".py", "a") as newFile:
    newFile.write('import unittest\n\n')
    newFile.write('def fn():\n\n')
    newFile.write('class TestFunc(unittest.TestCase):\n')
    newFile.write('\tdef test_fn(self):\n')
    newFile.write('\t\tself.assertEqual(fn(), "1")\n\n')
    newFile.write('unittest.main()')

print(newFileName, 'created')
