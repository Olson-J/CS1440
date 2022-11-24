import random


class RandNumberSet():  	         	  
    MIN_SIZE = 3  	         	  
    MAX_SIZE = 16

    def __init__(self, nSize, nMax):
        """  	         	  
        Create a RandNumberSet  	         	  

        'nSize': a parameter restricted to be in the range [3..16]  	         	  
        'nMax': a parameter restricted to be no less than `nSize*nSize`  	         	  

        Numbers are kept in separate segments so that the numbers within  	         	  
        columns on the resulting Bingo! card increase from left to right.  	         	  

        Within a column numbers are unordered.  	         	  

        A newly initialized RandNumberSet may present its numbers in  	         	  
        order.  Use .shuffle() to mix it up.  	         	  
        """  	         	  
        # sanity check on __m_nSize  	         	  
        self.__m_nSize = int(nSize)
        if int(self.__m_nSize) < RandNumberSet.MIN_SIZE:
            self.__m_nSize = RandNumberSet.MIN_SIZE  	         	  

        if int(self.__m_nSize) > RandNumberSet.MAX_SIZE:
            self.__m_nSize = RandNumberSet.MAX_SIZE  	         	  

        # sanity check on __m_nMax: pick the larger of `nMax` or `nSize^2 * 2`  	         	  
        self.__m_nMax = max(int(nMax), self.__m_nSize * self.__m_nSize * 2)
        self.__m_nRowPos = 0  	         	  

        segments = []  	         	  
        segment_size = int(nMax) // self.__m_nSize  # n.b. `//` operator means "integer division"
        remainder = int(nMax) % self.__m_nSize
        low = 1  	         	  
        for segment in range(1, self.__m_nSize + 1):
            high = low + segment_size  	         	  
            # When `len(RandNumberSet)` is not evenly divisible by `nSize`,  	         	  
            # there will be some numbers left over.  Distribute these extra  	         	  
            # numbers starting from segment #0, going up from there  	         	  
            if segment <= remainder:
                high += 1

            segments.append(list(range(low, high)))
            low = high
        self.segments = segments

    def segment(self):
        return self.segments

    def __len__(self):  	         	  
        """  	         	  
        This dunder makes `len()` work on RandNumberSets  	         	  

        The length of a RandNumberSet is equal to the number of segments  	         	  
        it contains; in other words, len(RandNumberSet) == card size.  	         	  
        """  	         	  
        return self.__m_nSize

    def __getitem__(self, n):  	         	  
        """Return the specified row of Bingo numbers, raise IndexError when out-of-bounds"""  	         	  
        if 0 <= n < self.__m_nSize:  	         	  
            row = []  	         	  
            for seg in self.segments:  	         	  
                row.append(seg[n])  	         	  
            return row  	         	  
        else:  	         	  
            raise IndexError  	         	  

    def shuffle(self):  	         	  
        """  	         	  
        Shuffle each segment and reset the current row position so that  	         	  
        next_row() will start from the top again.  	         	  
        """  	         	  
        for seg in self.segments:  	         	  
            random.shuffle(seg)  	         	  
        self.__m_nRowPos = 0

    def next_row(self):  	         	  
        """  	         	  
        Return the next row of Bingo numbers, or None if the RandNumberSet  	         	  
        is exhausted.  	         	  

        This method automatically keeps track of which row is up next  	         	  
        """  	         	  
        if self.__m_nRowPos >= self.__m_nSize:  	         	  
            return None  	         	  
        row = []
        for seg in self.segments:
            row.append(seg[self.__m_nRowPos])
        self.__m_nRowPos += 1
        return row

    def __str__(self):  	         	  
        strs = []  	         	  
        for seg in self.segments:  	         	  
            strs.append(str(seg))  	         	  
        return '\n'.join(strs)  	         	  
