# Problem: Number of recent calls
# Approach: Use a queue to store timestamps; for each new call, push the timestamp and remove all timestamps older than 3000 ms to keep only the valid recent calls.
# Time Complexity:O(1)
# Space Complexity: O(n)
class RecentCounter:
    
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)    


