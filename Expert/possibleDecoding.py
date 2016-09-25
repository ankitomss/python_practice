
def possibleDecode(num):
    count = [0 for i in range(len(num)+1)]
    count[0] = 1
    count[1] = 