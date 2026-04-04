// Last updated: 04/04/2026, 13:10:12
class Solution {
public:
    int minOperations(vector<int>& nums) {
        map<int,int> mp;
        
        int n = nums.size();
        
        int rem = 0;
        bool flag = true;
        for ( int i =n -1;i>=0;i--){
            if(++mp[nums[i]] >1){
                rem  =i;
                flag = false;
                break;
            }
        
        }
        if ( rem == 0  && flag ) return 0;
        return (rem+3)/3;
    }
        
};