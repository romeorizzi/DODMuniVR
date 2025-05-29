#!/usr/bin/env python3

from sys import stdin, stdout, stderr, argv
import os
import ruamel.yaml as yaml
import shutil
import argparse

usage = f"""
   Call as follows:
      {argv[0]} [options]

   where the long (or short) forms of the options are:
     --verbosity (or -v)
   and the different verbosity levels are:
         0 run quiet (all problems go on stderr anyhow)
         1 notify on stdout only after having successfully parsed a yaml file
         2 notify on stdout when an output file has been completed
         3 notify on stdout just before opening a file
         4 print main checkpoints and transitions between stages
(default value)
         5 print at each checkpoint or phase transition
(default value)
         6 print-debuggings that can be turned-on when calling the scripts

     -- appelli (or -a)
        appello_algoritmi spots out these problems in the generated Markdown pages

   Note: any disambiguating prefix is good for the long form (--) of all option names"""


# Funzione per caricare il file YAML
def load_yaml(filename):
    if os.path.exists(filename):
        print(f"Found file `{filename}`. Now opening and processing it ...", file=ostream["now_opening_a_file"])
    else:
        print(f"Errore: il file `{filename}` non è stato trovato!", file=stderr)
        exit(1)    
    try:
        with open(filename) as stream:
            datayaml = yaml.YAML(typ='safe', pure=True).load(stream)
    except yaml.YAMLError as exc:
        print(f"Errore nel parsing dello YAML (in `{filename}`): {exc}", file=stderr)
        exit(1)
    print(f"Ok: the file `{filename}` has been successfully read and parsed as YAML.", file=ostream["ifile_parsed_ok"])
    return datayaml


def create_readme_and_symlinks(topic, tbody):
    """
       1. writes the `README.md` file in the `target_folder` defined in the next line of code
       2. in the suitable form, but essentially the same content as written in the topic folder `README.md` file, is also returned to the coller that will insert it verbatim as a section in the  `README.md` file of the `.../archive/problems` folder
    """
    #print(f"\n\n\n -> called create_readme_and_symlinks(\n     {topic=}\n     {tbody=}\n)\n\n\n")
    
    target_folder = os.path.join("..", "topics", topic)
    readme_text_4topic_folder = f'# {tbody["readme_title"]}\n\n'
    readme_text_4problems_folder = f'<details>\n<summary>{tbody["readme_title"]}</summary>\n\n'
    
    # Crea la cartella di destinazione se non esiste
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for pcodename,problem_dict in tbody["problems"].items():
        print(f"\n\n\n{pcodename=}, {problem_dict=}\n\n\n", file=ostream["switchable_print-debuggings"])
        # Aggiungi riferimento al problema `problem_dict` nel README in creazione:
        closing_of_mention_line = "\n"
        if "appello_algoritmi" in problem_dict and problem_dict["appello_algoritmi"] is not None:
            closing_of_mention_line = f" ({problem_dict['appello_algoritmi']})\n"
        pcodename = problem_dict["codename"]        
        readme_text_4topic_folder += f'- [{pcodename}](../../problems/{pcodename})\n'
        readme_text_4problems_folder +=  f'- [{pcodename}]({pcodename})\n'
        
        # Crea/aggiorna il symlink nella cartella di argomento specifico:
        symlink_path = os.path.join(target_folder, pcodename)
        problem_path = os.path.join("..", "..", "problems", pcodename)
        if os.path.exists(symlink_path):
            os.remove(symlink_path)
        os.symlink(problem_path, symlink_path)
        
    # Scrivi il README.md nella cartella di argomento specifico:
    readme_path = os.path.join(target_folder, "README.md")
    with open(readme_path, "w") as fout:
        fout.write(readme_text_4topic_folder)
    print(f"\nOk: per il {topic=} (ossia nel folder {target_folder=}) ho creato i symlink ai problemi di pertinenza ed il file README.md con la loro lista.", file=ostream["ofile_closed_ok"])

    readme_text_4problems_folder += '</details>'
    return readme_text_4problems_folder


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=usage, formatter_class=argparse.RawTextHelpFormatter)
    options = parser.add_argument_group("options")
    options.add_argument("-v","--verbosity", type=int, default=4, choices=range(10))
    args = parser.parse_args()
    devnull = open(os.devnull, 'w')
    ostream = {}
    ostream_keys = ["ifile_parsed_ok",
                    "ofile_closed_ok",
                    "now_opening_a_file",
                    "checkpoint1",
                    "checkpoint2",
                    "switchable_print-debuggings"]
    for i,key in enumerate(ostream_keys):
        ostream[key] = stdout if i < args.verbosity else open(os.devnull, 'w')

# BEGIN (real __name__ == "__main__"):
    topics_yaml = load_yaml(os.path.join("..", "topics", "topics.yaml"))
    print("Ora leggeremo e processeremo i file `info.yaml` dalle cartelle dei problemi e lo integriamo.", file=ostream["checkpoint1"])
    for topic in topics_yaml:
        #print(f"\n\n{topic=}\n{topics_yaml=}\n\n")
        if not "problems" in topics_yaml[topic]:
            topics_yaml[topic]['problems'] = {}
        #print(f"\n\n{topics_yaml[topic]['problems']=}\n\n")

    for pcodename in os.listdir():
      if os.path.isdir(pcodename):
        p_yamlfile = os.path.join(pcodename, "info.yaml")
        if os.path.exists(p_yamlfile):
            problems_yaml = load_yaml(p_yamlfile)
            #print(f"\n\n\n{problems_yaml=}\n\n\n")
            p_topics = []
            p_topics_as_strs = []
            with open(os.path.join(".", pcodename, "README.md"), "w") as fout:
                fout.write(f"# {problems_yaml['title']} ({pcodename})\n\n")
                if "training" in problems_yaml:
                    fout.write("## Ripreso dalle Olimpiadi di Informatica\n\n")
                    fout.write(f'Una versione di questo problema fu proposta alle {problems_yaml["training"]["evento"]} ({problems_yaml["training"]["year"]}).\n> [!TIP]\n> Segui [questo link]({problems_yaml["training"]["URL"]}) per vederne il testo, sottomettere tue soluzioni al sito di training delle olimpiadi, o ispezionare quale altro materiale o indicazione sia lì fornita.')
                if "COCI" in problems_yaml:
                    URL_COCI_home = "https://hsin.hr/coci/"
                    edizione_COCI = problems_yaml["COCI"]["edizione_as_str"]
                    URL_edizione = URL_COCI_home + edizione_COCI + "/"
                    URL_contest = URL_edizione + str(problems_yaml["COCI"]["num_contest"])
                    task_num = str(problems_yaml["COCI"]["task_num"])
                    task_name = problems_yaml["COCI"]["task_name"]
                    fout.write(f"## Problema preso dalle [CROATIAN OPEN COMPETITION IN INFORMATICS (COCI)]({URL_COCI_home})\n\n")
                    fout.write(f'Si chiamava `{task_name}` ed era il task {task_num} del [Contest {problems_yaml["COCI"]["num_contest"]}]({URL_contest}) in [Edizione {edizione_COCI}]({URL_edizione}).')
                if len(problems_yaml["main_topics"]) > 0:
                    for t in problems_yaml["main_topics"]:
                        if t not in topics_yaml:
                            print(f"WARNING (FIX THIS FIRST!): the main topic `{t}` of problem `{pcodename}` is not present in the file `.../topics/topics.yaml`!", file=stderr)
                            #exit(0)
                        else:
                            p_topics.append(t)
                            p_topics_as_strs.append(f"**{t}**")
                if len(problems_yaml["topics"]) > 0:
                    for t in problems_yaml["topics"]:
                        if t not in topics_yaml:
                            print(f"WARNING (FIX THIS FIRST!): the topic `{t}` is not present in the file `.../topics/topics.yaml` though it is one of the topics of problem {pcodename}!", file=stderr)
                            #exit(0)
                        else:
                            p_topics.append(t)
                            p_topics_as_strs.append(t)
                if len(p_topics) > 0:
                    fout.write("\n\n## Argomenti/tecniche di pertinenza\n\n - ")
                    fout.write("\n - ".join(p_topics_as_strs) + "\n")
                    # problems_yaml["p_topics"] = p_topics
                    # problems_yaml["p_topics_as_strs"] = p_topics_as_strs
                if len(problems_yaml["similar_problems"]) > 0:
                    fout.write("## Problemi Simili\n\n - ")
                    fout.write("\n - ".join(problems_yaml["similar_problems"]) + "\n")
                if problems_yaml["try_before"] is not None:
                    fout.write(f"\n> [!TIP]\n> Se troppo difficile prova ad affrontare prima il problema `{problems_yaml['try_before']}`.\n\n")
                if problems_yaml["try_next"] is not None:
                    fout.write(f"\n> [!TIP]\n> Se vuoi approfondire su questa linea un buon prossimo problema potrebbe essere `{problems_yaml['try_next']}`.\n\n")                    
            print(f"Ok: ho creato il file `.../archive/problems/{pcodename}/README.md` and ascribed the `{pcodename}` dictionary to the topics {p_topics}\n", file=ostream["ofile_closed_ok"])
            for topic in p_topics:
                if topic not in topics_yaml:
                    print("ATTENZIONE (FIX THIS FIRST!): devi aggiungere l'argomento `{topic=}` al file `.../topics/topics.yaml` poichè il problema `pcodename` è ascritto ad esso.")
                    exit(0)
                topics_yaml[topic]["problems"][pcodename] = problems_yaml
                print(f"\nOk: ho aggiunto il problema `{pcodename}` all'argomento {topics_yaml[topic]['readme_title']=} ({topic=})", file=ostream["checkpoint2"])

    # Elaborazione di ciascun singolo topic, ma anche tessitura di un summary
    summary = "# Elenco problemi raccolti per topics\n\n> [!TIP]\n> Clicca sugli topics per visualizzarne la lista dei relativi problemi.\n\n> [!NOTE]\n> Uno stesso problema può ricadere sotto più topics.\n\n"
    for topic, tbody in topics_yaml.items():
        print(f" + Found in file YAML: {topic=}", file=ostream["checkpoint1"])
        summary += create_readme_and_symlinks(topic, tbody)
        print(f" = Successfully managed: {topic=}", file=ostream["checkpoint1"])
    print("\nOk: in ciascun argomento (ossia subfolder di `.../archive/topics`) ho crato i symlink ai problemi di pertinenza ed il file README.md con la loro lista.", file=ostream["checkpoint1"])
    
    with open(os.path.join(".", "README.md"), "w") as fout:
        fout.write(summary)
    print("\nOk: Ho infine creato un README.md complessivo nella presente cartella (`.../archive/problems`), coi problemi organizzati per argomento.\n (Uno stesso problema può apparire sotto più topics.)\n\nFinito. Fatto tutto!", file=ostream["ofile_closed_ok"])
