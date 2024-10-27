class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                subStr = ''
                print(stack)
                while True:
                    ch = stack.pop()
                    if ch == "[":
                        break
                    else:
                        subStr = ch + subStr

                num = ''
                while stack and len(stack[-1]) == 1 and 48 <= ord(stack[-1]) <= 57:
                    ch = stack.pop()
                    num += ch
                num = num[::-1]
                stack.append(int(num) * subStr)
        return ''.join(stack)
