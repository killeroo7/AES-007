# AES-007
A python tool to perform AES Encryption or Decryption.

# USAGE
1) Encryption
```
python3 AES-007.py -k "Key" --iv "16BitIV" -p "plaintext"
```

2) Decrpytion
```
python3 AES-007.py -k "Key" --iv "16BitIV" -c "cipherText"
```

# FLAGS:
```
  -k --key [KEY]     Key/Password
  --iv [IV]          16 bit IV
  -p PLAINTEXT       Encrpyted Text
  -c CIPHERTEXT      Cipher Text
  -m --mode [mode]   Mode of Operation [default=AES.MODE_CBC]
```

# Supported Modes of Operations:
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
