#  Mostreremo come
installare l'eseguibile rtal (guida passo-passo)

# Lista Dettaglio 
1. Se sei su Windows e sei sprovvisto di Bash Shell devi installartela. Per farlo, si seguano le istruzioni della guida [How to Install Git Bash on Windows 2026](https://www.youtube.com/watch?v=hrinoukULzE)
2. Aprire Bash Shell (vai sullo Start, cerca Git Bash ed **eseguila come Amministratore**)
3. Portarsi della cartella corrente (di solito Git Bash prende avvio dalla home, indicata col simbolo $\sim$) alla cartella dove si vuole operare.  
  Ad esempio, per posizionarsi sul *Desktop*:
       ```bash
         $ cd ~/Desktop
       ```   
    * suggeriamo di crearsi quì la cartella `DODM` e la sotto-cartella `DODM/rtal` con
       ```bash
         $ mkdir -p DODM/rtal
       ```
    * si entra nella sotto-cartella con
       ```bash
         $ cd DODM/rtal
       ```
5. Per scaricare il package vai a questo [link](https://github.com/Guilucand/rtal-algo-client/releases). Scarica la versione adatta al tuo sistema operativo e calcolatore.
6. Un modo per farlo è copiare il link alla versione corretta (ad esempio la [versione Windows](https://github.com/Guilucand/rtal-algo-client/releases/download/V1.0.1/rtal-x86_64-pc-windows-msvc.tar.gz), 
  e tornare alla Bash Shell dove immettere la riga di comando:
   ```bash
   $ wget https://github.com/Guilucand/rtal-algo-client/releases/download/V1.0.1/rtal-x86_64-pc-windows-msvc.tar.gz
   ```
7. Decompri il file scaricato con  
   ```bash
   $ tar xf rtal-x86_64-pc-windows-msvc.tar.gz
   ```
8. Controlla che il file `rtal` sia presente nella sotto-cartella *rtal*:
   ```bash
   $ ls
   ```
   * Il risultato atteso è verificato se l'output è il seguente:
     ```bash
     rtal-x86_64-pc-windows-msvc.tar.gz
     rtal*
     ```
9. Si lanci la seguente linea di comando:
   ```bash
   $ ./rtal --version
   ```
   * Tutto ok se l'output è come da seguente risultato atteso:
     ```bash
     rtal.0.2.0
     ```
   
   
