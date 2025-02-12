from ai_pkg.search import *

start = 'Munchen'
goal = 'Frankfurt'
city_map = Graph(dict(
    # jalur 1
    Munchen=dict(Augsburg=84, Nurnberg=167, Kassel=502),
    Augsburg=dict(Karlsruhe=250),
    Karlsruhe=dict(Mannheim=80),
    Mannheim=dict(Frankfurt=85),
    # jalur 2
    Nurnberg=dict(Wurzburg=103, Stuttgart=183),
    Wurzburg=dict(Erfurt=186, Frankfurt=217),
    # jalur 3
    Kassel=dict(Frankfurt=173),

    ),directed=True)


class CityProblem(Problem):
    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        return action

    def path_cost(self, cost, A, action, B):
        return cost + (self.graph.get(A, B) or infinity)


def breadth_first_search(problem):
    global track_path
    frontier = deque([Node(problem.initial)])
    explored = set()
    track_path = [problem.initial]

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        expanded = node.expand(problem)
        for child in expanded:
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                track_path.append(child.state)
                frontier.append(child)
    return None


if __name__ == '__main__':
    track_path = []
    romania_problem = CityProblem(start, goal, city_map)
    node = breadth_first_search(romania_problem)
    if node is not None:
        final_path = node.solution()
        final_path.insert(0, start)
        print('TRACKING PATH: ', ' -> '.join(track_path))
        print('SOLUTION PATH: ', ' -> '.join(final_path))