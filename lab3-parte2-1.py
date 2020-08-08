from Crypto.Hash import HMAC, SHA256

secret = b'Cifrado de informacion seccion 10'
h = HMAC.new(key=b'CC3078', msg=secret, digestmod=SHA256)
print(h.hexdigest())

secret = b'La implementacion de este ejercicio fue sencilla'
h = HMAC.new(key=b'MAC', msg=secret, digestmod=SHA256)
print(h.hexdigest())

