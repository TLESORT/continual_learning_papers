

from utils import generate_md_file
import bibtexparser

file_name = 'bibtex.bib'
with open(file_name) as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_db = bibtexparser.loads(bibtex_str, parser=bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False))

################################### Create Readme ####################################
def plot_titles(titles):
    return '\n' + "## " + titles[0] + '\n'

list_types = [["Classics", "Classic"],
               ["Surveys", "Survey", "survey"],
               ["Influentials", "Influential"],
               ["Regularization Methods", "Regularization"],
               ["Distillation Methods", "Distillation"],
               ["Rehearsal Methods", "Rehearsal"],
               ["Generative Replay Methods", "Generative Replay"],
               ["Dynamic Architectures or Routing Methods", "Architectures", "Dynamic Architecture"],
               ["Hybrid Methods", "Hybrid"],
               ["Meta-Continual Learning"],
               ["Continual-Meta Learning"],
               ["Lifelong Reinforcement Learning", "Reinforcement"],
               ["Continual Generative Modeling", "Generative Modeling"],
               ["Applications"]]

generate_md_file(DB=bib_db, list_classif=list_types, key="keywords", plot_title_fct=plot_titles, filename= "README.md", add_comments=True)


