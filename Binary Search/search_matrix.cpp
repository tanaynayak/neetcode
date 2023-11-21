class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n-1
        while l<=r:
            mid = l + (r-l)/2
            if matrix[mid/n][mid%n]==target:
                return True
            elif matrix[mid/n][mid%n]>target:
                r=mid-1
            else:
                l=mid+1
        return False
        