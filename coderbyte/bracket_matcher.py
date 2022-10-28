def BracketMatcher(strParam):
    either = False
    open_count = 0
    close_count = 0
    for c in strParam:
        if not either and c == ")":
            return 0
        if c == "(":
            either = True
            open_count += 1
        if c == ")":
            close_count += 1
            if open_count == close_count:
                either = False
    if open_count == close_count:
        return 1
    else:
        return 0

test1 = "(coder)(byte))"
#Output: 0
test2 = "(c(oder)) b(yte)"
#Output: 1 

print(BracketMatcher(test2))