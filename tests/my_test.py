import elgamal
keys = elgamal.generate_keys()
priv = keys['privateKey']
pub = keys['publicKey']
message = "ya popochka"
print(message)
cipher = elgamal.encrypt(pub, message)
print(cipher)
plain = elgamal.decrypt(priv, cipher)
print(plain)