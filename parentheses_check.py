def parenthesis_check(brackets):
    s = []
    i, n = 0, len(brackets)
    while i < n:

        if brackets[i] in "[{(":
            s.append(brackets[i])
        elif s and ((s[-1] == "(" and brackets[i] ==")") or (s[-1] == "{" and brackets[i] =="}") or (s[-1] == "[" and brackets[i] =="]")):
            s.pop()
        else:
            return False
        i += 1

    if not s:
        return True

s = "[()]{}{[()()]()}"
print parenthesis_check(s)
