inp = input()
print(any(c.isalnum() for c in inp))
print(any(c.isalpha() for c in inp))
print(any(c.isdigit() for c in inp))
print(any(c.islower() for c in inp))
print(any(c.isupper() for c in inp))


