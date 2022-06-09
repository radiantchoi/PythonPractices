# LeetCode No.841 Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/

from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = deque([0])
        visited = [False] * len(rooms)
        
        while unlocked:
            now = unlocked.popleft()
            visited[now] = True
            gotkeys = rooms[now]
            rooms[now] = []
            for room in gotkeys:
                unlocked.append(room)
        
        for room in visited:
            if not room:
                return False
        
        return True