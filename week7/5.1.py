num = 0
total = 0.0
while True:
    val = input("Enter a number :")
    if val == 'done':
        break
    try:
        v = float(val)
    except:
        print("Invalid Input")
        continue

    num += 1
    total += v

print(total, num, total/num)
