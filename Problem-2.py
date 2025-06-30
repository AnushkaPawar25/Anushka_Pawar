# Problem-2: With a single integer as the input, generate the following until 
# a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     .
#     .
#     5) input a = x, then output : 1, 3, 5, 7, .......


class Series:
    
    def oddSeries(self, a: int) -> list:
        ans = []
        prev = 1
        
        while a > 0:
            ans.append(prev)
            prev += 2
            a -= 1

        return ans


if __name__ == "__main__":
    a = 10
    series = Series()
    result = series.oddSeries(a)
    print("Result:", result)