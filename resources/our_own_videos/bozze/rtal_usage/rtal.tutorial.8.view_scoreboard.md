# Mostreremo come
Visualizzare un resoconto complessivo dei punti attualmente già ottenuti sui vari problemi, punteggio totale e livello attuale di bonus che concorrerà alla valutazione finale del corso (da 0 a 5 gradi di voto).

# Dettaglio
1. Apri la Bash Shell.
2. Per visualizzare il resoconto dei tuoi risultati, è necessario aver conseguito il login con successo (vedi tutorial 4).
3. Immetti la seguente linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect scoreboard
   ```
   * Il risultato atteso consiste in:
     - una tabella di risultati ottenuti per ogni ID studente e problema disponibile,
     - una seconda tabella contenente i dati riferiti al moltiplicatore di punti e la sua data di scadenza per ogni problema,
     - il dettaglio di punteggio per ogni problema sottomesso al server, conseguito dal tuo ID accademico/numero di matricola.
4. A scopo informativo, puoi scaricare il resoconto dei risultati ottenuti e registrati a server immettendo la seguente linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm get scoreboard
   ```
