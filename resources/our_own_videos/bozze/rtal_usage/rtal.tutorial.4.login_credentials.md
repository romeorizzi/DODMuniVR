# Obiettivo
Illustrare come registrarsi al server utilizzando le proprie credenziali accademiche.
La registrazione ha l'obiettivo di attivare la partecipazione dello studente alle esercitazioni,
permettendo di accumulare punti aggiuntivi alla valutazione finale del corso.

# Lista Dettaglio  
1. Inserire la seguente linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm login
   ```
   * Il risultato atteso è:
    ```bash
    Matricola:
    ```
2. Inserire l'ID universitario personale, per esempio:
   `VR123456`
   e si preme Enter sulla tastiera.
   * Il risultato atteso è:
    ```bash
    Complete the authentication at the following URL: https://ta.di.univr.it/matricola-VR123456&authKey...
    ```
3. Si clicca sul link premendo **Ctrl + tasto sx del mouse**,
4. Si apre la finestra di LogIn del portale accademico, quindi si svolge il proprio login.
5. Si chiude la finestra di conferma di LogIn.
6. Per verificare se il login è stato confermato dalla Bash Shell, si compila la seguente linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm login
   ```
   * Il risultato atteso è:
     ```bash
     ERROR Already authenticated, run `rtal logout` to remove the authentication data and retry
     ```
     
