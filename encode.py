import base64

encode_text = input(str("Encode here : "))
encode_text_bytes = encode_text.encode("ascii")
base64_bytes = base64.b64encode(encode_text_bytes)
base64_string = base64_bytes.decode("ascii")
print(f"Your encode: {base64_string}\n")
