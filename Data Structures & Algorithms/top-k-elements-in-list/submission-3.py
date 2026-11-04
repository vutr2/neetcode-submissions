class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            buckets[c].append(num)
        
        results = []
        for c in range(len(buckets) - 1, 0, -1):
            for num in buckets[c]:
                results.append(num)
                if len(results) == k:
                    return results