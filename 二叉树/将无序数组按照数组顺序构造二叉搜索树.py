
def str_inx(word_, string_):
    return [i for i in range(len(string_)) if string_[i] == word_]

def ab_max_inx(s_a, s_b):
    i, len_a, len_b = 0, len(s_a), len(s_b)
    while len_a > i and len_b > i and s_a[i] == s_b[i]:
        i += 1
    return i

def common_substr(s_a, s_b):
    """
    两个字符串的所有公共子串，包含长度为1的
    :param s_a:
    :param s_b:
    :return:
    """
    res = []
    if s_a:
        a0_inx_in_b = str_inx(s_a[0], s_b)
        if a0_inx_in_b:
            b_end_inx, a_end_inx = -1, 0
            for inx in a0_inx_in_b:
                if b_end_inx > inx:
                    continue
                this_inx = ab_max_inx(s_a, s_b[inx:])
                a_end_inx = max(a_end_inx, this_inx)
                res.append(s_a[:this_inx])
                b_end_inx = this_inx + inx
            res += common_substr(s_a[a_end_inx:], s_b)
        else:
            res += common_substr(s_a[1:], s_b)
    return res

res = common_substr("0123456789", "123a345890")
print(res)

'''
给出两个字符串。
0123456789
123a345890
返回所有的公共子串，子串不能有重复的字符。
【0，123，45，89】
【0，12，345，89】
要求时间空间复杂度尽量最优。
'''
    0 1 2 3 4 5 6 7 8 9
1   0 1 0 0 0 0 0 0 0 0
2   0 0 1 0 0 0 0 0 0 0
3   0 0 0 1 0 0 0 0 0 0 
a   0 0 0 0 0 0 0 0 0 0
3   0 0 0 1 0 0 0 0 0 0 
4   0 0 0 0 1 0 0 0 0 0
5   0 0 0 0 0 1 0 0 0 0
8   0 0 0 0 0 0 0 0 1 0
9   0 0 0 0 0 0 0 0 0 1
0   1 0 0 0 0 0 0 0 0 0