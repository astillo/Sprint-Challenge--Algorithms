'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def isth(piece, count =0):
    print(piece)

    #check to see if it is not possible
    if len(piece) < 2:
       return count
    #increase count
    elif piece[:2] == 'th':
        count+=1
    #create string wth one less char for next iteration
    return isth(piece[1:], count)


def count_th(word):
    
    return isth(word)
