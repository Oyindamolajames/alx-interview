#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
    - boxes: A list of lists representing the boxes and their keys. Each inner list represents a box, where the index of the list corresponds to the box number and the elements within the list are the keys contained in that box.

    Returns:
    - True if all boxes can be unlocked, False otherwise.

    Algorithm:
    This function uses breadth-first search (BFS) to traverse through the boxes and check if all boxes can be unlocked. It starts from the first box (box 0), marks it as visited, and adds it to a queue. Then, while the queue is not empty, it dequeues a box from the queue and checks its keys. If a key leads to an unvisited box, that box is marked as visited and added to the queue. This process continues until the queue is empty or all boxes have been visited. If all boxes have been visited, the function returns True; otherwise, it returns False.

    Example Usage:
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
