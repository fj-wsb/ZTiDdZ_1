import base64

def base64_encode_decode():
    plain_text_to_ascii = input("wpisz tekst do zaszyfrowania: ").encode("ascii")
    ascii_to_encoded_text = base64.b64encode(plain_text_to_ascii).decode("ascii")
    print(f"zaszyfrowany tekst: {ascii_to_encoded_text}")

    decoded_text = base64.b64decode(ascii_to_encoded_text).decode("ascii")
    print(f"odszyfrowany tekst: {decoded_text}")

base64_encode_decode()