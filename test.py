def solution(s):
    result = []
    if len(s) % 2:
        s += "_"
    for i in range(0, len(s), 2):
        print(s)
        result.append(s[i] + s[i + 1])
    return result


print(solution(s="abcde"))
