// Last updated: 04/04/2026, 13:10:22
class Solution {
public:
    vector<int> decimalRepresentation(int n) {

        
        vector<int> ans;
        long long  e = 1;

        while(n>0){

            int rem = n%10;
            if (rem != 0) ans.push_back(rem*e);
            n= n/10;
            e *= 10;
        }
        reverse(ans.begin(),ans.end());
        return ans;
        
        
    }
};