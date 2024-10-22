class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            track[tuple(chars)].append(s)
        
        return list(track.values())
