// Last updated: 06/04/2026, 16:33:23
1class Solution {
2public:
3    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
4
5        int direction = 0;
6        int x = 0;
7        int y = 0;
8
9        // Directions: North, East, South, West
10        vector<pair<int,int>> cal(4);
11        cal[0] = {0,1};
12        cal[1] = {1,0};
13        cal[2] = {0,-1};
14        cal[3] = {-1,0};
15
16        // Right turn
17        vector<int> dr = {1,2,3,0};
18
19        // Left turn
20        vector<int> dl = {3,0,1,2};
21
22        int maxdis = 0;
23
24        // Store obstacles in set
25        set<pair<int,int>> obs;
26        for (auto &o : obstacles) {
27            obs.insert({o[0], o[1]});
28        }
29
30        for (int cmd : commands) {
31
32            if (cmd > 0) {
33
34                auto [u,v] = cal[direction];
35
36                while (cmd > 0) {
37
38                    if (obs.find({x+u, y+v}) == obs.end()) {
39
40                        x += u;
41                        y += v;
42
43                        maxdis = max(maxdis, x*x + y*y);
44
45                    } else {
46                        break;
47                    }
48
49                    cmd--;
50                }
51
52            } 
53            else if (cmd == -1) {
54                direction = dr[direction];
55            } 
56            else if (cmd == -2) {
57                direction = dl[direction];
58            }
59        }
60
61        return maxdis;
62    }
63};