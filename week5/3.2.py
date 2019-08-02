hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

ans = 0.0

ans = ans + r * h

if h - 40 > 0:
    ans = ans + r * 0.5 * (h - 40)

print(ans)
