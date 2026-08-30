import json, sqlite3
from cryptography.fernet import Fernet

KEY_FILE = "key.json"
DB = "static/SQL/usr.db"

# load key from JSON
# with open(KEY_FILE, "r") as fkey:
#     data = json.load(fkey)
#     key = data["fernet_key"]
key = "VVVCpeqUR3iSoWU1zcUNbNPGczVKN3q-rkT9JhYoQrA="
f = Fernet(key)
print(key)


conn = sqlite3.connect(DB)
cursor = conn.cursor()
usrN = input("UserName: ")
cursor.execute("SELECT password FROM usr WHERE username=?", (usrN,))
row = cursor.fetchone()
conn.close()

print("Stored password (raw):", row[0])
if row:
    stored_encrypted_pass = row[0]
    # make sure we have bytes
    if isinstance(stored_encrypted_pass, str):
        stored_encrypted_pass = stored_encrypted_pass.encode()

    decrypted_pass = f.decrypt(stored_encrypted_pass).decode()
    print("Decrypted pass:", decrypted_pass)
else:
    print("User not found")

