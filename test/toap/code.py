import pyotp

key = 'A373RAVJVHEDMQWJICVSIY6UATCKYJJU'
totp = pyotp.TOTP(key)
print(totp.now())