import collections
def remove_dup_letters(s):
    counter = collections.Counter(s)

    stack = []
    for c in list(s):
        counter[c] -= 1
        if c in stack:
            continue

        while stack and stack[-1] > c and counter[stack[-1]] > 0:
            stack.pop()

        stack.append(c)
    return "".join(stack)

print remove_dup_letters("ankitvi")