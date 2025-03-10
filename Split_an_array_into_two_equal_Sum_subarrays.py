class Solution:
    def canSplit(self, arr):
        #code her
        n = len(arr)
        start = 0
        end = n-1
        s1 = arr[start]
        s2 = arr[end]
        while start < end:
            if s1 == s2 :
                if end -start > 1:
                    start += 1
                    end -= 1
                else:
                    return True 
                          
                s1 += arr[start]
                s2 += arr[end]
            elif s1 < s2:
                start += 1
                s1 += arr[start]
            else:
                end -= 1
                s2 += arr[end]
        if s1 == s2 and start != end:
            return True
        else:
            return False

            
a = Solution()
arr = [3, 1, 1, 2]
print(a.canSplit(arr))
print(a.canSplit([1, 2, 3, 4, 5, 5]))