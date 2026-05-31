# Obiettivo
Si  mostra come
* visualizzare la lista dei problemi da risolvere con il comando `list`,
* scaricare un problema.

# Lista Dettaglio
1. Per visualizzare la lista dei problemi da risolvere, si compila la seguente linea di comando:  
  ```bash
  $ rtal -s wss://ta.di.univr.it/dodm list
  ```
  * Si precisa che la parte della linea di comando `-s wss://ta.di.univr.it/dodm` permette a rtal di:
    * Collegarsi al server con -s,
    * accedendo all'indirizzo wss://ta.di.univr.it/dodm.
  * Il  risultato atteso è:
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
2. Per scaricare un problema:
  1. Ci si posiziona nella work directory $\rightarrow$ per istanza è $\sim$*/Desktop/tutorial*
      ```bash
      $ cd ~/Desktop/tutorial
      ```
  2. Si crea l'archivio *problemi* e ci si sposta dentro:
      ```bash
      $ mkdir problemi
      $ cd problemi
      ```
  3. Per istanza, si scarica il problema *sudoku*, compilando la linea di comando seguente:
      ```bash
      $ rtal -s wss://ta.di.univr.it/dodm get sudoku
      ```
      * Verifica che nella cartella corrente sia stato scaricato il file, compilando:
        ```bash
        $ ls
        ```
        Il risultato atteso è:
        ```bash
        sudoku.tar
        ```
  4. Si decomprime il file del problema scaricato e si viualizza il contenuto:
        ```bash
        tar xf sudoku.tar
        cd sudoku
        ls
        ```
        *  Si verifica che il risultato della linea di codice precedente è:
        ```bash
        README_rtal.md  README_synopsis.md  example.in.txt  example.out.txt  meta.yaml  testo_en.pdf  testo_it.pdf
        ```
        Questa lista di file rappresenta il materiale che serve a svolgere e verificare localmente il problema scaricato.
        
