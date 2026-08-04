class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse = True)
        prevTime = (target - pair[0][0])/pair[0][1]
        fleets = 1
        for i in range(1,len(pair)):
            curCar = pair[i]
            time = (target - curCar[0])/curCar[1]
            if time > prevTime:
                prevTime = time
                fleets += 1

        return fleets
