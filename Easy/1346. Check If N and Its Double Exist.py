class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mySet = set()
        for n in arr:
            if n in mySet:
                return True
            else:
                mySet.add(n / 2)
                mySet.add(n * 2)

        return False
