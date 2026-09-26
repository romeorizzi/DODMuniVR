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
     - tabellone globale: una tabella di risultati ottenuti per ogni ID studente e problema disponibile (per visione globale e trasparenza),
     - moltiplicatori attuali: una seconda tabella contenente i dati riferiti al moltiplicatore attuale dei punti, e la sua data di scadenza per ogni problema (allo scopo di promuovere una partecipazione attiva al corso e ad un impegno da subito, quando più profiquo, sugli homework, quando sottometti la tua soluzione per un problema di homework viene archiviato un punteggio pari al prodotto del moltiplicatore attuale per il punteggio proprio dell'esercizio),
     - tuo portafoglio personale: il dettaglio dei punteggio che hai ottenuto per ogni problema sottomesso al server, come conseguito guardando alle sottomissioni migliori (su ciascun problema) effettuate dal tuo ID accademico/numero di matricola.
4. Immettendo il comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm get scoreboard
   ```
   ti viene scaricato in locale l'archivio `scoreboard.tar`, che contiene i file:
   - `multipliers.yaml`: i moltiplicatori di un problema vanno a decrescere nel tempo. Questo file contiene le varie coppie (bonus, scadenza) attualmente inserite per ciascun problema (la politica è che, per ogni problema, potremo solo posticiapare la scadenza di un certo moltiplicator o aggiunte nuove coppie, se ce lo richiedete o segnalate come opportuno).
   - `points2marks.yaml`: contiene la mappa monotona che traduce il punteggio totale (summa su tutti i problemi dei prodotti tra punti problema e massimo moltiplicatore attivo sul problema all'atto della sottomissione).

[video del tutorial](https://youtu.be/5-o9OqZCBPU)