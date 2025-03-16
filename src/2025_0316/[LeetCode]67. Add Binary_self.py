class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = 0
        num_a = int(a, 2)
        num_b = int(b, 2)

        sum_val = num_a + num_b

        ans = bin(sum_val)[2:]
        return ans


if __name__ == "__main__":
    a = "11"
    b = "1"
    sol = Solution()
    print(sol.addBinary(a, b))