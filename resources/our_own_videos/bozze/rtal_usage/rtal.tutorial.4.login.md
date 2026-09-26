# Mostreremo come autenticarsi al server con le proprie credenziali accademiche.
L'autenticazione è richiesta da quei server il cui ruolo non è solo quello di fornire un feedback immediato utile all'acquisizione autonoma di competenze ma anche contribuire alla valutazione sommativa di un corso. Nel caso del server `dodm` (che gestisce la collection di problemi presenti come homework per il corso di Discrete OPtimization and Decision Making), siccome vengono prodotti punteggi spendibili nella valutazione del profitto finale nel corso è richiesto effettuare un login. E' un operazione semplice che basta fare una volta sola (per computer), ma se il computer non è tuo ti converrà poi fare logout al termine del suo utilizzo. 


## Dettaglio  
1. Per autenticarti, immetti il seguente comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm login
   ```
   * Il risultato atteso è il seguente prompt:
    ```bash
    Matricola:
    ```
2. Inserisci al prompt la tua matricola universitaria personale (che per l'Università di Verona avrà il formato VR??????), per esempio:
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
     
## Fare logout

Se il computer è tuo puoi probabilmente evitarti di fare logout (e poi dover rifare login ogni volta), avere il login attivo significa solo avere un cookie passivo che non ha alcun effetto nè alcun dispendio eneregetico.
L'unico motivo di fare logout è per evitare il rischio che qualcuno sottometta delle soluzioni a nome tuo che poi saresti in difficoltà a spiegare in sede di esame finale.

In ogni caso anche questa è un'operazione estremamente semplice da compiere, ti basta immettere un'unica riga di comando:

   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm logout
   ```
