# Sigalog: Easy Signing URLs.

This module has only two uses:

`python -m Sigalog make_key`

to make a public-private key pair in the current directory, and

`python -m Sigalog sign <url>`

to produce a URL signature. Make you are `cd`'d into the same directory as your private key.
