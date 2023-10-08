import string

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

alph_l = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
alph_h = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for ch in message:

    first_lit = None

    if ch in alph_l:
        first_lit = alph_l[0]
    elif ch in alph_h:
        first_lit = alph_h[0]

    if first_lit:
        pos = ord(ch) - ord(first_lit)
        pos = (pos + offset) % 26
        new_char = chr(pos + ord(first_lit))
    else:
        new_char = ch

    encoded_message += new_char


print(encoded_message)
