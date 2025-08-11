# FUTURE_CS_03
A repository on a secured file upload system


File Upload Portal with AES Encryption

This project is a secure file upload portal built using Python Flask for the backend, WTForms for form handling, cryptography for AES encryption, and werkzeug.utils for file management. The system ensures files are encrypted at rest and securely transmitted in transit.


Features

File Upload Interface – Simple and user friendly form built with WTForms.

AES Encryption – Files are encrypted using the cryptography library before being stored on the server.

Secure Transmission – Data is sent securely to the server, ensuring confidentiality in transit.

File Handling with werkzeug.utils – Ensures safe file saving and prevents unsafe filenames.


How It Works

1. Upload Stage

User selects a file and submits it via a Flask based web form powered by WTForms.

Form validation ensures only allowed file types are processed.



2. Encryption Stage

The server generates an AES encryption key.

The uploaded file’s contents are encrypted using AES from the cryptography library.

The encrypted file is saved to the server’s storage.



3. Storage & Retrieval

Only the encrypted version of the file is stored (encrypted at rest).

A decryption function (using the same AES key) is available to retrieve and view the file in its original form


Technologies Used

Python Flask – Lightweight backend framework for handling requests and routing.

WTForms – For secure, validated form handling in the upload interface.

cryptography – For AES encryption and secure key generation/management.

werkzeug.utils – For secure and reliable file handling.

