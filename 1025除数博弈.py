class Solution:
    def divisorGame(self, N: int) -> bool:
        # 如果 N 是奇数，因为奇数的所有因数都是奇数，因此 N 进行一次 N-x 的操作结果一定是偶数，
        # 所以如果 a 拿到了一个奇数，那么轮到 b 的时候，b拿到的肯定是偶数，这个时候 b 只要进行 -1，
        # 还给 a 一个奇数，那么这样子 b 就会一直拿到偶数，
        # 到最后b一定会拿到最小偶数2，a就输了。
        # 所以如果游戏开始时 Alice 拿到 N 为奇数，那么她必输，也就是false；
        # 如果拿到 N 为偶数，她只用 -1，让 bob 拿到奇数，最后 bob 必输，结果就是true。
        if N % 2 == 0:
            return True
        else:
            return False