<a id ="up"></a>
<p align="center">
<img src="assets/banner.png">
<img src="https://img.shields.io/badge/PyShield-v2.0.1.5-blue?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white">
<img src="https://img.shields.io/badge/tests-100/100-76B900?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/build-passing-76B900?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/code quality-A-76B900?style=for-the-badge&logo=&logoColor=whit">
<img src="https://img.shields.io/badge/license-GPL3.0-blue?style=for-the-badge&logo=&logoColor=whit">
</p>

---
### 🛡Py-Shield🛡
Tool/Library for Python used to obfuscate and protect your code from decompilation, reverse debug, etc. Also, can prevent detection by antiviruses.

---
### 💻Supported Platforms💻

- Python 3
- Windows
- Various Linux distributions
- Mac OS

---
### 🔧Main Features🔧
> **Hash strings**
> - Hashing all strings in piece of code. It replaces all strings with their hash.
> - Protects strings context.

> **Looping obfuscation**
> - Encrypting piece of code using base64 and zlib for N times.
> - Best way to decrease/prevent antiviruses detection.

> **AES encryption**
> - Encrypting piece of code using AES 256 encryption algorithm.
> - One of two nice ways to protect code from deobfuscation.

> **Fernet encryption**
> - Encrypting piece of code using Fernet encryption algorithm.
> - One of two nice ways to protect code from deobfuscation.
---

### 🏁Quick start🏁
1. Clone repo
    ```
    git clone https://github.com/ByteCorum/Py-Shield.git
    ```
2. Install requirements
   ```
   pip install -r requirements.txt
   ```
3. More info
   ```
   py-shield --help
   ```
4. Example
    ```
    py-shield --mode hashstr;crypt;looping;aes --loops 3 main.py
    ```
5. Output
   ```
   from PyShield.script_67158430 import PyShield
   PyShield(__file__, b'x\x9c\x05\xc1I\xa2C0\x00\x00\xd0\x03Y\x18\xf0Q\xc4\\;TEM\r...')
   ```
6. Example legacy
    ```
    py-shield-legacy --loops 3 --mode 2 --file main.py
    ```
7. Output legacy
   ```
   _=lambda __:__import__('zlib').decompress(__import__('cryptography.fernet').fernet.Fernet(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[1]).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[0])[::-1]);exec((_)(b'x\x9c\x15\x...')
   ```

---

### 📜Additional Info📜
> [!NOTE]  
> Obfuscation tool has 2 major versions legacy and global. This repo includes both of them, but we highly recommend you to use the global version, cut it much securer. Anyway, we won't end support of legacy version, so if u have issues, let us know.

> [!TIP]
> We highly recommend compiling obfuscated script using Nuitka. Use `--follow imports` while obfuscating to tell Nuitka what to import
---

### 📲Contacts

<a href="https://github.com/ByteCorum"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
   <a href="https://discordapp.com/users/798503509522645012"><img src="https://img.shields.io/badge/Discord-003E54?style=for-the-badge&logo=Discord&logoColor=white"></a>
---

[⬆go up⬆](#up)
