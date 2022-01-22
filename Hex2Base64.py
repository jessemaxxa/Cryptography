import codecs


def hex2base(hex):
	
	
	b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
	print(b64)

hex2base("1c0111001f010100061a024b53535009181c")
