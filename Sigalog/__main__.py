import sys
import os
import oscrypto.asymmetric as asym
import base64

pubkey_filename = "sigalog_pub.pem"
privkey_filename = "sigalog_priv.pem"

    
help_text = """Sigalog: Easy Signing URLs.

This module has only two uses:

python -m Sigalog make_key

to make a public-private key pair in the current directory, and

python -m Sigalog sign <url>

to produce a URL signature. Make you are `cd`'d into the same directory as your private key."""


if len(sys.argv) > 1:
    command = sys.argv[1]
else:
    command = ""

if command=="make_key":
    if os.path.isfile(pubkey_filename):
        print(pubkey_filename + " already exists, move it somewhere else. I don't want to overwrite any keys.")
    elif os.path.isfile(privkey_filename):
        print(privkey_filename + " already exists, move it somewhere else. I don't want to overwrite any keys.")
    else:
        print("Generating Key Pair")
        pub, priv = asym.generate_pair("rsa", bit_size = 2048)
        pub_f = open(pubkey_filename, 'wb')
        priv_f = open(privkey_filename, 'wb')
        pub_f.write(asym.dump_public_key(pub, "pem"))
        priv_f.write(asym.dump_private_key(priv, u'salt', "pem"))
        pub_f.close()
        priv_f.close()
elif command=="sign":
    if len(sys.argv) < 3:
        print(help_text)
    else:
        url = sys.argv[2]
        print("signing url: "+url)

        if not os.path.isfile(privkey_filename):
            print(privkey_filename + " does not exist, run the make_key command.")
        else:
            f = open(privkey_filename, 'rb')
            privkey = f.read()
            f.close()
            priv = asym.load_private_key(privkey, u'salt')
            
            sig = asym.rsa_pss_sign(priv, url, "sha256")
            print(base64.b64encode(sig))
else:
    print(help_text)
