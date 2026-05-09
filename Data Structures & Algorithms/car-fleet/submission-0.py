class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = list(zip(position, speed)) # A list of tuples (car pos, speed of car)
        # print(pairs)

        # Sort the tuples by the car positions in descending order
        pairs.sort(reverse=True)

        # After sorting, calculate the time taken to reach the target. 
        times = []
        for t in pairs:
            d, s = t[0], t[1]
            time = (target - d) / s
            times.append(time)
        print(times)
        # Then, iterate through times
        stack, num_fleets = [], 0
        for t in times:
            if not stack:
                stack.append(t)
                num_fleets += 1
            curr = stack[-1]
            # if the time of subsequent cars <= the previous one, it is in the same fleet
            if t <= curr: continue
            
            # Otherwise, the the car we are looking at is a new fleet, set base = this current time. 
            stack.append(t)
            num_fleets += 1

        # Return the size of the stack
        return num_fleets;