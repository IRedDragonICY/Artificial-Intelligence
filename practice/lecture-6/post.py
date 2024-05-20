from ai_pkg.planning import (HLA, Problem as PlanProblem)

library = {
    'HLA': ['Go(Home, Airport)',
            'Taxi(Home, Airport)'],
    'steps': [['Taxi(Home, Airport)'],
              []],
    'precond': [['At(Home)'],
                ['At(Home)']],
    'effect': [['At(Airport) & ~At(Home) & ~Have(Cash)'],
               ['At(Airport) & ~At(Home) & ~Have(Cash)']]
}

goto_airport = HLA('Go(Home, Airport)', precond='At(Home)', effect='At(Airport) & ~At(Home) & ~Have(Cash)')

problem = PlanProblem('At(Home) & Have(Cash) & Have(Car)', 'At(Airport) & ~At(Home) & ~Have(Cash)',
                      [goto_airport])

solution = PlanProblem.hierarchical_search(problem, library)

for i in range(len(solution)):
    print('precondition: ', solution[i].precond)
    print('action: ', solution[i].name, solution[i].args)
    print('effect : ', solution[i].effect)