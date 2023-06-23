class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click[0], click[1]  # get coordinates of the click
        
        if not board:               # if not board, then obvi nada we can do
            return board
        
        if board[x][y] == 'M':          # if the click is on an unrevealed Mine 'M', we lose, so change it to a revealed Mine, 'X' and return the board
            board[x][y] = 'X'
            return board
        
        def rec(board, x, y):                   # recursive function, here at a given coordinate, first we check if the coord is within bounds, if nor return nothing
            if 0 <= x <= len(board) - 1 and 0 <= y <= len(board[x]) - 1:
                if board[x][y] == 'E':                             # we only care about the point if it is an unrevealed empty space 'E'
                    count = 0                                   # set a count for the adjacent spaces (counting how many mines there are nearby)

                    for p in range(x - 1, x + 2):               # go through the 8 spaces around it
                        for l in range( y - 1, y + 2):  
                            print(count)
                            if p == x and l == y:               # if it is the same base coord, we skip
                                continue
                            if 0 <= p <= len(board) - 1 and 0 <= l <= len(board[p]) - 1:    # check if the coord we looking at is within bounds
                                if board[p][l] == 'M':          # if that coord is an Unrevealed Mine 'M', count += 1
                                    count += 1
                       

                    if count == 0:                      # after checking the surrounding 8, if count still == 0, then we can to call rec() on the surrounding 8.
                        board[x][y] = 'B'           # first set the cur coord as a Revealed Blank Space 'B', then call rec()
                        for p in range(x - 1, x + 2):       # same range function as before to look at the 8 squares; skipping the cur one
                            for l in range( y - 1, y + 2):
                                if p == x and l == y:
                                    continue
                                rec(board, p, l)    # we dont have to check bounds here becayse it will when the function runs (line 18)
                    else:
                        board[x][y] = str(count)        # if count != 0, then we want to make the coord say the number of mines near it
                    
                       
            else:
                return              # this runs if the coord is out of bounds, then nada to do
            
        rec(board, x, y)        # call the recursive function with the click coordinates
        
        return board            # return board
            
        
        
        