s = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def solutions(S, k):
    k = s.index(S) + k
    i = k if k < 7 else k % 7
    return s[i]

if __name__ == "__main__":
    print(solutions("Sat", 5))
