# main.py
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

# Create folders
os.makedirs("keys", exist_ok=True)
os.makedirs("messages", exist_ok=True)

# -------------------- Encryption Functions --------------------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def generate_key():
    return Fernet.generate_key()

def encrypt_text(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode())

def decrypt_text(token, key):
    f = Fernet(key)
    return f.decrypt(token).decode()

# -------------------- File Handling --------------------
def save_to_file(content, folder, filename):
    path = os.path.join(folder, filename)
    with open(path, "wb") as f:
        f.write(content)
    return path

def load_from_file(path):
    with open(path, "rb") as f:
        return f.read()

# -------------------- GUI Mode --------------------
def gui_mode():
    window = tk.Tk()
    window.title("Text Encryption & Decryption Tool")
    window.geometry("700x450")

    tk.Label(window, text="Text / Encrypted Text:").pack()
    text_entry = tk.Entry(window, width=70)
    text_entry.pack()

    tk.Label(window, text="Shift (for Caesar) / Fernet Key:").pack()
    key_entry = tk.Entry(window, width=70)
    key_entry.pack()

    method_var = tk.StringVar(value="Fernet")
    tk.Radiobutton(window, text="Caesar Cipher", variable=method_var, value="Caesar").pack()
    tk.Radiobutton(window, text="Fernet (AES)", variable=method_var, value="Fernet").pack()

    output = tk.Text(window, height=8, width=80)
    output.pack()

    # ----------- Functions -----------
    def encrypt_action():
        text = text_entry.get()
        method = method_var.get()
        if not text:
            messagebox.showerror("Error", "Enter text to encrypt!")
            return

        if method == "Caesar":
            try:
                shift = int(key_entry.get())
                encrypted = caesar_encrypt(text, shift)
                output.delete("1.0", tk.END)
                output.insert(tk.END, encrypted)
            except:
                messagebox.showerror("Error", "Shift must be a number!")
        else:
            key = generate_key()
            encrypted = encrypt_text(text, key)
            output.delete("1.0", tk.END)
            output.insert(tk.END, encrypted.decode())

            # Show and save key
            messagebox.showinfo("Fernet Key", f"Save this key safely:\n{key.decode()}")
            key_entry.delete(0, tk.END)
            key_entry.insert(0, key.decode())

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_to_file(encrypted, "messages", f"encrypted_{timestamp}.txt")
            save_to_file(key, "keys", f"key_{timestamp}.key")
            messagebox.showinfo("Saved", f"Encrypted text and key saved to files.")

    def decrypt_action():
        text = text_entry.get()
        method = method_var.get()
        if not text:
            messagebox.showerror("Error", "Enter text to decrypt!")
            return

        if method == "Caesar":
            try:
                shift = int(key_entry.get())
                decrypted = caesar_decrypt(text, shift)
                output.delete("1.0", tk.END)
                output.insert(tk.END, decrypted)
            except:
                messagebox.showerror("Error", "Shift must be a number!")
        else:
            key_text = key_entry.get()
            if not key_text:
                messagebox.showerror("Error", "Fernet key required for decryption!")
                return
            try:
                f = Fernet(key_text.encode())
                decrypted = f.decrypt(text.encode())
                output.delete("1.0", tk.END)
                output.insert(tk.END, decrypted.decode())
            except Exception as e:
                messagebox.showerror("Decryption Error", str(e))

    def load_encrypted_file():
        path = filedialog.askopenfilename(initialdir="messages", title="Select Encrypted File")
        if path:
            content = load_from_file(path).decode()
            text_entry.delete(0, tk.END)
            text_entry.insert(0, content)

    def load_key_file():
        path = filedialog.askopenfilename(initialdir="keys", title="Select Key File")
        if path:
            content = load_from_file(path).decode()
            key_entry.delete(0, tk.END)
            key_entry.insert(0, content)

    # ----------- Buttons -----------
    tk.Button(window, text="Encrypt", command=encrypt_action).pack(pady=5)
    tk.Button(window, text="Decrypt", command=decrypt_action).pack(pady=5)
    tk.Button(window, text="Load Encrypted File", command=load_encrypted_file).pack(pady=3)
    tk.Button(window, text="Load Key File", command=load_key_file).pack(pady=3)

    window.mainloop()

# -------------------- CLI Mode (unchanged) --------------------
def cli_mode():
    print("=== Text Encryption & Decryption Tool ===")
    method = input("Choose method: [1] Caesar / [2] Fernet: ")

    if method == '1':
        action = input("Encrypt or Decrypt? [E/D]: ").upper()
        text = input("Enter text: ")
        shift = int(input("Enter shift key (number): "))
        if action == 'E':
            print("Encrypted:", caesar_encrypt(text, shift))
        else:
            print("Decrypted:", caesar_decrypt(text, shift))

    elif method == '2':
        action = input("Encrypt or Decrypt? [E/D]: ").upper()
        if action == 'E':
            text = input("Enter text to encrypt: ")
            key = generate_key()
            encrypted = encrypt_text(text, key)
            print(f"\nEncrypted Text: {encrypted.decode()}")
            print(f"Fernet Key (SAVE THIS!): {key.decode()}")
            save_to_file(encrypted, "messages", "encrypted.txt")
            save_to_file(key, "keys", "key.key")
        else:
            enc_input = input("Enter encrypted text OR file path: ")
            if os.path.exists(enc_input):
                encrypted = load_from_file(enc_input)
            else:
                encrypted = enc_input.encode()
            key_input = input("Enter Fernet key OR key file path: ")
            if os.path.exists(key_input):
                key = load_from_file(key_input)
            else:
                key = key_input.encode()
            decrypted = decrypt_text(encrypted, key)
            print("\nDecrypted Text:", decrypted)

# -------------------- Main --------------------
if __name__ == "__main__":
    mode = input("Choose Mode: [1] CLI / [2] GUI: ")
    if mode == '1':
        cli_mode()
    else:
        gui_mode()
