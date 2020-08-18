class Solution:
    import re
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 关键步骤：先把所有标点符号用空格代替
        # 注意，split(" ")和split()是不同的
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.split()
        hash_map = {}
        for word in words:
            word = word.strip("!?',;.").lower()
            hash_map[word] = hash_map.get(word, 0) + 1
        for k, v in sorted(hash_map.items(), key=lambda x: x[1], reverse=True):
            if k not in banset:
                return k