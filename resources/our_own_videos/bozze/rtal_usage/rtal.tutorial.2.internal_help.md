# Obiettivi
Mostrare come il comando help può tornare utile nella comprensione e nella compilazione di `rtal`.

# Lista di Dettaglio
1. Una volta installato `rtal`, compiliamo la linea di comando:
   ```bash
   $ rtal --help
   ```
   * Il risultato atteso è:
     ```bash
      rtal 0.2.0

      USAGE:
          rtal [OPTIONS] <SUBCOMMAND>
      
      OPTIONS:
          -h, --help                       Print help information
          -s, --server-url <SERVER_URL>    Server URL [default: ws://127.0.0.1:8008/]
          -V, --version                    Print version information
      
      SUBCOMMANDS:
          connect    Connect to problem evaluator
          get        Download problem attachments
          help       Print this message or the help of the given subcommand(s)
          list       List available problems
          login
          logout
     ```
 2. Dato che l'ordine di scrittura è `rtal [OPTIONS] <SUBCOMMAND>` si compila, per istanza, la linea di comando:
    ```bash
    $ rtal help list
    ```
    * Il risultato atteso è:
      ```bash
      rtal-list
      List available problems
      
      USAGE:
          rtal list [OPTIONS] [FILTER]
      
      ARGS:
          <FILTER>    Filter problems with a regex
      
      OPTIONS:
          -h, --help       Print help information
          -v, --verbose    List services and parameters, add more than one to list more information
      ```
    
  
