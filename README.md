

# Text Encryption & Decryption Tool

## **Description**

A Python application to **secure text messages** using two encryption methods: **Caesar Cipher** (educational/simple) and **Fernet (AES-based)** encryption (secure and real-world standard).

The tool features both **GUI and CLI modes**, automatic key generation, file save/load functionality, and a user-friendly interface for encrypting and decrypting messages safely.

---

## **Features**

* **Encrypt & Decrypt Text**

  * **Caesar Cipher:** Basic text shifting (for learning encryption logic).
  * **Fernet (AES-based):** Strong, secure encryption with HMAC validation.
* **Automatic Key Management:** Fernet key is generated automatically and displayed to the user.
* **File Handling:**

  * Save encrypted messages to `messages/` folder.
  * Save keys to `keys/` folder.
  * Load messages and keys from files for decryption.
* **GUI & CLI Modes:** Run either in a simple command-line interface or a graphical interface for easy use.
* **Error Handling:** Prevents incorrect inputs, invalid keys, and displays helpful messages.

---

## **Installation**

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd TextEncryptionTool
   ```
2. Install required dependencies:

   ```bash
   pip install cryptography
   ```
3. Run the tool:

   * **CLI mode:**

     ```bash
     python main.py
     ```

     Choose mode `[1] CLI` and follow instructions.
   * **GUI mode:**

     ```bash
     python main.py
     ```

     Choose mode `[2] GUI` and use buttons to encrypt/decrypt.

---

## **Usage**

### **Encrypting with Fernet (GUI example):**

1. Enter text in the **Text box**.
2. Select **Fernet**.
3. Click **Encrypt**.
4. Fernet key is displayed in a popup and auto-filled in the key box.
5. Encrypted text and key are automatically saved to `messages/` and `keys/`.

### **Decrypting with Fernet:**

1. Enter or load encrypted text.
2. Enter or load Fernet key.
3. Click **Decrypt** → original text is recovered.

### **Caesar Cipher:**

* Enter a numeric shift key to encrypt/decrypt messages.

---

## **Example**

**Text:** `sujan`
**Encrypted (Fernet):**

```
gAAAAABo85fG3pEgro3Q15jeXdF-p3DEKnxHWX2658CRyN8W70g4tdf0x0Vr6LqwXowLnOkzVpD_c68tapNuHYVQYcdBmk9dTg==
```

**Key:** `D0t8J0sd...` (shown after encryption)
**Decrypted:** `sujan`

---

## **Folder Structure**

```
TextEncryptionTool/
├── main.py           # Main program
├── README.md         # Project documentation
├── messages/         # Encrypted message files
├── keys/             # Encryption key files
├── requirements.txt  # Python dependencies
```


