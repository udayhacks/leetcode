class Solution:
    def merge(self, nums1, m, nums2, n) :
        i = k = 0 
        z = m
        if m== 0 :
            nums1[:] = nums2[:]
        while i  < m+n and k < n and z < m+n:
            

            if i == z :
                nums1[i] = nums2[k]
                k+=1
                z+=1
            
            elif nums1[i]>nums2[k] :
                nums1[z] = nums2[k]
                nums1[z],nums1[i] = nums1[i],nums1[z]
                k+=1
                z+=1
            i+=1


nums1 =[1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1
a = Solution()
a.merge( nums1, m, nums2, n) 