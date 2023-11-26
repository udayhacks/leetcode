class Solution:
    def nextGreatestLetter(self, letters, target):
        l = 0 
        h= len(letters)-1
        while l <= h :
            m = (l+h)//2
            if letters[m] <=target :
                l= m+1
            else:
                h = m-1
        return letters[l] if  l< len(letters)  else  letters[0]

            
           
           
           
           
           
a = Solution()
letters = ["c","f","j"]
target = "z"
a.nextGreatestLetter(letters,target)



