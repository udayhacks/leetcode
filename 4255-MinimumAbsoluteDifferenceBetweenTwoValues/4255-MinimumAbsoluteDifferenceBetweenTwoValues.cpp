// Last updated: 04/04/2026, 13:10:09
class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums) {
     int ans = INT_MAX;
        int n = nums.size();
        for ( int i = 0 ;i<n;i++){
            for ( int j = 0 ;j<n;j++){
                if (( nums[i] == 1 && nums[j] == 2)||( nums[i] ==2 && nums[j] ==1)){
                    ans = min(abs(i-j),ans);
                }
            }
        }
        if ( ans == INT_MAX) return -1;
        else return ans;
        
        
    }
};