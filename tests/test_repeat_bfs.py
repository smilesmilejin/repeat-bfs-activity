from activity.main import repeat_bfs
import pytest 

def test_repeat_bfs_no_edges():
    #Arrange
    graph = {
        1: [],
        2: [],
        3: [],
        4: []
    }

    #Act
    result = repeat_bfs(graph)

    #Assert
    assert result == [1, 2, 3, 4]

def test_repeat_bfs_two_islands():
    #Arrange
    graph = {
        1: [3],
        2: [4],
        3: [1],
        4: [2]
    }

    #Act
    result = repeat_bfs(graph)

    #Assert
    assert result == [1, 3, 2, 4]

def test_repeat_bfs_empty_graph():
    #Arrange
    graph = {}

    #Act
    result = repeat_bfs(graph)

    #Assert
    assert result == []

def test_repeat_bfs_disconnected_graph():
    #Arrange
    graph = {
        1: [5,3],
        2: [],
        3: [5],
        4: [1,2],
        5: [3]
    }

    #Act
    result = repeat_bfs(graph)

    #Assert
    assert result == [1, 5, 3, 2, 4]