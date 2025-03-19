//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
    
    
  private :
  
  void topo(int node,vector<vector<int>>& adj,int arr[],stack<int> &stck){
      arr[node]  = 1;
      cout<<node<< "in topo a"<<endl;
      for (auto nod :adj[node]){
        cout<<nod<< "in topo b"<<endl;
          if (!arr[nod]){
              topo(nod, adj , arr, stck);
          }
      }stck.push(node);
      cout<<node<< "in topo c"<<endl;
  }
  

  
  public:
    // Function to return list containing vertices in Topological order.
    vector<int> topologicalSort(vector<vector<int>>& adj) {
        int v = adj.size();
        int arr[v] = {0} ;
        stack<int> stck;
        for (int i = 0 ; i<v ; i++){
            if (!arr[i]){
                topo(i , adj , arr, stck);
            }
        }
        vector<int> ans;
        while (!stck.empty()){
        ans.push_back(stck.top());
        stck.pop();
        }
        return ans; 
        // Your code here
    }
};


int main(){

Solution sol;
vector<vector<int>> adj ;
vector<int> ans;
adj = {{}, {3}, {3}, {}, {0,1}, {0,2}};
ans = sol.topologicalSort(adj);

for(auto i : ans) cout << i;

return 0 ;
}