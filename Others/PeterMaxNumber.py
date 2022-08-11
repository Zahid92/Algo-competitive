def maxFavoriteNum(num):
    # 12110
    bp = -1
    i = 1
    while i < len(num):
        if num[i] < num[i - 1]:
            bp = i
            break
        i += 1
    if bp == -1:
        return num

    ans = str(int(num[:bp]) - 1)
    ans += '9' * (len(num) - len(ans))
    return ans


if __name__ == '__main__':
    n = input("Enter the Number :")
    print(maxFavoriteNum(n))
