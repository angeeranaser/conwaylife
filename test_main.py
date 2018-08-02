# Game of Life
# Program by: Angeera Naser
# angeeraxn@gmail.com
# github.com/angeeranaser
# Project referenced from https://robertheaton.com/2018/07/20/project-2-game-of-life/

import numpy as np
import main

def test_dead_cells_no_neighbors(): # Do dead cells with no live neighbors stay dead?
    init = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]) # None of the dead cells have 3 neighbors.
    expected = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]) # None of the dead cells should come alive.
    actual = main.next_board(init)
    assert np.array_equal(expected, actual)

def test_dead_cells_three_neighbors(): # Do dead cells with three live neighbors come alive?
    init = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]) # Cell (0,0) is dead and has 3 neighbors/
    expected = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]) # Cell (0,0) should come alive.
    actual = main.next_board(init)
    assert np.array_equal(expected, actual)

def test_live_cells_few_neighbors(): # Do live cells with too few neighbors die?
    init = np.array([
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]) # Cell (2,1) is alive, but has less than 2 neighbors.
    expected = np.array([
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]) # Cell (2,1) should die.
    actual = main.next_board(init)
    assert np.array_equal(expected, actual)

def test_live_cells_many_neighbors(): # Do live cells with too many neighbors die?
    init = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]) # Cell (1,1) is alive, but has more than 3 neighbors.
    expected = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]) # Cell (1,1) should die (and cells (0,0), (2,0), (0,2), and (2,2) come alive).
    actual = main.next_board(init)
    assert np.array_equal(expected, actual)

def test_prettify(): # Is the output of the pretty-printer correct?
    init = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ])
    expected = '|     O     |\n' \
               '|  O  O  O  |\n' \
               '|     O     |\n'
    actual = main.prettify(init)
    assert expected == actual

