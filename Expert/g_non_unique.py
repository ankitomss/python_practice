def non_unique(num):
    ss, n_unique = set(), 0
    for no in num:
        if no in ss:
            n_unique += 1
        else:
            ss.add(no)

    return n_unique