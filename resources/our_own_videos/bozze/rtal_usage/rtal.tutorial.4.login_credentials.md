# Mostreremo come
autenticarsi al server con le proprie credenziali accademiche.
L'autenticazione è richiesta per quelle collection di problemi dove il server produce punteggi spendibili nella valutazione del profitto finale nel corso.

# Dettaglio  
1. Per autenticarti, immetti il seguente comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm login
   ```
   * Il risultato atteso è il seguente prompt:
    ```bash
    Matricola:
    ```
2. Inserisci al prompt la tua matricola universitaria personale (VR??????), per esempio:
   `VR123456`
   e premi Enter/Invio sulla tastiera.
   * Il risultato atteso è:
    ```bash
    Complete the authentication at the following URL: https://ta.di.univr.it/matricola-VR123456&authKey...
    ```
3. Clicca sul link premendo **Ctrl + tasto sx del mouse** (oppure copia-incolla l'URL in un browser),
4. Si apre nel browser la finestra di LogIn del portale accademico, dove dovrai effettuare login con le tue credenziali GIA.
5. Una volta apparsa la schermata di conferma di LogIn, chiudi la finestra del browser.
6. Per verificare che il login è operativo alla Bash Shell ed `rtal`, rilancia la linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm login
   ```
   * Il risultato atteso è:
     ```bash
     ERROR Already authenticated, run `rtal logout` to remove the authentication data and retry
     ```
     
