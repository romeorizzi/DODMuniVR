# Obiettivo
Mostrare come
* visualizzare la lista dei problemi di una collection col comando `list`,
* scaricarsi i materiali pubblici di un problema.

# Lista Dettaglio
La sintassi sarebbe:
  ```bash
  $ rtal -s <URL-collection-problemi>
  ```
Per il corso DODM, la collection per gli homework si trova all'URL `wss://ta.di.univr.it/dodm` che va quindi specificato come argomento server (`-s`):
  ```bash
  $ rtal -s wss://ta.di.univr.it/dodm list
  ```
  * Il  risultato atteso è una lista di problemi, del tipo:
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
2. Per scaricare un problema:
  1. Posizionati nella directory che si è scelta come cartella padre per le cartelle dei vari problemi affrontati:
      ```bash
      $ cd ~/Desktop/DODM/rtal
      ```
  2. A titolo di esempio, per scaricare il problema *conio1*, il comando è il seguente:
      ```bash
      $ rtal -s wss://ta.di.univr.it/dodm get conio1
      ```
      * Verifica che nella cartella corrente sia stato scaricato il file di archivio:
        ```bash
        $ ls
        ```
        Il risultato atteso è:
        ```bash
        conio1.tar
        ```
  4. Decomprimi/espandi l'archivio del problema scaricato e visualizza il contenuto:
        ```bash
        tar xf conio1.tar
        cd conio1
        ls
        ```
        *  Verifica che il risultato della linea di comando precedente sia qualcosa di simile a:
        ```bash
        README_rtal.md       conio1_template_gurobi.py*  meta.yaml
        README_synopsis.md   example.in.txt              testo_en.pdf
        conio1_template.py*  example.out.txt             testo_it.pdf
        ```
        Questa lista di file rappresenta il materiale che serve a svolgere e verificare localmente il problema scaricato.
        
