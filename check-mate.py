def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    """
    # dictionary to store the value of the columns 
    columns = {
    	'A' : 1,
    	'B' : 2,
    	'C' : 3,
    	'D' : 4,
    	'E' : 5,
    	'F' : 6,
    	'G' : 7,
    	'H' : 8
    }

    if king[0] == queen[0] or king[1] == queen[1]:

    	return True

    elif int(king[1]) - int(queen[1]) == columns[king[0]] - columns[queen[0]]:

    	return True 

    return False




print(check("D6", "H6"))


print(check("E6", "E4"))


print(check("B7", "D5"))


print(check("A1", "H8"))


print(check("A8", "H1"))


print(check("D6", "H7"))


print(check("E6", "F4"))
