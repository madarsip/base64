import base64

decode_text = input(str("Decode here : "))
decode_bytes = decode_text.encode("ascii")
decode_string_bytes = base64.b64decode(decode_bytes)
decode_string = decode_string_bytes.decode("ascii")
print(f"Decoded string: {decode_string}\n")
