# Mostreremo
Come autenticarsi al server con le proprie credenziali accademiche.
L'autenticazione è richiesta per quelle collection di problemi dove il server produce punteggi spendibili nella valutazione del profitto finale nel corso.

# Lista Dettaglio  
1. Inserire la seguente linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm login
   ```
   * Il risultato atteso è:
    ```bash
    Matricola:
    ```
2. Inserisci la tua matricola universitaria personale (VR??????), per esempio:
   `VR123456`
   e premi Enter/Invio sulla tastiera.
   * Il risultato atteso è:
    ```bash
    Complete the authentication at the following URL: https://ta.di.univr.it/matricola-VR123456&authKey...
    ```
3. Clicca sul link premendo **Ctrl + tasto sx del mouse** (oppure copia-incolla l'URL in un browser),
4. Si apre la finestra di LogIn del portale accademico, dove dovrai effettuare login con le tue credenziali GIA.
5. Chiudi la finestra di conferma di LogIn.
6. Per verificare se il login è stato confermato dalla Bash Shell, rilancia la linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm login
   ```
   * Il risultato atteso è:
     ```bash
     ERROR Already authenticated, run `rtal logout` to remove the authentication data and retry
     ```
     
