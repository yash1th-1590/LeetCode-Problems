class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        freq = {}
        for num in barcodes:
            freq[num] = freq.get(num, 0) + 1
        items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        n = len(barcodes)
        ans = [0] * n
        id = 0
        for num, count in items:
            while count > 0:
                if id >= n:
                    id = 1
                ans[id] = num
                id += 2
                count -= 1
        return ans
        