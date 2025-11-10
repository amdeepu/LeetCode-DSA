from typing import List
class Solution:
    def twoSum(self, list1: List[int], target: int) -> List[int]:
        dict  = {}	#{2: 0},{7:1},{11:2},{15:3}
        for i, num in enumerate(list1): #i=0,num=2, i=1,num=7, i=2,num=11, i=3,num=15

            check = target - num #check=9-2=7,check=9-7=2, 9-11=-2, 9-15=-6
            if check in dict:   #2 ,-2, -6
              print(dict[check], i)	#0 1
            dict[num]=i #7:1, 11:2, 15:3
            print(dict) #2:0,{2: 0, 7: 1},2: 0},{7:1},{11:2},{2: 0},{7:1},{11:2},{15:3}
s=Solution()
s.twoSum([2,7,11,14,12,5],17)
