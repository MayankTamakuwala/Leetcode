class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        track = (['a', a], ['b', b], ['c', c])

        res = ""
        while True:
            if "aaa" in res and "bbb" in res and "ccc" in res:
                break
            first, second, third = sorted(track, key=lambda x: x[1], reverse = True)

            if (res[-2:] == first[0] * 2 and second[1] <= 0 and third[1] <= 0) or (first[1] <= 0):
                break

            if res[-2:] == first[0] * 2:
                if second[1] > 0:
                    res += second[0]
                    second = [second[0], second[1] - 1]
            else:
                res += first[0]
                first = [first[0], first[1] - 1]

            track = (first, second, third)

        return res
