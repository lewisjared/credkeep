credkeep
========

credkeep is a python package that helps ease the pain of storing sensitive credentials. Credentials that are securely
encrypted using AWS's Key Management Service (KMS) can be stored in version control systems where they cannot be
decrypted without access to a users encryption key on KMS.

Installation
============

`pip install credkeep`

Usage
=====

`credkeep` requires you to configure your own KMS master key. This key is used to encrypt/decrypt your data and is
securely stored by AWS. Your KMS master keys can be viewed at https://console.aws.amazon.com/iam/home#encryptionKeys.
For information about creating new master keys, see http://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html.

Plaintext api secrets should not be stored in plain text. For example `developer_secrets.json`

.. code-block:: javascript

    {
        "SECRET_API_KEY": "thisismysecretkey",
        "ANOTHER_API_KEY": "anotherkey"
    }

By calling `credkeep.encrypt_file`

.. code-block:: javascript

    {
      "SECRET_API_KEY": "CiAr4gKwrApZNibuqh1YKjlIGMj4A4GSHArF+0lCqBnqOxKfAQEBAgB4K+ICsKwKWTYm7qodWCo5SBjI+AOBkhwKxftJQqgZ6jsAAAB2MHQGCSqGSIb3DQEHBqBnMGUCAQAwYAYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzGyPmdgqEbxzvnjKICARCAMzOd+DIaI/rUbc8dYQTxGS8aQQNjgXPt6Or0rxo7fFn0rA5/Kf6zpnui0q9XXtUatL4D3Q==",
      "ANOTHER_API_KEY": "CiAr4gKwrApZNibuqh1YKjlIGMj4A4GSHArF+0lCqBnqOxKXAQEBAgB4K+ICsKwKWTYm7qodWCo5SBjI+AOBkhwKxftJQqgZ6jsAAABuMGwGCSqGSIb3DQEHBqBfMF0CAQAwWAYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAxgB3p/zbVarLd/5a4CARCAK4w48/dCK7EvwTDELb11bpBe8TpaIhcCalfOqACQzoLoqgciAY8DuczOvRs="
    }

This encrypted json file is safe to distribute via version control as it requires access to the master key on KMS. When
the secrets in the file are required the file can be decrypted using `credkeep.decrypt_file`. This function can optionally
set local environment variables with the decrypted secrets. These environment variables will not persist between shells
or reboots.
