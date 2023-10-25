# Step 1: Generate a key pair (usually done beforehand)
import ast
import hashlib
import encryption_module
import json
import RSAencryption_module
import SHA256_module

private_key, public_key =encryption_module.RSAkeygeneration(8)

# Step 2: Create certificate content
certificate_content = {
    'subject': 'Alice',
    'public_key': public_key
}

# Step 3: Certificate signing
certificate_hash=SHA256_module.sha256(str(certificate_content).encode())
certificate_hash_str=str(certificate_hash)

json_string = json.dumps(certificate_content)
signature = encryption_module.create_sig(json_string, private_key)

# Step 4: Assemble certificate
certificate = {
    'certificate_content': certificate_content,
    'signature': signature,
}

# Step 5: Verification

valid=encryption_module.verify_sig(json_string,signature,public_key)
print("with hashing as string: ",valid)

print("")

sig2=RSAencryption_module.create_sig('alice',private_key)
print("with hashing as int the message: ",RSAencryption_module.verify_sig('alice',sig2,public_key))

print(public_key)
encrypted=encryption_module.RSAencryptCH(json.dumps(public_key),private_key)
decrypted=encryption_module.RSAdecryptCH(encrypted,public_key)
print(encryption_module.convert_to_tuple(decrypted) == public_key)
