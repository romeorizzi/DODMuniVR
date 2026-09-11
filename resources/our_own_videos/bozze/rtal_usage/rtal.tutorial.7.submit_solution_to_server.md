# Mostreremo come
Sottomettere la soluzione al server per una sua validazione (e valutazione) su set più o meno estesi di istanze.

## Inquadramento di massima (considerazioni di contesto)
All'invocazione di `rtal`, come da tutorial precedente, il set di istanze viene specificato tramite l'argomento `size` del comando `connect` (la riga di comando conteneva infatti `-a size=esempi_testo` dacchè è bene che il primissimo riscontro vada ricercato affrontando istanze già note).
Nel testo del problema si specificano vari possibili subtasks più o meno impegnativi da risolvere (vuoi perchè alcuni concentrano l'attenzione solo su casi particolari del problema, o perchè propongono istanze più grandi che richiedono soluzioni computazionalmente più efficienti per risultare sostenibili). Tali subtask sono solitamente collocati in un ordine totale di difficoltà, di cui il primo è tipicamente `esempi_testo`, e l'ultimo (il cui nome varia da problema a problema) è tipicamente il valore di default per l'argomento `size`.
Per ottenere validazione e valutazione su tutti i subtask basterà pertanto omettere l'argomento `size`. Se però la tua soluzione non può essere adeguata oltre un certo livello di difficoltà, ti conviene specificare dove per il momento si ferma la tua ambizione specificando tale livello tramite l'argomento `size`, in modo da non dover attendere tempi molto lunghi e ottenere dei feedback inutilmente dispersivi.
Questa possibilità di gradare la difficolatà viene particolarmente utile nel fare i primi test e ottenere i primi riscontri.

## Tieni presente che
Per ogni problema, puoi sottomettere quante volte vuoi e, se il problema è oggetto anche di valutazione, ti verrà tenuto buono il punteggio più alto mai ottenuto da una tua sottomissione.** 


* **Valutazione delle istanze**: Per ogni singola istanza del problema, il server verifica la correttezza del risultato e il rispetto dei tempi di esecuzione, assegnando un punteggio parziale.
* **Registrazione del punteggio**: Il server memorizza ogni sottomissione e relativo punteggio.
* **Scoreboard**: In ogni momento puoi chiedere al server un report del tuo punteggio attuale su tutti i problemi. (Il prossimo tutorial ti mostra come invocare questo servizio.)
* **Bonus per l'esame**: La somma dei punti accumulati sui vari problemi colloca lo studente in uno specifico scaglione di merito, a cui corrisponde un punteggio extra da sommare al voto finale dell'esame.

## Dettaglio
1. Come esempio si considera il problema *conio1*, il cui imo subtask si chiama `extra_large`.
   Portati nella cartella contenente il file della soluzione:
   ```bash
   $ cd ~/Desktop/DODM/rtal/conio1
   ```
2. Immetti la seguente riga di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect -a size=extra_large  -f source=conio1.py conio1 -- python conio1.py
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
   *Nota: più pratico e meno error-prone se hai la soluzione completa al problema*, la seguente riga avrebbe prodotto lo stesso identico effetto:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect -f source=conio1.py conio1 -- python conio1.py
   
3. Per visualizzare il contenuto del file *results.txt*, immetti la seguente linea di comando:
   ```bash
   $ less ./output/results.txt
   ```
   * Il risultato atteso contiene la lista delle valutazioni attribuite per ogni risultato
   che il codice della soluzione inviata ha calcolato, per ogni istanza del problema.
