# Mostreremo come
verificare localmente il codice della soluzione scritta per un problema. Consigliamo di spendere tale verifica prima di sottomettere le proprie soluzioni al server tramite `rtal`.

# Dettaglio
1. Con la Bash Shell, portati nella cartella dove hai scaricato e decompresso l'archivio del problema di interesse (che qui assumeremo essere *conio1*):
   ```bash
   $ cd ~/Desktop/DODM/rtal/conio1
   ```
2. Assumiamo che la soluzione da testare sia scritta in python e che il file che la contiene si chiami *conio1.py* e si trovi nella cartella corrente:
   ```bash
   ~/Desktop/DODM/rtal/conio1
   ```
3. Lanciamo il seguente comando per eseguire *conio1.py*:
   ```bash
   $ python conio1.py
   ```
   Il programma non restituisce nulla in risposta a questa linea di comando,
   perché in attesa dei dati di input come previsti. All'immissione di tali dati, solitamente al completamento di ciascuna delle diverse istanze del testbed di valutazione, il programma dovrebbe stampare in output le soluzioni.
4. Nella sezione **Esempio di Input/Output** del file *testo_en.pdf* contenuto in *~/Desktop/DODM/rtal/conio1*, alla tabella **Input from 'stdin'**, sono presenti i seguenti dati:
   ```bash
   4
   98
   324
   3472
   3456789
   ```
   Qui il `4` della prima riga indica il numero di istanze, ciascuna codificata in una delle successive righe.
   Al terminale, immetti quindi le prime due righe, e attendi che il programma emetta la soluzione della prima istanza come suo output.
   Inserisci quindi le altre 3 righe/istanze una alla volta, preferibilmente dando al programma il tempo necessario per rispondere all'istanza precedente.
   In pratica, a termine del processo, sul terminale dovrebbero essere visualizzate le seguenti righe (le parentesi in realtà non sono presenti, servono solo per distinguere le righe immesse da te piuttosto che quelle ritornate dal programma testato):
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
   Specie quando le istanze dovessero trovare codifica su più righe, ti potrà convenire procedere di copia incolla (da ambiente grafico il più delle volte lo shortcut per copiare sarà Ctrl-C, ma per incollare su terminale si usa Ctrl-Shif-V; per copiare su terminale si usa Ctrl-Shif-C, in entrambi gli ambienti funziona il tasto destro del mouse) o, ancora più conveniente, utilizzare la redirezione da o verso file. Assumendo che il file input.txt contenga quelle 5 righe di input:
```bash
   $ python conio1.py < ./input.txt
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
