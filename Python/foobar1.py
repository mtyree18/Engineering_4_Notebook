def solution(data, n):
    remove = []
    for x in data:
        num = data.count(x)
        if num > n:
            remove.append(x)
    result = [x for x in data if x not in remove]
    return result
solution(data,n)
