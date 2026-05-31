# Obiettivi
Spiegare step-by-step come installare l'eseguibile rtal.

# Lista Dettaglio 
1. Per svolgere l'installazione, installare la Bash Shell se non presente,
2. Aprire Git Bash,
3. Appena si apre, far notare che si è posizionati nella home, segnata con il simbolo $\sim$ nell'intestazione di comando,
4. Cambiare directory posizionandoci su una cartella di riferimento.  
  Per istanza,
    * ci posizioniamo nel *Desktop* con
       ```bash
         $ cd ~/Desktop
       ```   
    * creiamo la cartella *tutorial* con
       ```bash
         $ mkdir tutorial
         $ cd tutorial
       ```
5. Per scaricare il package si va al seguente [link](https://github.com/Guilucand/rtal-algo-client/releases)
  e si scarica la propria versione che dipende dal sistema operativo del calcolatore.
6. Si copia quindi il link alla versione corretta (per istanza, consideriamo la [versione Windows](https://github.com/Guilucand/rtal-algo-client/releases/download/V1.0.1/rtal-x86_64-pc-windows-msvc.tar.gz), 
  quindi si ritorna sulla Bash Shell e si scrive:
   ```bash
   $ wget https://github.com/Guilucand/rtal-algo-client/releases/download/V1.0.1/rtal-x86_64-pc-windows-msvc.tar.gz
   ```
7. Si decomprime il file con  
   ```bash
   $ tar xf rtal-x86_64-pc-windows-msvc.tar.gz
   ```
8. Si  controlla che il file `rtal` sia presente nell'archivio *tutorial*:
   ```bash
   $ ls
   ```
   * Il risultato atteso è verificato se l'output è il seguente:
     ```bash
     rtal-x86_64-pc-windows-msvc.tar.gz
     rtal*
     ```
9. Per ultimo check, compiliamo la seguente linea di comando:
   ```bash
   $ ./rtal --version
   ```
   * Il risultato atteso è verificato se l'output è il seguente:
     ```bash
     rtal.0.2.0
     ```
   
   
