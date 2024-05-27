from ai_pkg.planning import PlanningProblem, Action, goal_test
from ai_pkg.utils import expr

def double_tennis_problem():
    initial = 'At(A, LeftBaseLine) & At(B, RightNet) & Approaching(Ball, RightBaseLine) & Team(A, B) & Team(B, A)'
    goal = 'Returned(Ball) & At(a, RightNet) & At(a, LeftNet)'
    actions = [
        Action('Hit(player, Ball, loc)',
               precond='Approaching(Ball, loc) & At(player, loc)',
               effect='Returned(Ball)'),
        Action('Go(player, to, loc)',
               precond='At(player, loc)',
               effect='At(player, to) & ~At(player, loc)')
    ]
    return PlanningProblem(init=initial, goals=goal, actions=actions)

if __name__ == '__main__':
    p = double_tennis_problem()
    print("Initial state:", p.init)
    print("Goal state:", p.goals)
    print("Is goal satisfied initially?", goal_test(p.goals, p.init))

    solution = [
        expr("Go(A, RightBaseLine, LeftBaseLine)"),
        expr("Hit(A, Ball, RightBaseLine)"),
        expr("Go(A, LeftNet, RightBaseLine)")
    ]

    print("\nExecuting solution...")
    for action in solution:
        print("Action:", action)
        p.act(action)
        print("Current state:", p.init)

    print("\nIs goal satisfied finally?", goal_test(p.goals, p.init))