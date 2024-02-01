#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

const int N = 8;


bool isSafe(const vector<int>& board, int row, int col) {
    for (int i = 0; i < row; ++i)
        if (board[i] == col || abs(board[i] - col) == abs(i - row))
            return false;

    return true;
}


void solveQueensDLS(vector<vector<int>>& solutions, vector<int>& board, int row, int depthLimit) {
    if (row == N) {
        solutions.push_back(board);
        return;
    }

    for (int col = 0; col < N; ++col) {
        if (isSafe(board, row, col)) {
            board[row] = col;
            if (row + 1 < depthLimit) { 
                solveQueensDLS(solutions, board, row + 1, depthLimit);
            }
            else {
                
                solutions.push_back(board);
            }
        }
    }
}


void printChessboard(const vector<int>& board, int solutionNumber) {
    cout << "Solution #" << solutionNumber << ":\n";
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (board[i] == j)
                cout << "1 ";
            else
                cout << "0 ";
        }
        cout << "\n";
    }
    cout << "\n";
}

int main() {
    vector<vector<int>> solutions;
    vector<int> board(N, 0);  // Initialize the chessboard with all queens in the first column

    int depthLimit = 8;  // Depth limit for DLS

    auto start = high_resolution_clock::now();  // Start the timer

    solveQueensDLS(solutions, board, 0, depthLimit);

    auto stop = high_resolution_clock::now();  // Stop the timer

    // Print all the solutions
    for (int i = 0; i < solutions.size(); ++i) {
        printChessboard(solutions[i], i + 1);
    }

    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Total number of solutions: " << solutions.size() << "\n";
    cout << "Execution time: " << duration.count() << " microseconds\n";

    return 0;
}
