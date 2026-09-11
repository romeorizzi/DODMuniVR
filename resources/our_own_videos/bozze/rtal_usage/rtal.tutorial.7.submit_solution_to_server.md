# Mostreremo come
Sottomettere la soluzione al server per il collaudo definitivo su tutte le istanze.
* **Valutazione delle istanze**: Per ogni singola istanza del problema, il server verifica la correttezza del risultato e il rispetto dei tempi di esecuzione, assegnando un punteggio parziale.
* **Registrazione del punteggio**: Il server memorizza il punteggio totale ottenuto per ciascun problema.
* **Bonus per l'esame**: La somma dei punti accumulati nei vari problemi colloca lo studente in uno specifico scaglione di merito, a cui corrisponde un punteggio extra da sommare al voto finale dell'esame.

# Dettaglio
1. Come esempio si considera il problema *conio1*, quindi portiamoci nella cartella contenente il file della soluzione:
   ```bash
   $ cd ~/Desktop/DODM/rtal/conio1
   ```
2. Immetti la seguente linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect -f source=conio1.py conio1 -- python conio1.py
   ```
   * Il risultato atteso è:
   ```bash
   WARN Received new subtask, restarting user program...
   Received "./output/README_synopsis.md"
   Received "./output/log.txt"
   Received "./output/results.txt"
   Received "./output/README_rtal.md"
   Received "./output/results.yaml"
   Received "./output/results_with_feedback.txt"
   ```
3. Per visualizzare il contenuto del file *results.txt*, immetti la seguente linea di comando:
   ```bash
   $ less ./output/results.txt
   ```
   * Il risultato atteso contiene la lista delle valutazioni attribuite per ogni risultato
   che il codice della soluzione inviata ha calcolato, per ogni istanza del problema.
