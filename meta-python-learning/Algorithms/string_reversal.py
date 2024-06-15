trial = 'reveral'
new_trail = trial[::-1]
print(new_trail)


## ----------- Using recursion-------

def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1] + str[0])
