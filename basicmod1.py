def mod37_to_char(n):
    if 0 <= n <= 25:   
        return chr(n + ord('A'))
    elif 26 <= n <= 35: 
        return chr(n - 26 + ord('0'))
    elif n == 36:       
        return '_'
    else:
        return ''

sequence = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]

decrypted_message = ''.join(mod37_to_char(num % 37) for num in sequence)

flag = f"picoCTF{{{decrypted_message}}}"

print(flag)
