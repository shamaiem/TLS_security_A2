# Step 1: Generate a key pair (usually done beforehand)
import ast
import hashlib
import encryption_module as encryption
import json
import RSAencryption_module as RSAencryption
import SHA256_module as SHA_256

private_key, public_key =encryption.RSAkeygeneration(8)

# Step 2: Create certificate content
certificate_content = {
    'subject': 'Alice',
    'public_key': public_key
}

# Step 3: Certificate signing
certificate_hash=SHA_256.sha256(str(certificate_content).encode())
certificate_hash_str=str(certificate_hash)

json_string = json.dumps(certificate_content)
signature = encryption.create_sig(json_string, private_key)

# Step 4: Assemble certificate
certificate = {
    'certificate_content': certificate_content,
    'signature': signature,
}

# Step 5: Verification
valid=encryption.verify_sig(json_string,signature,public_key)
print(valid)
# valid= encryption.verify_sig(json_string, signature, public_key)
# print("without the hashing the message: ",valid)

# sig2=RSAencryption.create_sig('alice',private_key)
# print("with hashing the message: ",RSAencryption.verify_sig('alice',sig2,public_key))

# print(public_key)
encrypted=encryption.RSAencryptCH((public_key),private_key)
decrypted=encryption.RSAdecryptCH(encrypted,public_key)
print( encryption.convert_to_tuple(decrypted) == public_key)
