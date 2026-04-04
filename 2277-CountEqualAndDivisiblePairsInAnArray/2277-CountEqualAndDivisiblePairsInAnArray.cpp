// Last updated: 04/04/2026, 13:12:05
class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
       int count = 0 ;
       int n = nums.size();
       for (int i = 0 ;i<n;i++){
        for(int j = i+1;j<n;j++){
            if (nums[i]== nums[j] && (i*j)%k == 0) count++;
        }
       }
       return count ; 
    }
};