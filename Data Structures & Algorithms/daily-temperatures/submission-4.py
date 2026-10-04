class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        for i in range(len(temperatures) - 2, -1, -1):
            temperature = temperatures[i]
            day_check = 1

            while (day_check + 1) < length:

                the_check_temp = temperatures[i + day_check]

                if the_check_temp > temperature:
                    result[i] = day_check
                    break
                elif result[i + day_check] == 0:
                    break
                else:                 
                    day_check += result[i + day_check]
        return result