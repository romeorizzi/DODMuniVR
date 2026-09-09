# Mostreremo come
far verificare il codice della soluzione al server. Questa operazione necessita di accesso alla rete e del client `rtal`.

# Dettaglio
La filosofia è sempre quella di proocedere prudentemente per passi. Pertanto, dopo aver speso i primi test in locale, si effettuerà una prima sottomissione al server restringendo l'attenzione alle sole istanze del testo
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
