# Caesar Cipher

Using an ancient encryption technique, this application can take a phrase and encrypt, decrypt, or crack it (as long as it uses the Caesar Cipher!).

## API

- encrypt(phrase, key) - takes a given phrase, and an integer to tell how much to 'shift' the letters in the alphabet, and returns an encrypted message.
- decrypt(encrypted_phrase, -key) - takes an encrypted message and a known key, returns an unencrypted message.
- crack(encrypted_phrase): takes an encrypted message and returns the most likely unencrypted message.
