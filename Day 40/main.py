import random
text = input("Enter text: ")


def Encyption (text):
    text_list = text.lower().split()
    transformed_text = []
    for i in text_list:
        after = random.sample(text, 3)
        before = random.sample(text, 3)
        if len(i) >= 3:
            coded_word = i[1:] + i[0] 
            coded_word = before[0] + coded_word + after[0] 
            transformed_text.append(coded_word)
        else:
            print("Word is too short to encrypt")
            coded_word = i   
            transformed_text.append(coded_word)
    return " ".join(transformed_text)

Encrptioned_text = Encyption(text)
print( "Encrypted text: ", Encrptioned_text)


def Decryption(Encrptioned_text):
    Encrptioned_text
    transformed_text = []
    for i in Encrptioned_text.lower().split():
        if len(i) >= 3:
            uncoded_word = i[1:-1] 
            uncoded_word = uncoded_word[-1] + uncoded_word[:-1]
            transformed_text.append(uncoded_word)
        else:
            print("Word is too short to decrypt")
            uncoded_word = i
            transformed_text.append(uncoded_word)
    return " ".join(transformed_text)

Decrypted_text = Decryption(Encrptioned_text)
print("Decrypted text: ", Decrypted_text)

if Decrypted_text == text.lower():
    print("Decryption successful!")
else:
    print("Decryption failed. The original text and decrypted text do not match.")
