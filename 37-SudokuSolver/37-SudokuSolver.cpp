// Last updated: 05/04/2026, 14:13:36
1class Solution {
2private:
3
4    bool isSafe(vector<vector<char>>& board, int row, int col, char dig) {
5        
6        // column check
7        for (int r = 0; r < 9; r++) {
8            if (board[r][col] == dig) return false;
9        }
10
11        // row check
12        for (int c = 0; c < 9; c++) {
13            if (board[row][c] == dig) return false;
14        }
15
16        // 3x3 box check
17        int sr = (row / 3) * 3;
18        int sc = (col / 3) * 3;
19
20        for (int r = sr; r < sr + 3; r++) {
21            for (int c = sc; c < sc + 3; c++) {
22                if (board[r][c] == dig) return false;
23            }
24        }
25
26        return true;
27    }
28
29    bool helper(vector<vector<char>>& board, int row, int col) {
30        
31        if (row == 9) return true;
32
33        int next_row = row;
34        int next_col = col + 1;
35
36        if (next_col == 9) {
37            next_row = row + 1;
38            next_col = 0;
39        }
40
41        if (board[row][col] != '.') {
42            return helper(board, next_row, next_col);
43        }
44
45        for (char dig = '1'; dig <= '9'; dig++) {
46            if (isSafe(board, row, col, dig)) {
47                board[row][col] = dig;
48
49                if (helper(board, next_row, next_col)) return true;
50
51                board[row][col] = '.';
52            }
53        }
54
55        return false;
56    }
57
58public:
59
60    void solveSudoku(vector<vector<char>>& board) {
61        helper(board, 0, 0);
62    }
63};