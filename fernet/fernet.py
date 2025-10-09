from cryptography.fernet import Fernet 

key = Fernet.generate_key() # Generated key is below. 
key = "g11qIt5Z1x56bjNsQoADVOQSIDClnfmc6E6SKBTZJc8=" 
print(key) 

f = Fernet(key) 

token = f.encrypt(b"A really secret message. Not for prying eyes.")