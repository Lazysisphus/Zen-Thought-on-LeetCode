# # 参考：https://blog.csdn.net/ggdhs/article/details/90713154
# # 最长公共子序列
# def LCS(string1, string2):
#     len1 = len(string1)
#     len2 = len(string2)
#     res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
#     for i in range(1, len2 + 1):
#         for j in range(1, len1 + 1):
#             if string2[i - 1] == string1[j - 1]:
#                 res[i][j] = res[i - 1][j - 1]+1
#             else:
#                 res[i][j] = max(res[i - 1][j], res[i][j - 1])
#     return res[-1][-1]
# print(LCS("helloworld", "loop"))

# # 最长公共子串
# def LCstring(string1, string2):
#     len1 = len(string1)
#     len2 = len(string2)
#     res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
#     result = 0
#     for i in range(1, len2 + 1):
#         for j in range(1, len1 + 1):
#             if string2[i - 1] == string1[j - 1]:
#                 res[i][j] = res[i - 1][j - 1] + 1
#                 result = max(result, res[i][j])  
#     return result
# print(LCstring("helloworld","loop"))
# # 输出结果为：2

def lcs(a,b):
	lena=len(a)
	lenb=len(b)
	c=[[0 for i in range(lenb+1)] for j in range(lena+1)]
	flag=[[0 for i in range(lenb+1)] for j in range(lena+1)]
	for i in range(lena):
		for j in range(lenb):
			if a[i]==b[j]:
				c[i+1][j+1]=c[i][j]+1
				flag[i+1][j+1]='ok'
			elif c[i+1][j]>c[i][j+1]:
				c[i+1][j+1]=c[i+1][j]
				flag[i+1][j+1]='left'
			else:
				c[i+1][j+1]=c[i][j+1]
				flag[i+1][j+1]='up'
	return c,flag

def printLcs(flag,a,i,j):
	if i==0 or j==0:
		return
	if flag[i][j]=='ok':
		printLcs(flag,a,i-1,j-1)
		print(a[i-1],end='')
	elif flag[i][j]=='left':
		printLcs(flag,a,i,j-1)
	else:
		printLcs(flag,a,i-1,j)
		
a='ABCBDAB'
b='BDCABA'
c,flag=lcs(a,b)
# for i in c:
# 	print(i)
# print('')
# for j in flag:
# 	print(j)
# print('')
printLcs(flag,a,len(a),len(b))
# print('')