FRESH_JAKFILE = u'''// For more information visit https://github.com/dispel/jak/
// Protip: Set your syntax highlighting to JavaScript.
{{
  // RECOMMENDED
  // List files to encrypt here so you can quickly encrypt/decrypt them all
  // using the "$> jak encrypt/decrypt all" commands.

  "files_to_encrypt": ["path/to/file"],

  // I created a secure 32 character password for you. You can make one yourself
  // if you want by using the "$> jak genpass" command.

  "password": "{password}"

  // You can store your password in a file INSTEAD of having a "password" value.
  // This allows you to commit the jakfile. (never commit your password!)
  // "password_file": "path/to/jakpasswordfile"
}}'''

GENPASS_RESPONSE = '''Here is your shiny new strong password.

{password}

Remember to keep this password secret and save it. Without it you will NOT be able
to decrypt any file(s) you encrypt using it.'''