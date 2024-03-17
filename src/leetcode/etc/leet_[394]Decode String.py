# Given an encoded string, return its decoded string. 
# 
#  The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. Note that k is guaranteed to 
# be a positive integer. 
# 
#  You may assume that the input string is always valid; there are no extra 
# white spaces, square brackets are well-formed, etc. Furthermore, you may assume 
# that the original data does not contain any digits and that digits are only for 
# those repeat numbers, k. For example, there will not be input like 3a or 2[4]. 
# 
#  The test cases are generated so that the length of the output will never 
# exceed 10⁵. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 30 
#  s consists of lowercase English letters, digits, and square brackets '[]'. 
#  s is guaranteed to be a valid input. 
#  All the integers in s are in the range [1, 300]. 
#  
# 
#  Related Topics String Stack Recursion 👍 12396 👎 581


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        answer = ''
        for c in s :
            if c != ']':
                # ] 만날때까지 stack에 넣기
                stack.append(c)
            else:
                decode = '' # decode string

                # [ 만날때까지 decoe 에 붙이기
                while stack[-1] != '[':
                    decode += stack.pop()

                stack.pop() # [ 제거
                k = '' #숫자
                while stack and stack[-1].isdigit() == True:
                    k += stack.pop()  # 현재 숫자가 문자로 이므로 숫자를 문자로 뽑아내기

                stack.append(decode*int(k[::-1])) #숫자가 거꾸로 k에 들어있으므로 reverse

        for word in stack:
            answer += ''.join(word[::-1]) #각각 들어있는 word를 합치기
        return answer
        
# leetcode submit region end(Prohibit modification and deletion)
