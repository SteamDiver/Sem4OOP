def sort_by_length(lst):
    return sorted(lst, key=len)

def by_alph(str):
    return str[0]

def sort_by_aplph(lst):
    return sorted(lst, key=by_alph)

a = ["qwqwqwqcscksn", "bac","acb","abcd", "dcdwcdwcq"]
b = sort_by_length(a)
c = sort_by_aplph(b)
print(b);
print(c);
