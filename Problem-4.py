# Problem-4: Get the total count of number listed in the dictionary which is
# multiple of [1,2,3,4,5,6,7,8,9]
#   (examples)
#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

from collections import defaultdict


class Divisibility:
    def frequency(self, arr: list) -> map:
        mp = defaultdict(int)
        
        for num in arr:
            for i in range(1, 10):
                if num % i == 0:
                    mp[i] = mp.get(i, 0) + 1

        return mp


if __name__ == "__main__":
    arr = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result = Divisibility().frequency(arr)
    print("Result:", result)
