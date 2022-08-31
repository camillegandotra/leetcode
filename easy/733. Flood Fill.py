class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        startingcolor = image[sr][sc]       # get the starting color of our starting coordinates
        if startingcolor == color:          # if the startingcolor is the same as color, we return image because theres nothing to do
            return image
        
        def Fill(r, c, color, staringcolor):            # Fill function which we will call recursively
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != staringcolor:      
                #check if r,c is outside image dimensions, if it is return nothing cause we cant do anything with that
                #check is the color at r,c;if it is not equal to the startingcolor, return nothing cause no need to do anything with it
                return
            
            image[r][c] = color                 #change the color of r,c to color
        
            Fill(r-1,c, color, staringcolor)    # call recursive to pixels connected 4-directionally to r,c
            Fill(r+1,c, color, staringcolor)
            Fill(r,c-1, color, staringcolor)
            Fill(r,c+1, color, staringcolor)
            
        
        Fill(sr,sc, color, startingcolor)       # we start our recursive calling by calling Fill with our starting coordinates
            
        return image                            #return altered image