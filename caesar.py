plain_text = input("Pls enter your plain text: ")
plain_text.lower()
shift = int(input("Pls enter the shift value: "))
encrypted_text = ""

abc = "abcdefghijklmnopqrstuvwxyz"

for i in plain_text:
    if i in abc:
        char_index = abc.find(i)
        encrypted_text += abc[(char_index + shift) % len(abc)]
    else:
        encrypted_text += i
        
print("The encrypted sentence is:",encrypted_text)