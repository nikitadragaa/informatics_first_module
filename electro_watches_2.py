n=int(input())
hours = n // 3600
n = n - hours * 3600
minutes = n // 60
n = n - minutes * 60
seconds = n % 60

def add_zero(digit):
    if digit < 10:
        digit = '0' + str(digit)
    return digit

minutes = add_zero(minutes)
seconds = add_zero(seconds)
    
print(hours % 24, minutes, seconds, sep=":")
