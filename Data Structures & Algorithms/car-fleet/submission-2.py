class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = list(zip(position,speed))
        # pair.sort(reverse=True)
        # prevTime = (target - pair[0][0])/pair[0][1]
        # fleets = 1
        # for i in range(1, len(pair)):
        #     car = pair[i]
        #     time = (target - car[0])/ car[1]
        #     if time > prevTime:
        #         fleets += 1
        #         prevTime = time
        # return fleets

        pair = list(zip(position, speed))
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            arrival_time = (target-p)/s
            if stack and stack[-1] >= arrival_time:
                continue
            stack.append(arrival_time)

        return len(stack)

