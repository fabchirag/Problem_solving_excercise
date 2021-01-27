ints = input("Enter a value for ints: ").split()
t = tuple(float(i) for i in ints)
print("you Hash is: ", hash(t))
