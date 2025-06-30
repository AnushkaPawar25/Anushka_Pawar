# Problem-3: With a single integer as the input, generate the following until
# a = x [series of numbers as shown in below examples]

#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5
#     5) input a = 5, then output : 1, 3, 5, 7, 9
#     6) input a = 6, then output : 1, 3, 5, 7, 9
#     .
#     .
#     7) input a = x, then output : 1, 3, 5, 7, .......


class Series:
    def series(self, a: int) -> list:
        ans = []
        if a <= 0:
            return ans
        prev = 1
        curr = 1
        tempSeries = []
        while curr <= a:
            tempSeries.append(prev)
            if (curr % 2 == 1):
                ans = tempSeries[:]
            curr += 1
            prev += 2

        return ans


if __name__ == "__main__":
    a = 5
    result = Series().series(a)
    print("Result:", result)
