# Obiettivo
Si illustra come si visualizzano i risultati raccolti per ogni soluzione sottomessa e poi registrata al server, 
per permettere allo studente di ottenere un resocondo del proprio andamente e quantificare i punti che sta accumulando 
in aggiunta alla propria valutazione finale del corso di studio.

# Lista Dettaglio  
1. Si apre la Bash Shell,
2. Per visualizzare il resoconto dei propri risultati, è necessario aver conseguito il Login con successo,
3. Si compila la seguente riga di comando:
  ```bash
  $ rtal -s wss://ta.di.univr.it/dodm connect scoreboard
  ```
  *  Il risultato atteso consiste in:
      - una Tabella di risultati ottenuti per ogni ID studente e Problema Disponibile,
      - una seconda Tabella contente i dati riferiti al moltiplicato di punti e la sua data si scadenza per ogni problema,
      - Il dettaglio di punteggio per ogni problema sottomesso al server, conseguito dal proprio ID accademico/Numero di matricola.
  * A scopo informativo, è disponibile la possibilità scaricare il resoconto dei risultati ottenuti e regitrati a server
    compilando la seguente linea di comando: 
    ```bash
    $ rtal -s wss://ta.di.univr.it/dodm get scoreboard
    ```
    
