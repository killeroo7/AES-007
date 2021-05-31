#!/usr/bin/env python3

from Crypto.Cipher import AES
import base64
import argparse
from termcolor import colored


def banner():
	x = '''

	 █████╗ ███████╗███████╗       ██████╗  ██████╗ ███████╗
	██╔══██╗██╔════╝██╔════╝      ██╔═████╗██╔═████╗╚════██║
	███████║█████╗  ███████╗█████╗██║██╔██║██║██╔██║    ██╔╝
	██╔══██║██╔══╝  ╚════██║╚════╝████╔╝██║████╔╝██║   ██╔╝ 
	██║  ██║███████╗███████║      ╚██████╔╝╚██████╔╝   ██║  
	╚═╝  ╚═╝╚══════╝╚══════╝       ╚═════╝  ╚═════╝    ╚═╝                                                                                        
	'''
	y = "\t+----------------------------------------------------+"     
	z = "							~~Twitter: Killeroo7p\n"

	print(colored(x,"red"))
	print(colored(y,"magenta"))
	print(colored(z,"blue"))


def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-k','--key',dest='key',help="Key/Password",required=True)
        parser.add_argument('--iv',dest='iv',help="IV",required=True)        
        parser.add_argument('-p',dest='plaintext',help="Encrpyted Text")
        parser.add_argument('-c',dest='ciphertext',help="Cipher Text")
        parser.add_argument('-m','--mode',dest='mode',help="Mode of Operation [default=AES.MODE_CBC]",default=AES.MODE_CBC)
        args = parser.parse_args()

        if not args.plaintext and not args.ciphertext:
        	parser.error(colored("Please Enter Either Plain Text or Cipher Text","magenta"))
        return args

def pad(msg):
	return msg + b"\0" * (AES.block_size - len(msg)%AES.block_size)

def encrypt(message, key, iv, mode, key_size=256):
	message = pad(message)
	cipher = AES.new(key, mode, iv)
	return base64.b64encode(cipher.encrypt(message))     

def decrypt(ciphertext, key, iv, mode):
	ciphertext = base64.b64decode(ciphertext)
	cipher = AES.new(key, mode, iv)
	plaintext = cipher.decrypt(ciphertext)
	return plaintext.rstrip(b"\0")


banner()
args = get_args()
key = args.key
iv = args.iv
mode = getattr(AES, args.mode.split('.')[1])

if args.plaintext:
	plaintext = args.plaintext
	encryptedMsg = encrypt(plaintext.encode(),key.encode(),iv.encode(),mode)
	print(colored("PLAIN TEXT     = ","cyan") + colored(plaintext,"yellow"))
	print(colored("ENCRYPTED TEXT = ","cyan") + colored(encryptedMsg.decode(),"yellow"))

elif args.ciphertext:
	ciphertext = args.ciphertext
	decryptedMsg = decrypt(ciphertext.encode(),key.encode(),iv.encode(),mode)

	print(colored("ENCRYPTED TEXT = ","cyan") + colored(ciphertext,"yellow"))
	print(colored("DECRYPTED TEXT = ","cyan") + colored(decryptedMsg.decode(),"yellow"))


'''
#Key Notes About AES
1) AES key must be either 16, 24, or 32 bytes long
2) IV must be 16 bytes long
3) Cipher Text must be a multiple of 16 in length. 
4) Plain Text must also be multiple of 16 but program automatically pads it. So can be any length.
'''