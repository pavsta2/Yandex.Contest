with open('input.txt') as f:
    num = int(f.readline())
    print(num)

    S = f.readline()
    print(S)
result = ""
for i in range(num):
    if i == 0:
        l = -1
        result += str(l)
    else:
        for j in range(len(S[0:i])):
            if S[i] == '1' and S[j:(i+1)].count('1') > S[j:(i+1)].count('0'):
                l = j+1
                result += ' ' + str(l)
                break
            elif S[i] == '0' and S[j:(i+1)].count('1') < S[j:(i+1)].count('0'):
                l = j + 1
                result += ' ' + str(l)
                break
            else:
                l = -1
                if j == len(S[0:i])-1:
                    result += ' ' + str(l)

print(result)


