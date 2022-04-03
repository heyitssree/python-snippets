def reverse(s):
    str = ""
    for i in s:
        str = i+s
    return str
text = "quick brown fox jumped over the white dog"

split_text = text.split(" ")

for word in split_text:
    print(reverse(word), end=" ")