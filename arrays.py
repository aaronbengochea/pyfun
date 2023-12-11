class Array:

    def __init__(self,size):
        self.arr = ['*'] * size
        self.size = size

    def insert(self, value, position):
        newSize = self.size + 1
        tempArray = self.arr

        for i in range(self.arr):
            if(i < position):
                tempArray[i] = self.arr[i]

#  217 - Contains Duplicates
def containsDuplicates(nums) -> bool:
    numSet = set()
    for num in nums:
        if num in numSet:
            return True
        else:
            numSet.add(num)
    return False

# 242 - Valid Anagram
def isAnagram(stringOne, stringTwo) -> bool:
    if len(stringOne) != len(stringTwo):
        return False

    balDict = {}

    for char in stringOne:
        if char in balDict:
            balDict[char] += 1
        else:
            balDict[char] = 1
    
    for char in stringTwo:
        if char in balDict:
            balDict[char] -= 1
        else:
            return False
        
    isAnagram = False
    for freq in balDict.values():
        if freq != 0:
            return False
        
    return True

def twoSum(nums, target):
    if len(nums) == 2:
        return [0,1]
    
    balDict = {}
    i = 0

    for i, num in enumerate(nums):
        difference = target - num

        if difference in balDict and balDict[difference] != i:
            return [balDict[difference], i]
        
        balDict[num] = i

    return 
    
def groupAnagrams(strs):
    print(strs)







if __name__ == "__main__":
    arr1 = [3,3]
    print("Duplicates: ", containsDuplicates(arr1), end='\n')

    s1 = "caer1g5"
    s2 = "race1g5"
    print("IsAnagram: ", isAnagram(s1,s2), end='\n')

    target = 6
    print("TwoSum: ", twoSum(arr1, target))

