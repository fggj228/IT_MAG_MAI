package feffhteens.models.solver;

import feffhteens.models.board.Board;

public interface IntSolver {
    boolean isSolvable();
    int moves();
    Iterable<Board> solution();
}
