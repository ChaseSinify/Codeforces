w = int(input())
def yn(w):
    if w <= 2:
        return "NO"
    if w % 2 == 1:
        return "NO"
    return "YES"
print(yn(w))