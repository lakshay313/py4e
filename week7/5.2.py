maxV = None
minV = None
while True:
    val = input("Enter a number :")
    if val == 'done':
        break
    try:
        v = int(val)
    except:
        print("Invalid input")
        continue

    if maxV is None:
        maxV = v
        minV = v
    if maxV < v:
        maxV = v
    if minV > v:
        minV = v

print("Maximum is",maxV)
print("Minimum is",minV)
