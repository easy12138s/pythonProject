"""
    给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
    字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

    示例 1:
    输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

    示例 2:
    输入: strs = [""]
    输出: [[""]]

    示例 3:
    输入: strs = ["a"]
    输出: [["a"]]

    思路：首先每个单词能字母异位组成的单词数量为：字母数量的阶乘，
         每次取出一个单词，将其异位组成的所有单词列表words和strs进行取交集intersection：intersection = list(set(words) & set(strs))
"""
import itertools


class Solution(object):

    def __init__(self):
        self.words = []
        self.groupWords = []

    def groupAnagrams(self, strs: list) -> list:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            self.words.append([""])
            return self.words
        else:
            for group in strs:
                print(list(group))
            return '1'

    @classmethod
    def monogram(cls, s, l, r):
        if l == r:
            return ''.join(s)
        else:
            for i in range(l, r + 1):
                s[l], s[i] = s[i], s[l]
                Solution.monogram(s, l + 1, r)
                s[l], s[i] = s[i], s[l]


if __name__ == '__main__':
    solution = Solution()
    # solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    s1 = list('abcde')
    print(Solution.monogram(s1, 0, 4))
