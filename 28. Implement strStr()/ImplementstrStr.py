def strStr(self, haystack: str, needle: str) -> int:
    haystackLen = len(haystack)
    needleLen = len(needle)

    for i in range(haystackLen):
        startInd = i
        endInd = i + needleLen
        if endInd <= haystackLen:

            if haystack[startInd:endInd] == needle:
                return startInd
    return -1