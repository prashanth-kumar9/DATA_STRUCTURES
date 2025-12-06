def binString(n):
    if n == 0:
        return ['']
    else:
        smallerStrings = binString(n - 1)
        result = []
        for string in smallerStrings:
            result.append(string + '0')
            result.append(string + '1')
        return result
print(binString(3))