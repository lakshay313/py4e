def computepay(hrs, rate):
    ans = hrs * rate
    if hrs > 40:
        ans = ans + (hrs-40)*rate*.5

    return ans


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("error")
    quit()

p = computepay(h,r)
print(p)
