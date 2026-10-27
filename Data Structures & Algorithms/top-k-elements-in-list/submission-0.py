class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        most_freq =[]

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for i in range(k):
            val = max(freq, key = freq.get)
            most_freq.append(val)
            del freq[val]
        
        return most_freq