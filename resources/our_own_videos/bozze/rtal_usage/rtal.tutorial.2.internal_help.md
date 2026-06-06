# Obiettivi
Proporre l'uso del (sotto-)comando help per conoscere la sintassi ed argomenti dei sotto-comandi del comando `rtal`.

# Lista di Dettaglio
1. Una volta installato `rtal`, puoi eseguire la linea di comando:
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
 2. Dalla scrittura `rtal [OPTIONS] <SUBCOMMAND>` scopriamo che il corretto ordine nell'invocazione di un (sotto-)comando è quello esemplificato ora, per ottenere aiuto sul comando list:
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
Si consiglia di sperimentare col comando help per superare ogni timidezza. Si dimostra particolarmente utile nell'esplorazione del comando `connect` che presenta un più ricco set di argomenti ed opzioni.

      
    
  
