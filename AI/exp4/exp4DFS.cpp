#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

const int N = 8;
int solutionCount = 0;

bool isSafe(vector<vector<int>>& board, int row, int col) {
    for (int i = 0; i < col; ++i)
        if (board[row][i] == 1)
            return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 1)
            return false;

    for (int i = row, j = col; i < N && j >= 0; i++, j--)
        if (board[i][j] == 1)
            return false;

    return true;
}

void printSolution(const vector<vector<int>>& board) {
    cout << "Solution #" << ++solutionCount << ":\n";
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << board[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

bool solveNQueensUtil(vector<vector<int>>& board, int col) {
    if (col == N) {
        printSolution(board);
        return true; 
    }

    bool res = false;
    for (int i = 0; i < N; ++i) {
        if (isSafe(board, i, col)) {
            board[i][col] = 1;  

            res = solveNQueensUtil(board, col + 1) || res;

            board[i][col] = 0; 
        }
    }

    return res;
}

void solveNQueens() {
    vector<vector<int>> board(N, vector<int>(N, 0));

    auto start = high_resolution_clock::now();

    if (!solveNQueensUtil(board, 0)) {
        cout << "No solutions exist.\n";
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Total runtime: " << duration.count() << " microseconds\n";
}

int main() {
    solveNQueens();

    return 0;
}
