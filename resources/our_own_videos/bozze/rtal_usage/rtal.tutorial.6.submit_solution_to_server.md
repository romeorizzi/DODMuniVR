# Obiettivo
Testare il più ampio range di soluzioni disponibili (oltre a quelle fornite negli esempi di testo) e registrazione del risultato a livello ufficiale 
(la somma dei risultati della soluzione svolte per ogni problema affrontato, aiuterò lo studente ad accumulare punti aggiuntivi alla valutazione finale del corso).

# Lista Dettaglio
1. Per istanza si considera il problema *conio1* e ci si sposta nell'archivio contenente il file della soluzione.
   Seguendo il procedimento illustrato nelle lezioni precedenti si compila la seguente linea di comando:
    ```bash
    $ cd ~/Desktop/tutorial/problemi/conio1
    ```
3. Si apre la Bash Shell e si lanciano le seguenti righe di comando:
  ```bash
  $ rtal - s wss:/ta.di.univr.it/dodm connect -f sources=conio1.py conio1 -- python conio1.py
  ```
  * Il  risultato atteso è:
  ```bash
  WARN Received new subtask, restarting user program...
  Received "./output/README_synopsis.md"
  Received "./output/log.txt"
  Received "./output/results.txt"
  Received "./output/README_rtal.md"
  Received "./output/results.yaml"
  Received "./output/results_with_feedback.txt"
  ```
4. Visualizziamo il contenuto del file *./output/results.txt* inviando la seguente linea di comando:
  ```bash
  $ less ./output/results.txt
  ```
  * Il risultato atteso contiene la lista delle valutazioni attribuite per ogni risultato 
  che il codice della soluzione inviata ha calcolato, per ogni istanza del problema.
   
