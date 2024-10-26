class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy Approach
        # O(n) time and O(1) memory

        # First ensure and check if the solution exists
        # Solution exists if sum(gas) >= sum(cost)

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                start = i + 1
                total = 0
        return start
