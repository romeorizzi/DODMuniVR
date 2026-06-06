# Mostreremo come
* visualizzare la lista dei problemi di una collection col comando `list`,
* scaricarsi i materiali pubblici di un problema.

# Dettaglio
Una sintassi base del comando `list` sarebbe:
  ```bash
  $ rtal -s <URL-collection-problemi> list
  ```
Per il corso DODM, la collection per gli homework si trova all'URL `wss://ta.di.univr.it/dodm` che va quindi specificato come argomento server (`-s`):
  ```bash
  $ rtal -s wss://ta.di.univr.it/dodm list
  ```
Il  risultato atteso è una lista di problemi, del tipo:
  ```bash
    - borse
    - conio1
    - conio3
    - first_PD
    - first_non_local_PD
    - lis
    - piastrelle10
    - project
    - scoreboard
    - shortest_paths
    - sudoku
    - triangolo
  ```
    _Nota:_ la lista dei problemi proposti come homework tende ad allungarsi entro uno stesso anno accademico.
    
Per scaricare un problema della lista posizionati nella cartella scelta come cartella padre per i folder dei vari problemi affrontati:
  ```bash
      $ cd ~/Desktop/DODM/rtal
  ```
e poi, se a titolo di esempio vuoi scaricare il problema *conio1*, immetti il comando:
  ```bash
      $ rtal -s wss://ta.di.univr.it/dodm get conio1
  ```
Verifica che il file `conio1.tar` appaia ora nella lista dei file presenti nel folder corrente; lista che puoi ottenere col comando:
  ```bash
        ls
  ```
Decomprimi/espandi l'archivio  `conio1.tar` con:
  ```bash
        tar xf conio1.tar
  ```
Visualizzane il contenuto con:
  ```bash
        cd conio1
        ls
  ```
L'output sulla shell al comando precedente comando dovrebbe essere qualcosa di simile a:
  ```bash
        README_rtal.md       conio1_template_gurobi.py*  meta.yaml
        README_synopsis.md   example.in.txt              testo_en.pdf
        conio1_template.py*  example.out.txt             testo_it.pdf
  ```
Questi file sono tutto il materiale che ti serve per poter svolgere e verificare localmente il problema scaricato.
        
