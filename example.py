# Step 1: Generate a key pair (usually done beforehand)
import ast
import hashlib
import encryption
import json
import RSAencryption

private_key, public_key =encryption.RSAkeygeneration(8)

# Step 2: Create certificate content
certificate_content = {
    'subject': 'Alice',
    'public_key': public_key
}

# Step 3: Certificate signing

json_string = json.dumps(certificate_content)
signature = encryption.create_sig(json_string, private_key)

# Step 4: Assemble certificate
certificate = {
    'certificate_content': certificate_content,
    'signature': signature,
}

# Step 5: Verification
# valid= encryption.verify_sig(json_string, signature, public_key)
# print("without the hashing the message: ",valid)

# sig2=RSAencryption.create_sig('alice',private_key)
# print("with hashing the message: ",RSAencryption.verify_sig('alice',sig2,public_key))

print(public_key)
encrypted=encryption.RSAencryptCH(json.dumps(public_key),private_key)
decrypted=encryption.RSAdecryptCH(encrypted,public_key)
print( encryption.convert_to_tuple(decrypted) == public_key)
