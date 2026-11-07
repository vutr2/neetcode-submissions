class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            results += str(len()) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            result.append(s[start: start] + length)

            i = start + length

        return result