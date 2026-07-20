class Solution(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        sol = [[0] * c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                sol[idx // c][idx % c] = mat[i][j]
        return sol