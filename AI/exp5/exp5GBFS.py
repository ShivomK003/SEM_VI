import heapq
import timeit

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = 0 if parent is None else parent.depth + 1
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        total_distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i * 3 + j]
                if value != 0:
                    goal_row, goal_col = (value - 1) // 3, (value - 1) % 3
                    total_distance += abs(i - goal_row) + abs(j - goal_col)
        return total_distance

    def generate_neighbors(self):
        neighbors = []
        empty_index = self.board.index(0)
        empty_row, empty_col = empty_index // 3, empty_index % 3

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in moves:
            new_row, new_col = empty_row + dr, empty_col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = list(self.board)
                new_board[empty_index], new_board[new_row * 3 + new_col] = new_board[new_row * 3 + new_col], new_board[empty_index]
                neighbors.append(PuzzleState(new_board, parent=self, move=(dr, dc)))

        return neighbors

def reconstruct_path(state):
    path = []
    while state is not None:
        path.append(state.move)
        state = state.parent
    return path[::-1]

def greedy_best_first_search(initial_state):
    open_set = [initial_state]
    closed_set = set()
    
    start_time = timeit.default_timer()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            print("Solution found:")
            print("Current State:")
            print("Board:", current_state.board)
            print("g(n):", current_state.depth)
            print("h(n):", current_state.heuristic)
            print("f(n):", current_state.depth + current_state.heuristic)
            print("====================")
            end_time = timeit.default_timer()
            elapsed_time = end_time - start_time
            print("Goal reached in {:.6f} microseconds.".format(elapsed_time))
            return reconstruct_path(current_state)

        closed_set.add(current_state)

        for neighbor in current_state.generate_neighbors():
            if neighbor not in closed_set and neighbor not in open_set:
                heapq.heappush(open_set, neighbor)

        print("Current State:")
        print("Board:", current_state.board)
        print("g(n):", current_state.depth)
        print("h(n):", current_state.heuristic)
        print("f(n):", current_state.depth + current_state.heuristic)
        print("====================")

    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time
    print("No solution found in {:.6f} microseconds.".format(elapsed_time))
    return None

if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 0, 5, 7, 8, 6]  # Different from the goal state
    initial_state = PuzzleState(initial_board)

    solution = greedy_best_first_search(initial_state)

    if not solution:
        print("No solution found.")
