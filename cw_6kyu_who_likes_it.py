# my initial

def likes(names):
    outputStr = ""
    if len(names) == 0:
        outputStr += "no one likes this"
    if len(names) == 1:
        outputStr += names[0] + " likes this"
    if len(names) == 2:
        outputStr += names[0] + " and " + names[1] + " like this"
    if len(names) > 2:
        outputStr += '{0}, {1} and '.format(names[0], names[1])
        if len(names) == 3:
            outputStr += names[2] + " like this"
        else:
            outputStr += str(len(names)-2) + " others like this"
    print(outputStr)
    return outputStr

# top solution

def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)