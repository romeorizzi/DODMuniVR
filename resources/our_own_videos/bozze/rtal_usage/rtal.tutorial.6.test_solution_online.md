# Mostreremo come
Ottenere validazione della nostra soluzione (con feedback immediato) dal server. Questa operazione richiede il client `rtal` e accesso alla rete.

# Dettaglio  
La filosofia è sempre quella di procedere prudentemente per passi.  
Dopo aver speso i primi test in locale (come visto al tutorial *test solution locally*), si immetta il seguente comando per far interagire la nostra soluzione in locale col server nel cloud:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect -f source=conio1.py -a size=esempi_testo conio1 -- python conio1.py
   ```
   Con questa linea di comando `rtal`:
   1. si connette al server,
   2. riceve dal server l'input per i soli esempi nel testo del problema *conio1* e li trasmette come standard input al processo specificato a valle del `--`,
   3. quindi: a valle del `--` deve essere sempre specificato qualcosa che può essere eseguito (e testato) anche in isolato, in questo caso il processo specificato è l'invocazione dell'interprete Python sul file *conio1.py* (entrambi residenti sulla tua macchina). Il tuo programma viene pertanto eseguito così come visto al tutorial *test solution locally*, con l'unica differenza che ora `rtal` fornisce lui l'input al tuo programma e ne ridirige l'output verso il server così che esso possa validare la tua soluzione su un set di istanze.
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
6. In questi file trovi il feedback espresso dal server. Puoi visualizzare ad esempio il file `results.txt` immettendo la seguente linea di comando:
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
7. se vuoi sbirciare input ed output del tuo processo (quello invocato a valle del `--`) ti basta aggiungere il flag `-e` per ottenere echo sul terminale sia del canale di ingresso (`stdin`) che di quello di uscita (`stdout`):
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect  -e  -f source=conio1.py -a size=esempi_testo conio1 -- python conio1.py
   ```
8. se quanto il tuo programma deve immettere su `stdout` nel rispetto del protocollo di comunicazione stabilito dal problema non ti basta a realizzare pienamente cosa stà succedendo, puoi procedere con un print debugging arbitrariamente fine ritoccando la tua soluzione contenuta nel file `conio1.py` affinchè, nel suo procedere passo passo, riporti su `stderr` o su un qualche file le informazioni che possono aiutarti. Quanto la tua soluzione stamperà su `stderr` apparirà sul tuo terminale dove hai invocato `rtal` (con ogni sincronicità rispettata del caso ti avvali anche del meccanismo di echo, ossia del flag `-e`).


## Considerazioni finali e di contesto

All'invocazione di `rtal`, come da tutorial precedente, il set di istanze viene specificato tramite l'argomento `size` del comando `connect` (la riga di comando conteneva infatti `-a size=esempi_testo` dacchè è bene che il primissimo riscontro vada ricercato affrontando istanze già note).
Nel testo del problema si specificano vari possibili subtasks più o meno impegnativi da risolvere (vuoi perchè alcuni concentrano l'attenzione solo su casi particolari del problema, o perchè propongono istanze più grandi che richiedono soluzioni computazionalmente più efficienti per risultare sostenibili). Tali subtask sono solitamente collocati in un ordine totale di difficoltà, di cui il primo è tipicamente `esempi_testo`, e l'ultimo (il cui nome varia da problema a problema) è tipicamente il valore di default per l'argomento `size`.
Per ottenere validazione e valutazione su tutti i subtask basterà pertanto omettere l'argomento `size`. Se però la tua soluzione non può essere adeguata oltre un certo livello di difficoltà, ti conviene specificare dove per il momento si ferma la tua ambizione specificando tale livello tramite l'argomento `size`, in modo da non dover attendere tempi molto lunghi e ottenere dei feedback inutilmente dispersivi.
Questa possibilità di gradare la difficolatà viene particolarmente utile nel fare i primi test e ottenere i primi riscontri.
