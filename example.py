# Step 1: Generate a key pair (usually done beforehand)
import ast
import hashlib
import encryption
import json
import RSAencryption
import SHA_256

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
print("with hashing as string: ",valid)

print("")

sig2=RSAencryption.create_sig('alice',private_key)
print("with hashing as int the message: ",RSAencryption.verify_sig('alice',sig2,public_key))

print("")
print("checking public key encyrption and decryption")
encrypted=encryption.RSAencryptCH((public_key),private_key)
decrypted=encryption.RSAdecryptCH(encrypted,public_key)
print( encryption.convert_to_tuple(decrypted) == public_key)
