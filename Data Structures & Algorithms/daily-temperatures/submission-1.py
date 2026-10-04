class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        for i in range(len(temperatures))[:-1:][::-1]:
            temperature = temperatures[i]
            day_check = 1

            # if the next day is warmer than today, solves.
            if temperature < temperatures[i+day_check]: 
                result[i] = day_check

            # when the next day is not warmer, retrives the warmer day of the next day
            else:
                # but if no warmer for the next day, no needs for retrives
                if result[i+day_check] == 0:
                    result[i] = 0

                # the retrives
                while result[i+day_check] != 0:
                    day_check += result[i+day_check]
                    the_warmer_temp = temperatures[i+day_check]
                    if the_warmer_temp > temperature:
                        result[i] = day_check
                        break
                    if (the_warmer_temp < temperature) and (result[i+day_check]==0):
                        result[i] = 0
                        break
        return result