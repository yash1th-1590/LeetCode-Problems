class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [None] * (4 * n)
        def merge(a, b):
            ca, pa = a
            cb, pb = b
            c = [0] * k
            for i in range(k):
                c[(pa * i) % k] += cb[i]
            for i in range(k):
                c[i] += ca[i]
            return c, (pa * pb) % k
        def build(node, l, r):
            if l == r:
                c = [0] * k
                c[nums[l] % k] = 1
                tree[node] = (c, nums[l] % k)
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        def update(node, l, r, idx, val):
            if l == r:
                c = [0] * k
                c[val % k] = 1
                tree[node] = (c, val % k)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)
            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)
            return merge(left, right)
        build(1, 0, n - 1)
        result = []
        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            counts, _ = query(1, 0, n - 1, start, n - 1)
            result.append(counts[x])
        return result
        