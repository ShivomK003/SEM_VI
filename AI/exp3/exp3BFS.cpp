#include <iostream>
#include <queue>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

const int N = 8;


struct Board {
    int queens[N]; 

    Board() {
        fill(begin(queens), end(queens), -1);
    }
};

bool isSafe(const Board& board, int row, int col) {
    for (int i = 0; i < col; ++i) {
        if (board.queens[i] == row || abs(board.queens[i] - row) == abs(i - col)) {
            return false;
        }
    }
    return true;
}

void printBoard(const Board& board) {
    static int solutionNumber = 1;

    cout << "Solution #" << solutionNumber++ << ":\n";

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (board.queens[j] == i) {
                cout << "1 ";
            } else {
                cout << "0 ";
            }
        }
        cout << endl;
    }
    cout << endl;
}

void solveQueens() {
    queue<Board> q;
    Board initialBoard;
    q.push(initialBoard);

    auto start = high_resolution_clock::now();

    while (!q.empty()) {
        Board currentBoard = q.front();
        q.pop();

        int currentCol = 0;
        while (currentCol < N && currentBoard.queens[currentCol] != -1) {
            currentCol++;
        }

        if (currentCol == N) {
            printBoard(currentBoard);
        } else {
            for (int i = 0; i < N; ++i) {
                if (isSafe(currentBoard, i, currentCol)) {
                    Board newBoard = currentBoard;
                    newBoard.queens[currentCol] = i;
                    q.push(newBoard);
                }
            }
        }
    }

    auto stop = high_resolution_clock::now(); // Record the stop time
    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Total runtime: " << duration.count() << " microseconds" << endl;
}

int main() {
    solveQueens();

    return 0;
}
