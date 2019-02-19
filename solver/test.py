from solver.clause import Clause
from solver.knowledge_base import KnowledgeBase
from solver.solver import Solver


def test_solver_tautology():
    clauses = {1: Clause(1, [1, 2, 3, -1])}
    kb = KnowledgeBase(clauses, clause_counter=1)
    s = Solver(kb)

    assert s.solve_instance()[1] is True


def test_solver_diplomatic_puzzle():
    clauses = {1: Clause(1, [1, -2]), 2: Clause(2, [2, 3]), 3: Clause(3, [-3, -1])}
    kb = KnowledgeBase(clauses, clause_counter=3)
    s = Solver(kb)

    res, solved = s.solve_instance()

    assert res.current_set_literals == {1:True, 2: True, 3: False}
    assert solved is True

def test_solver_case3():

    clauses = [Clause(1, [1, -2]), Clause(2, [1, -3, 2]), Clause(3, [3, 2, -1]), Clause(4, [-2, -1, 3])]
    clauses = {clause.id: clause for clause in clauses}
    kb = KnowledgeBase(clauses, clause_counter=3)
    s = Solver(kb)

    res, solved = s.solve_instance()