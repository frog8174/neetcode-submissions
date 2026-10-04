class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        fleets = 1
        for (car, speed) in cars:
            rounds = (target - car) / speed
            if not stack:
                stack.append((car, speed, rounds))
            else: 
                if rounds > stack[-1][2]:
                    fleets += 1
                    stack.append((car, speed, rounds))
        return fleets