def getLucky(s: str, k: int) -> int:
    result = 0
    char = 'a'
    dic = {char: str((ord(char) % 97) + 1)}
    for i in range(-1, 24):
        value = ord(char) + 1
        char = chr(value)
        value = (value % 97) + 1
        dic[char] = str(value)
    print(dic)

    ans = ""
    for i in s:
        ans = ans + dic[i]
    print(ans)
    while k > 0:
        result = 0
        for i in ans:
            result = result + int(i)
        ans = str(result)
        k = k - 1
        print(result)
    return result