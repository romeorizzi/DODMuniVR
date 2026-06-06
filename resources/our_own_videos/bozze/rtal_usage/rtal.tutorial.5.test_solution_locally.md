# Obiettivi
Si illustra come verificare il codice della soluzione scritta per un determinato problema.
Per istanza, il problema è conio1.

# Lista Dettaglio  
1. Per istanza, con la Bash Shell, 
  ci si sposta nella cartella dove abb scaricato e decompresso l'archivio *conio1* contenente i dati per risolvere il problema nella seguente directory: 
  ```bash
  $ cd ~/Desktop/tutorial/problemi/conio1
  ```
2. Il file python che contiene la soluzione si chiama *conio1.py* ed è inserito nella workdirectory seguente:
  ```bash
  ~/Desktop/tutorial/problemi/conio1
  ```
3. Avviamo il seguente comando per compilare *conio1.py*:
  ```bash
  $ python conio1.py
  ```
  Il file non restituisce nulla in risposta a questa ultima linea di comando, 
  perché sta attendendo che vengano inseriti a mano le istanze del problema, ossia i dati che serveno a calcolare le diverse soluzioni richieste in output.
4. Alla tabella **Imput from 'stdin'**, nella sezione **Esempio di Input/Output** 
  del file *testo_en.pdf* contenuto in *~/Desktop/tutorial/problemi/conio1* sono presenti i seguenti dati:  
  ```bash
  4
  98
  324
  3472
  3456789
  ```
  Si inseriscono questi numeri in seguenza, premendo Enter tra il numero precedente e quello successivo.
  In questo modo,, il programma simula le soluzioni passo-passo.  
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
5. Per automatizzare questo procedimento si inserisce la seguente riga di comando:
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
6. Per visualizzare i risultati i risultati ottenuti dal server, si compila la linea di comando seguente:
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
     
