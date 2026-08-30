from cryptography.fernet import Fernet
import json,sqlite3
KEY_FILE = "key.json"

DB = "static/SQL/usr.db"
from cryptography.fernet import Fernet

# Assume you have an encrypted message and a key from a previous encryption
with open(KEY_FILE, "r") as f:
        data = json.load(f)
        key = data["fernet_key"]  # convert back to bytes
        f = Fernet(key)





conn = sqlite3.connect(DB)
cursor = conn.cursor()
print("list of usrenames: " + cursor.execute("SELECT username FROM usr").fetchall().__str__())
usrN = input("Username: ")
cursor.execute("SELECT password FROM usr WHERE username=?", (usrN,))
row = cursor.fetchone()
conn.close()

if row:
            stored_encrypted_pass = row[0]
            decrypted_pass = f.decrypt(stored_encrypted_pass).decode()

print("Decrypted message:", decrypted_pass)