# Mostreremo come
Ottenere validazione della nostra soluzione (con feedback immediato) dal server. Questa operazione richiede il client `rtal` e accesso alla rete.

# Dettaglio  
La filosofia è sempre quella di procedere prudentemente per passi.  
Dopo aver speso i primi test in locale (come visto al tutorial *test solution locally*), si immetta il seguente comando per far interagire la nostra soluzione in locale col server nel cloud:
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect -f source=conio1.py -a size=esempi_testo conio1 -- python conio1.py
   ```
   Con questa linea di comando, `rtal`:
   1. si connette al server `wss://ta.di.univr.it/dodm` che offre la collezione di problemi homework per il corso DODM (Discrete Optimization and Decision Making), è pertinente ricordare che questi problemi non offrono solo l'occasione di esercitarsi in modo autonomo ricevendo feedback immediato, ma producono punti bonus accolti nella valutazione sommativa a fine corso. Come vedremo sotto, questo arricchisce di argomenti il comando `rtal` da impostare a riga di comando nel terminale. Inoltre, per sottomettere soluzioni a server con ruolo valutatore oltre che feedback, è necessario essersi loggati (vedi il tutorial [rtal.tutorial.4.login.m](rtal.tutorial.4.login.m)).
   2. il flag `-f` serve per mettere un file in attachment. I file che il servizio assume di poter ricevere devo essere taggati. La tag `source` è lo slot dove inserire il file che contiene il sorgente del vostro programma che risolve il problema. I server con ruolo valutatore richiedono il riempimento di questo slot perchè il docente si riserva di attestare all'esame finale le competenze espresse con le proprie sottomissioni.   
   3. il flag `-a` serve per specificare un argomento (parametro problema-specifico che modula il comportamento del server `rtald` a fronte di una richiesta di `commit` per quel problema). L'argomento `size` serve per sintonizzare il server sulle ambizioni della sottomissione. Un problema propone diverse istanze, alcune hard-coded (come gli esempi del testo) e altre generate randomicamente ad ogni sottomissione. Ogni problema raggruppa le proprie istanze in subtask, ordinati dal più accessibile al più challenging. E' bene che il server sappia fino a quale subtask può spingersi la soluzione dello studente, e il parametro `size` serve proprio per specificare il nome del più avanzato sutask cui si mira con la presente sottomissione. Il subtask `esempi_testo` è ideale per una prima sottomissione di verifica in quanto propone esclusivamente le istanze esempio del testo, che sono facili, hard-coded, pubbliche e contenute nel file `example.in.txt` per vostra comodità. (Perchè questo argomento si chiama `size`? Un parametro rilevante nel determinare la difficoltà di un'istanza è la sua size (se ti manca questo concetto cerchiamo di chiarirlo con un esempio: considera un problema che richiede la competenza di ordinare $n$ oggetti, quì la size dell'istanza sarebbe $n$. Ordinare $n$ oggetti può essere fatto con soli $O(n log n)$ confronti, ma magari lo studente ha codificato una soluzione meno ambiziosa, di complessità computazionale $O(n^2)$. In questo caso sia lo studente che il server sprecherebbero solo tempo se lo studente sottomettesse il suo codice senza specificare un valore opportuno per il parametro opzionale `size`. Considera che per $n=1.000.000$ un algoritmo $O(n log n)$ impiegherebbe meno di un secondo mentre un algoritmo $O(n^2)$ impiegherebbe decine di minuti per darti una risposta a terminale).
   4. `conio1` è il nome del problema per il quale stiamo sottomettendo la nostra soluzione contenuta nel file sorgente `conio1.py`.
   5. se ci fermassimo qui, `rtal` prenderebbe come suo `stdin` quanto noi immettiamo da tastiera al terminale (e, oltre a visualizzarlo sul terminale, lo invierebbe al server) mentre quanto riceve dal server lo farebbe solo apparire sul nostro terminale, dove intercalerebbe le nostre immissioni da tastiera secondo il ritmo del protocollo di comunicazione previsto dal problema. Per tutti i problemi sul server dodm, non vogliamo essere noi a immettere in pochi secondi le risposte corrette per un'istanza, e quindi, con qeul `--`, chiediamo che le informazioni ricevute dal server vengano redirette al processo invocato a valle del `--`, e che l'output` di detto processo venga inviato al server. In questo modo il processo invocato a valle del `--` risolve le istanze al posto dell'umano che lo ha progettato. A valle del `--` deve essere sempre specificato qualcosa che, così invocato (solo quanto scritto a valle del `--`) al terminale, può essere eseguito (e testato) anche in isolato, in questo caso il processo specificato è l'invocazione dell'interprete Python sul file *conio1.py*. Nel loro insieme essi producono un processo che viene eseguito in locale sulla tua macchina e che `rtal` mette in comunicazione col server con un semplice gioco di redirezioni di `stdin` ed `stdout`).

In conclusione, se immetti la lunga riga di comando fornita sopra, il tuo programma viene eseguito così come visto al tutorial [rtal.tutorial.5.test_solution_locally.md](rtal.tutorial.5.test_solution_locally.md), con l'unica differenza che ora `rtal` fornisce lui l'input al tuo programma e ne ridirige l'output verso il server così che esso possa validare la tua soluzione su un set di istanze. Precisamente su tutte le istanze di tutti i subtask che non eccedano per ambizione il subtask il cui nome è specificato dall'argomento `size`. 
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
In questi file trovi il feedback espresso dal server. Puoi visualizzare ad esempio il file `results.txt` immettendo la seguente linea di comando:
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
   In questo caso hai ottenuto il codice AC (all correct) su ciascuna istanza. Ma se su alcune o tutte le istanze ottieni codici che ti segnalano che qualcosa è andato storto puoi allora ottenere maggior feedback visualizzando il file "./output/results_with_feedback.txt" che offre molte più informazioni. La nostra ambizione è quella di fornire, in piena trasparenza, un feedback completo che ti consenta di non bloccarti mai nel tuo processo di apprendimento.


## Ricorda

1. se vuoi sbirciare input ed output del tuo processo (quello invocato a valle del `--`) ti basta aggiungere il flag `-e` per ottenere echo sul terminale sia del canale di ingresso (`stdin`) che di quello di uscita (`stdout`):
   ```bash
   $ rtal -s wss://ta.di.univr.it/dodm connect  -e  -f source=conio1.py -a size=esempi_testo conio1 -- python conio1.py
   ```
2. se quanto il tuo programma deve immettere su `stdout` nel rispetto del protocollo di comunicazione stabilito dal problema non ti basta a realizzare pienamente cosa stà succedendo, puoi procedere con un print debugging arbitrariamente fine ritoccando la tua soluzione contenuta nel file `conio1.py` affinchè, nel suo procedere passo passo, riporti su `stderr` o su un qualche file le informazioni che possono aiutarti. Quanto la tua soluzione stamperà su `stderr` apparirà sul tuo terminale dove hai invocato `rtal` (con ogni sincronicità rispettata del caso ti avvali anche del meccanismo di echo, ossia del flag `-e`).


## Considerazioni finali e di contesto

All'invocazione di `rtal`, come da tutorial precedente, il set di istanze viene specificato tramite l'argomento `size` del comando `connect` (la riga di comando conteneva infatti `-a size=esempi_testo` dacchè è bene che il primissimo riscontro vada ricercato affrontando istanze già note).
Nel testo del problema si specificano vari possibili subtasks più o meno impegnativi da risolvere (vuoi perchè alcuni concentrano l'attenzione solo su casi particolari del problema, o perchè propongono istanze più grandi che richiedono soluzioni computazionalmente più efficienti per risultare sostenibili). Tali subtask sono solitamente collocati in un ordine totale di difficoltà, di cui il primo è tipicamente `esempi_testo`, e l'ultimo (il cui nome varia da problema a problema) è tipicamente il valore di default per l'argomento `size`.
Per ottenere validazione e valutazione su tutti i subtask basterà pertanto omettere l'argomento `size`. Se però la tua soluzione non può essere adeguata oltre un certo livello di difficoltà, ti conviene specificare dove per il momento si ferma la tua ambizione specificando tale livello tramite l'argomento `size`, in modo da non dover attendere tempi molto lunghi e ottenere dei feedback inutilmente dispersivi.
Questa possibilità di gradare la difficolatà viene particolarmente utile nel fare i primi test e ottenere i primi riscontri.
