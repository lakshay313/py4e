hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
ans = 0.0

ans = ans + r * h

if h - 40 > 0:
    ans = ans + r * 0.5 * (h - 40)

print(ans)
