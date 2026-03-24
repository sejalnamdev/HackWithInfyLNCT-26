def luckBalance(k, contests):
    imp = sorted([l for l, t in contests if t], reverse=True)
    unimp = sum(l for l, t in contests if not t)
    return unimp + sum(imp[:k]) - sum(imp[k:])