import heapq
import timeit

step_count = 0

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = 0 if parent is None else parent.cost + 1
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def calculate_heuristic(self):
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

def a_star_search(initial_state):
    global step_count
    open_set = [initial_state]
    closed_set = set()
    start_time = timeit.default_timer()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            print("Goal reached!")
            step_count += 1
            print(f"Current State {step_count}: ")
            print("Board:", current_state.board)
            print("g(n):", current_state.cost)
            print("h(n):", current_state.heuristic)
            print("f(n):", current_state.cost + current_state.heuristic)
            print("====================")
            end_time = timeit.default_timer()
            elapsed_time = end_time - start_time
            print("Goal reached in {:.6f} microseconds.".format(elapsed_time))
            return reconstruct_path(current_state)

        closed_set.add(current_state)

        for neighbor in current_state.generate_neighbors():
            if neighbor in closed_set:
                continue

            tentative_g = current_state.cost + 1
            if neighbor not in open_set or tentative_g < neighbor.cost:
                neighbor.cost = tentative_g
                neighbor.heuristic = neighbor.calculate_heuristic()
                heapq.heappush(open_set, neighbor)

        step_count += 1
        print(f"Current State {step_count}: ")
        print("Board:", current_state.board)
        print("g(n):", current_state.cost)
        print("h(n):", current_state.heuristic)
        print("f(n):", current_state.cost + current_state.heuristic)
        print("====================")

    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time
    print("No solution found in {:.6f} microseconds.".format(elapsed_time))
    return None

if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 0, 5, 7, 8, 6] 
    initial_state = PuzzleState(initial_board)

    solution = a_star_search(initial_state)

    if solution is None:
        print("No solution found.")