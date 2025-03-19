
    vector<int> topologicalSort(vector<vector<int>>& adj) {
        int V = adj.size();
        int indegree[V] = {0};
        for (auto i :adj){
            for (auto j :i){
                indegree[j]++;
                
            }
        }
        queue<int> que ;
        for (int i :indegree){
            if (i == 0 ) que.push(i);
        }
        vector<int> ans ;
        
        while (!que.empty()){
            int front = que.front();
            ans.push_back(front);
            que.pop();
            for (auto i : adj[front]){
                indegree[i]--;
                if (indegree[i]== 0 ) que.push(i);
            }
        }
        return ans;
        // Your code here
    }
