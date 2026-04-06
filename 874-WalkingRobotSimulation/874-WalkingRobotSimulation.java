// Last updated: 06/04/2026, 16:50:40
1import java.util.*;
2
3class Solution {
4
5    public int robotSim(int[] commands, int[][] obstacles) {
6
7        int direction = 0;
8        int x = 0;
9        int y = 0;
10
11        // Directions: North, East, South, West
12        int[][] cal = new int[4][2];
13        cal[0] = new int[]{0, 1};
14        cal[1] = new int[]{1, 0};
15        cal[2] = new int[]{0, -1};
16        cal[3] = new int[]{-1, 0};
17
18        // Right turn
19        int[] dr = {1, 2, 3, 0};
20
21        // Left turn
22        int[] dl = {3, 0, 1, 2};
23
24        int maxdis = 0;
25
26        // Store obstacles in set
27        Set<String> obs = new HashSet<>();
28
29        for (int[] o : obstacles) {
30            obs.add(o[0] + "," + o[1]);
31        }
32
33        for (int cmd : commands) {
34
35            if (cmd > 0) {
36
37                int u = cal[direction][0];
38                int v = cal[direction][1];
39
40                while (cmd > 0) {
41
42                    if (!obs.contains((x + u) + "," + (y + v))) {
43
44                        x += u;
45                        y += v;
46
47                        maxdis = Math.max(maxdis, x * x + y * y);
48
49                    } else {
50                        break;
51                    }
52
53                    cmd--;
54                }
55
56            } 
57            else if (cmd == -1) {
58
59                direction = dr[direction];
60
61            } 
62            else if (cmd == -2) {
63
64                direction = dl[direction];
65
66            }
67        }
68
69        return maxdis;
70    }
71}