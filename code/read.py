import os
from typing import List, Generator
from code.clause import Clause


def read_rules(rules_path: str) -> Generator[Clause, None, None]:
    id = 0
    with open(rules_path) as f:
        for line in f:
            tokens = line.split(' ')
            if tokens[-1] != '0\n':
                continue

            literals = [int(token) for token in tokens[0:-1]]

            yield Clause(id, literals)
            id += 1


if __name__ == "__main__":
    rules_path = os.getcwd() + "/../data/sudoku-rules.txt"
    sudoku_path = os.getcwd() + "/../data/sudoku-example.txt"

    clauses = read_rules(rules_path)
    print("Rules:", list(clauses))

    clauses = list(read_rules(sudoku_path))
    expected = [[168], [175], [225], [231], [318], [419], [444], [465], [493], [689], [692], [727], [732], [828], [886], [956], [961], [973]]

    assert str(clauses) == str(expected)
