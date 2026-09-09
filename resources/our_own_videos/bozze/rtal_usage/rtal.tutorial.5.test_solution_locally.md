# Mostreremo come
verificare localmente il codice della soluzione scritta per un problema. Come esempio, si considera il problema *conio1*.

# Lista Dettaglio  
1. Per istanza, con la Bash Shell, 
  ci si sposta nella cartella dove abbiamo scaricato e decompresso l'archivio *conio1* contenente i dati per risolvere il problema nella seguente directory: 
  ```bash
  $ cd ~/Desktop/DODM/rtal/conio1
  ```
2. Il file python che contiene la soluzione si chiama *conio1.py* ed è inserito dall* studente nella work directory seguente:
  ```bash
  ~/Desktop/DODM/rtal/conio1
  ```
3. Avviamo il seguente comando per eseguire il programma *conio1.py*:
  ```bash
  $ python conio1.py
  ```
  A prima occhiata, il file non restituisce nulla in risposta a questa ultima linea di comando, 
  perché sta attendendo che vengano inseriti a mano le istanze del problema, ossia i dati che serveno a calcolare le diverse soluzioni richieste in output.  
4. Alla tabella **Input from 'stdin'**, nella sezione **Esempio di Input/Output** 
  del file *testo_en.pdf* contenuto in *~/Desktop/DODM/rtal/conio1* sono presenti i seguenti dati:  
  ```bash
  4
  98
  324
  3472
  3456789
  ```
  Quindi si inseriscono in interfaccia Bash Shell questi numeri in seguenza, premendo Enter tra il numero precedente e quello successivo.
  In questo modo, il programma registra gli input e calcola le soluzioni passo-passo.  
  * Il risultato atteso è il seguente $\rightarrow$ tra $\(\)$ i numeri inseriti a scopo didattico:
  ```bash
  (4)
  (98)
  6
  1 1 1 0 2 1 0 0 0 0
  (324)
  5
  0 3 0 0 2 0 2 2 0 0
  (3472)
  8
  0 1 0 0 1 1 0 2 0 3
  (3456789)
  3464
  0 2 1 1 1 1 0 1 1 3456
  ```
### Automatizzazione
1. Per automatizzare questo procedimento si inserisce la seguente riga di comando:
  ```bash
  $ rtal -s wss://ta.di.univr.it/dodm connect -f source=conio.py -a size=esempi_testo conio1 -- python conio1.py
  ```
  Con questa linea di comano rtal 
  1. si connette al server,
  2. si collega all'input posto in esempi_testo per il problema conio1,
  3. richiama il python globale della nostra macchina e il file *conio1.py* che deve essere compilato.
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
7. Per visualizzare i risultati i risultati ottenuti dal server, si compila la linea di comando seguente:
  ```bash
  $ less ./output/results.txt
  ```
  * Il risultato atteso, se la soluzione è corretta, è:
    ```bash
    Subtask 1 (4 testcases):
    Case #001 [esempi_testo - hardcoded]: AC (0.500 secs/1.000 secs) All correct (got 2/2 points)
    Case #002 [esempi_testo - hardcoded]: AC (0.010 secs/1.000 secs) All correct (got 2/2 points)
    Case #003 [esempi_testo - hardcoded]: AC (0.008 secs/1.000 secs) All correct (got 2/2 points)
    Case #004 [esempi_testo - hardcoded]: AC (0.010 secs/1.000 secs) All correct (got 2/2 points)
    ```
     
# Dettaglio
1. Con la Bash Shell, portati nella cartella dove hai scaricato e decompresso l'archivio *conio1*:
   ```bash
   $ cd ~/Desktop/DODM/rtal/conio1
   ```
2. Il file Python che contiene la soluzione si chiama *conio1.py* e si trova nella cartella corrente:
   ```bash
   ~/Desktop/DODM/rtal/conio1
   ```
3. Lancia il seguente comando per eseguire *conio1.py*:
   ```bash
   $ python conio1.py
   ```
   Il programma non restituisce nulla in risposta a questa linea di comando,
   perché sta attendendo che vengano inseriti a mano le istanze del problema, ossia i dati che servono a calcolare le diverse soluzioni richieste in output.
4. Nella sezione **Esempio di Input/Output** del file *testo_en.pdf* contenuto in *~/Desktop/DODM/rtal/conio1*, alla tabella **Input from 'stdin'**, sono presenti i seguenti dati:
   ```bash
   4
   98
   324
   3472
   3456789
   ```
   Inserisci questi numeri in sequenza, premendo Enter tra un numero e il successivo.
   In questo modo, il programma simula le soluzioni passo-passo.
   * Il risultato atteso è il seguente (tra parentesi i numeri inseriti a scopo didattico):
   ```bash
   (4)
   (98)
   6
   1 1 1 0 2 1 0 0 0 0
   (324)
   5
   0 3 0 0 2 0 2 2 0 0
   (3472)
   8
   0 1 0 0 1 1 0 2 0 3
   (3456789)
   3464
   0 2 1 1 1 1 0 1 1 3456
   ```
5. Per automatizzare questo procedimento immetti la seguente linea di comando:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect -f source=conio1.py -a size=esempi_testo conio1 -- python conio1.py
   ```
   Con questa linea di comando `rtal`:
   1. si connette al server,
   2. si collega all'input posto in *esempi_testo* per il problema *conio1*,
   3. richiama il Python globale della tua macchina e il file *conio1.py* che deve essere eseguito.
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
6. Per visualizzare i risultati ottenuti dal server, immetti la seguente linea di comando:
   ```bash
   $ less ./output/results.txt
   ```
   * Il risultato atteso, se la soluzione è corretta, è:
     ```bash
     Subtask 1 (4 testcases):
     Case #001 [esempi_testo - hardcoded]: AC (0.500 secs/1.000 secs) All correct (got 2/2 points)
     Case #002 [esempi_testo - hardcoded]: AC (0.010 secs/1.000 secs) All correct (got 2/2 points)
     Case #003 [esempi_testo - hardcoded]: AC (0.008 secs/1.000 secs) All correct (got 2/2 points)
     Case #004 [esempi_testo - hardcoded]: AC (0.010 secs/1.000 secs) All correct (got 2/2 points)
     ```
