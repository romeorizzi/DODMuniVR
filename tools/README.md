#  ⚙ Work tools, the TALight platform

The course offers a body of theoretical tools but also a set of practical competences. These are not only assessed but also trained and fostered through a set of didactical  problems that the students are asked to solve during the course (proposed as homework or project). Some of these problems will ask you to design an algorithm and others will ask you to just model the problem in terms of either LP (Linear Programming) or ILP (Integer Linear Programming).
In either case, the product of your work takes the form of a real code with the general understanding that, running your code/machine on a generic instance of the problem, a solution for the generic instance of the assigned problem is automatically obtained.
You have the freedom to compose your code in the language of your choice, but as first choice we advise python since this will also be the language we will stick to in our examples to the class (by virtue of the fact that it can be readily grasped also by a novice). Also, as LP or ILP solvers our choice is to rest on Gurobi because it offers a practical and powerful (state of the art) option (also, Gurobi offers a community and rich didactic tutorials and other materials).

From now on, by "solution" we mean the machine you have assembled: it automatically yields a solution to any instance of the problem one submits to it.
With this, you will be put in the conditions not only to train and exhibit quite practical and concrete competences, but also to get automatic and immidiate evaluation and/or feedback on your work.


## ⚙ Our TALight platform and the `rtal` client

Our TALight platform will be the framework offering all these services. We come from our own experience in competitive programming (in particular with the Oii and the iOi) but our TALight platform is designed having in mind the didactic needs for a course like ours.
In particular, it is meant to offer more transparent and detailed contextual feedback.

TALight is based on two programs that are put in communication: `rtald` is run on our servers and proposes instances of the problems it servers, `rtal` runs on your machine and allows you or your code to receive these instances and return your answers for them to the server for evaluation and feedback (put in jargon: TALight has a client/server architecture where `rtal` is the client running on your machine and interacting with you or your solution while connected to the daemon `rtald` running on our servers and offering the evaluation and feedback services).

Since the TALight platform is intended for teaching rather than for competitions, it allows you to monitor what your program is doing: just print to `stderr` rather than to `stdout` to print on your monitor rather than sending to the server (useful also for print debugging). Hence, `stdout` and `stdin` are the two channels reserved for the two-ways communication with the server. We also try to give you timely feedback as soon as your program provides invalid answers (solutions that are not admissible, or not optimal). However, the server may immediately close the channel and drop your service request as soon as your solution badly violates the communication protocol as intended for the particular problem at hand.

In conclusion, you need to install on your machine and learn how to use our client `rtal`. Helping you with this is the goal of this `README.md` file.

---
# ⚙ 💻 Installation and Usage Guide for `rtal`

Install now and start using `rtal` right away. You will need it for the exercises, homework, and lab calls of the course.

- [⚙ Work tools, the TALight platform](#-work-tools-the-talight-platform)
  - [⚙ Our TALight platform and the `rtal` client](#-our-talight-platform-and-the-rtal-client)
- [⚙ 💻 Installation and Usage Guide for `rtal`](#--installation-and-usage-guide-for-rtal)
  - [How to get a Bash Shell](#how-to-get-a-bash-shell)
  - [How to get the `rtal` client](#how-to-get-the-rtal-client)
  - [Verify that `rtal` is installed correctly and check its version](#verify-that-rtal-is-installed-correctly-and-check-its-version)
  - [The internal help (`rtal help`)](#the-internal-help-rtal-help)
  - [Authentication and login (`rtal login`)](#authentication-and-login-rtal-login)
  - [See the list of problems currently in the collection (`rtal list`)](#see-the-list-of-problems-currently-in-the-collection-rtal-list)
  - [Download the text and the other public materials of a problem (`rtal get`)](#download-the-text-and-the-other-public-materials-of-a-problem-rtal-get)
  - [To view the active services for a problem](#to-view-the-active-services-for-a-problem)
  - [Get explanations on a service and the use of its optional arguments](#get-explanations-on-a-service-and-the-use-of-its-optional-arguments)
  - [Submit your solution or avail of other services offered for a problem (`rtal connect`)](#submit-your-solution-or-avail-of-other-services-offered-for-a-problem-rtal-connect)

Our guide here is complemented by a [Playlist of videos on YouTube](https://www.youtube.com/playlist?list=PLZ6q66pQKGuKzoqBzEqSFMq0_dY_sApLm) covering variuos of the things you need to do.

</details>
We also provide a youtube playlist of videos to help you get up and running with `rtal`.  
These cover various of the things you need to do, see what materials helps you best.

<details>
  <summary>Click here for an overview and direct access to the full list of video tutorials</summary>
    <ul>
      <li><a href="https://www.youtube.com/watch?v=KlvOSZPiFW0">1. How to get the rtal binary</a></li>
      <li><a href="">2. How to use the help option</a></li>
      <li><a href="">3. How to get an exercise to solve</a></li>
      <li><a href="">4. How to log in</a></li>
      <li><a href="">5. How to test your solution 'locally'</a></li>
      <li><a href="">6. How to submit your solution online</a></li>
      <li><a href="">7. How to check your scoreboar</a></li>
      <li>Two external videos with useful general instructions on how to operate in a shell
         <li><a href="https://www.youtube.com/watch?v=hrinoukULzE">A video on how to install Git Bash shell on Windows</a></li>
         <li><a href="https://youtu.be/zMKacHGuIHI?si=bkK8vb2XP99pOMrr">A practical introduction to stdin, stdout and stder</a></li>
      </li>
    </ul>
</details>



<a id="get_shell"></a>
## How to get a Bash Shell

If you are on Linux or Mac, then you already have a shell. Just open a terminal (and get the basics on how to use it!)

If you use Windows, we suggest you to install the Git Bash shell.
This software and detailed instructions to get started with the Bash shell, click on this [LINK](https://git-scm.com/install/).

[Here is a video](https://www.youtube.com/watch?v=hrinoukULzE) on how to install Git Bash shell on Windows.


<a id="get_rtal"></a>
## How to get the `rtal` client

<details>
<summary>download the binary</summary>

<a href="https://github.com/Guilucand/rtal-algo-client/releases">Download the release of the `rtal` binary</a> as suitable for your PC (knowing the Operating System and the broad processor architecture is enough). Decompress it (with `tar xvf` if from command line, else you can use `7-Zip` if your Operating System is Windows)
</details>

<details>
<summary>build from the source codes</summary>

You can **get the `rtal` sources** by cloning the repo with a single command from the CLI:

```bash
git clone https://github.com/Guilucand/rtal-algo-client.git
```

or downloading its `.zip` archive and decompressing it:
```bash
wget https://github.com/Guilucand/rtal-algo-client/archive/refs/heads/main.zip
unzip main.zip
```
Alternatively, to download the repo, press the green button <img src="../strumenti/stuff/figs/Git_Code_Green_Button.png" width="100" title="" alt=""> labeled "[< > Code]" that you find at the top of the [GitHub page of the repo](https://github.com/Guilucand/rtal-algo-client). 

To **compile** these sources, the `rust` compiler is needed. You can easily get it and configure it automatically by relying on the Rust community service [`rustup.rs`](https://rustup.rs/).

Once you have installed `rust`, before the actual compilation we recommend you run:

```bash
rustup update
```
to make sure your Rust installation is up to date.

**Building:**

From the root of the already cloned `rtal` source repo run:

```bash
cargo build
```

to get the DEBUG version of the `rtal` client, the one we recommend to problem-solvers (i.e. students) as it provides more supporting information.

The executable (`rtal`) will appear in the `/target/debug/` subfolder.

For more information on the options available for compilation go to the [repo page](https://github.com/Guilucand/rtal-algo-client).
</details>

To run the `rtal` command from any folder, add `rtal` to the `PATH` environment variable as follows.
<details>
<summary>How to add the `rtal` executable location to your `PATH` environment variable</summary>

To make `rtal` directly accessible from any directory on your machine, you need to place it in a folder included in your system's `PATH` environment variable. The following steps walk you through this process on Git Bash.

1. First, if you do not already have it, create a new folder where to place those binaries that you want to make accessible from everywhere:
   ```bash
   mkdir ~/.bin
   ```

2. Now, navigate to where you downloaded rtal and decompress the archive. For example, if it landed in your ~/Downloads folder:
   ```bash
   cd ~/Downloads 
   tar xf rtal-x86_64-pc-windows-msvc.tar.gz
   ```    

3. Next, copy the rtal file:
   ```bash
   cp rtal-x86_64-pc-windows-msvc/rtal ~/.bin
   ``` 

4. Finally, add the folder created in step&nbsp;1 to your `PATH` environment variable so that your shell will search also there for executables:  
   ```bash
   cd ~/.bin
   set -o noclobber
   echo 'export PATH=$PATH:~/.bin' >> ~/.bashrc
   ``` 

   To verify everything went well, just run:
   ```bash
   rtal --version
   ```  

   If all the above steps were carried out correctly, you should see something like:
   ```bash
   rtal 0.2.0
   ```



<a id="check_rtal"></a>
## Verify that `rtal` is installed correctly and check its version

```bash
rtal -V
```

<a id="rtal-help"></a>
## The internal help (`rtal help`) 

```bash
rtal help
```

To get more details on a specific subcommand (help,list,login,logout,get,connect):

```bash
rtal help connect
```

<a id="rtal-login"></a>
## Authentication and login (`rtal login`)

For servers that require authentication (servers for homework or for exams), authentication via GIA is enabled, so before you can use the `get` or `connect` subcommands you must authenticate with:

```bash
rtal -s <URL-server> login
```

For example, for the homeworks you run:

```bash
rtal -s wss://ta.di.univr.it/dodm login
```
and then enter your matriculation number (in the format VR??????) at the prompt and copy the URL that is returned to you into the browser where you will then enter your GIA credentials.

The main servers are:

| scopo    |     URL del server          | login | allegare sorgenti | attivo |
| :---     | :---                            | ---   |      ---      |  --- | 
| homework | `wss://ta.di.univr.it/dodm`     |  ✅   |  ✅   | da marzo a febbraio successivo |
| esercizi | `wss://ta.di.univr.it/esercizi` |  ❌   |  ❌   | continuativamente |

In practice, to make a submission you are required to log in to the server beforehand and attach the sources of your solution (if multiple files, attach a `.tar` of the folder containing them) to each submission via the `connect` service.

<a id="rtal-list"></a>
## See the list of problems currently in the collection (`rtal list`)


```bash
rtal -s <URL-server> list
```


<a id="rtal-get">rtal-get</a>
## Download the text and the other public materials of a problem (`rtal get`)

```bash
rtal -s <URL-server> get <problem_name>
```


<a id="rtal-list-v_problem_name"></a>
## To view the active services for a problem

```bash
rtal -s <URL-server> list <problem_name>
```

With the verbose flag `-v` you can view the *regexp* of the allowed values ​​for the various arguments:

```bash
rtal -s <URL-server> list -v <problem_name>
```

In this way, for problems that do not follow a rigid and already known format, it is not possible to obtain explicit explanations on what the purposes of the various services listed are and on the role that their arguments play. All this could in fact depend very freely on the specific problem; TALight in fact allows a lot of freedom to the problem-maker (the teacher).

<a id="synopsis-universal-service"></a>

## Get explanations on a service and the use of its optional arguments

To obtain this kind of information you need to contact the `synopsis` service of the problem of interest, as follows:

```bash
rtal -s <URL-server> connect <problem_name> synopsis -a service=<nome_servizio>
```

In fact, it is the `connect` subcommand, discussed in the next and last point, that is used to invoke the services offered to the problem-solver (the student) for a problem.

For example, to know how you can concretely use the `synopsis` service of a specific problem, apply it to itself as follows:

```bash
rtal -s <URL-server> connect <problem_name> synopsis -a service=synopsis
```

<a id="rtal-connect"></a>
## Submit your solution or avail of other services offered for a problem (`rtal connect`)

The `connect` subcommand is used, which is richer and more complex to use. We therefore limit ourselves to the main uses, go to [`EN_the-TALight-Problem-Solver-Tutorial1-internet-server.md`](EN_the-TALight-Problem-Solver-Tutorial1-internet-server.md) in this same folder for further details on both the installation and use of `rtal` and the `connect` subcommand.

The typical use for submitting your solution to the exam or as a homework (i.e. when scores get assigned to you) will roughly follow the following format:


```bash
rtal -s <URL-server> connect -f source=<PATH-TO-SOURCE-FILE> [-e] <problem_name> [<ARGS>] -- <MY-EXECUTABLE-SOLUTION>
```

Where:

- `<PATH-TO-SOURCE-FILE>` is the complete filename (relative or absolute) of the source file of your solution (if the source files are more than one attach the `.tar` of a folder containing the sources)

- the optional flag `-e` can be added to monitor the interaction between your solution and the evaluator running on the server

- `<ARGS>` includes any specific arguments, among these the most commonly used is `size` which is used to limit the submission to a single prefix of the subtasks (to avoid slowdowns in case your solution is not suitable to deal with larger instances).
  - `-a size=esempi_testo`
  - `-a size=small`

- `<MY-EXECUTABLE-SOLUTION>` is any string that, even if entered by itself alone at the CLI prompt, causes the solver you created to start. Just a few examples:
- `./a.out` for a compiled from `C/c++`, possibly followed by the arguments that it, as you designed it, expects/allows
- `./my_solution.py arg1 arg2 ...` if your `my_solution.py` file with the python code has execution permissions and starts with the shebang line
- `python my_solution.py` or `python3 my_solution.py` to have your script executed by the python interpreter actually present locally.


> [!NOTE]
> It is useful to understand the difference between writing to `stdout` or `stderr` and possibly also to files (don't be shy about experimenting). The `--echo` flag of the `connect` subcommand can also be very useful to identify where your solution does not respect the communication protocol between your solution and the server validator.

> [!TIP]
> Even if it is just a tool, getting a little familiar with using `rtal` will facilitate you

> [!TIP]
> For homework and projects, if you do not have a suitable machine from which to carry them out and submit them, you can use the university's VirtualLab service (if you need a VPN from home to use this service)

