import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

def main():
    trie = Trie()
    nums = []
    for _ in range(int(input())):
        strr = input().strip()
        nums.append(strr)
        trie.insert(strr)
    for num in nums:
        if trie.starts_with(num) != [num]:
            return "NO"
    return "YES"

if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())

"""

1
3
21
214
225

2
3
911
97625999
91125426
5
113
12340
123440
12345
98346


1
5
113
12340
123440
12345
98346

"""
# # 첫번째 시도: Trie는 인터넷 참고하여 작성 후 돌렸는데 전체를 한번 싹 입력받고 싹 정렬하여서 그런가 시간초과
# # 이후엔 각각 입력받는 즉시 판단하도록
# def main():
#     tri = Trie()
#     nums = []
#     n = int(input())
#     for _ in range(n):
#         nums.append(input().strip())
#     nums.sort()
#     for i in range(n):
#         tri.insert(nums[i])
#         for j in range(i):
#             if nums[i] in tri.starts_with(nums[j]):
#                 return "NO"
#     return "YES"
#
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         print(main())
