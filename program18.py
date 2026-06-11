"""
Write a python program to print the fibonacci sequence .

Fibonacci Sequence :

The FIbonacci sequence is a series of the numbers where each number is the sum of the two 
preceding ones, Typically starting with 0 and 1 . So The Sequence Begins with 0 and 1 and The 
Next Number is Obtained by adding the Previous Two Numbers . THis Pattern COntinues idenfinitely,
generating a sequence that looks likes this :

0,1,1,2,3,5,8,13,21,34,55,89,144 and so on

Mathematically, the Fibonacci Sequence can be defined using the following recurrence relation :

F(0)=0F(1)=1F(n)=F(n-1)+F(n-2)f or n>1

"""
class Solution(object):
    def threeSum(self, nums):
        
        if len(nums) < 3:  # lenth of the number
            return []       # return to the number 
        nums.sort()        # this is a nums.sort() 
        res = set()         # revers to the set a values set()
        for i, v in enumerate(nums[:-2]):  # for loop in i 
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
        