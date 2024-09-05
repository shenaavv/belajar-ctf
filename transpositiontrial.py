flag_enc = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"

flag = ""
for i in range(12, len(flag_enc),3):
    temp = flag_enc[i:i+3]
    flag += temp[2] + temp[0:2]

print(flag)
