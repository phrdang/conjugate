''' 
Create a program that can:
1. Allow the user to practice conjugations of Spanish verbs
in multiple tenses (and moods)
    - import random

### SMART VERSION ###
2. verbs are objects
    - attributes: 
        * ending: -ar, -er, -ir
            * -ar: -gar, -car, -zar, -guar
            * -ir: -uir, -ucir, -gir
            * -er: -eer, -ger, -traer
        * stem-changing
        * irregular/regular
        * definition (english)
            - definition changes in preterite
        * starred (by user)
    - methods:
        * conjugate(mood, tense, subject)
        * getters and setters
        * constructor
        * display_verb() (print attributes formatted nicely)
### BASIC VERSION ###
2. verbs are dictionary and/or multi-dimensional list entries

3. Allow user to add verbs
4. Write onto .txt to save data
'''

import random
from time import sleep

SUBJECTS = ['yo', 'tú', 'él/ella/usted', 'nosotros/as', 'vosotros/as', 'ellos/ellas/ustedes']
REFLEXIVE_PRONOUNS = ['me', 'te', 'se', 'nos', 'os', 'se']
VALID_ENDINGS = ['ar', 'er', 'ir']
VALID_STEM_CHANGES = ['i', 'ie', 'ue']

######### REGULAR #########

# indicative -ar endings
IND_PRES_AR = ['o', 'as', 'a', 'amos', 'áis', 'an']
IND_IMP_AR = ['aba', 'abas', 'aba', 'ábamos', 'abais', 'aban']
IND_PRET_AR = ['é', 'aste', 'ó', 'amos', 'asteis', 'aron']

# indicative -er and -ir endngs
IND_PRES_ER = ['o', 'es', 'e', 'emos', 'éis', 'en']
IND_PRES_IR = ['o', 'es', 'e', 'imos', 'ís', 'en']

IND_IMP_ER_IR = ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían']
IND_PRET_ER_IR = ['í', 'iste', 'ió', 'imos', 'isteis', 'ieron']

######### IRREGULAR #########

### INDICATIVE PRETERITE ###

# indicative -car, -gar, -zar, -guar yo endings preterite
IND_PRET_YO_CAR = 'qué'
IND_PRET_YO_GAR = 'gué'
IND_PRET_YO_ZAR = 'cé'
IND_PRET_YO_GUAR = 'güé'

# indicative -caer, -eer, -oer, -oír, -uir preterite endings (i > y)
IND_PRET_UIR = ['í', 'iste', 'yó', 'imos', 'isteis', 'yeron']
IND_PRET_EER = ['í', 'íste', 'yó', 'ímos', 'isteis', 'yeron']

# indicative -ucir, -traer preterite endings (j)
IND_PRET_UCIR_TRAER = ['je', 'jiste', 'jo', 'jimos', 'jisteis', 'jeron']

### INDICATIVE PRESENT ###

# -ger, -gir yo endings
IND_PRES_YO_GER_GIR = 'jo'

# just plain old irregulars

### INDICATIVE IMPERFECT ###
IND_IMP_SER = ['era', 'eras', 'era', 'éramos', 'erais', 'eran']
IND_IMP_IR = ['iba', 'ibas', 'iba', 'íbamos', 'ibais', 'iban']
IND_IMP_VER = ['veía', 'veías', 'veía', 'veíamos', 'veíais', 'veían']

# preterite

class Verb:    
    def __init__(self, verb, definition, is_reflexive=False, is_stem_changing=False, stem_change=None, is_starred=False):
        # checking if args are valid is the job of main
        
        # assign instance variables based on args
        self.verb = verb
        self.ending = verb[-2:]
        self.definition = definition
        self.is_reflexive = is_reflexive
        self.is_stem_changing = is_stem_changing
        self.stem_change = stem_change
        self.is_starred = is_starred

        # assign endings depending on verb (create lists)
        # handle irregular verbs later

        if self.ending == 'ar':
            IND_PRES = IND_PRES_AR
            IND_IMP = IND_IMP_AR
            IND_PRET = IND_PRET_AR

            # add other tenses later

        elif self.ending == 'er':
            IND_PRES = IND_PRES_ER
            IND_IMP = IND_IMP_ER_IR
            IND_PRET = IND_PRET_ER_IR

             # add other tenses later
        else:
            IND_PRES = IND_PRES_IR
            IND_IMP = IND_IMP_ER_IR
            IND_PRET= IND_PRET_ER_IR

             # add other tenses later
        
        # add conjugations

        self.ind_pres = []
        self.ind_imp = []
        self.ind_pret = []
        self.ind_fut = []

        self.ind_cond = []

        self.ind_pres_perf = []
        self.ind_past_perf = []
        self.ind_fut_perf = []
        self.ind_cond_perf = []

        for i in range(6):
            self.ind_pres.append(verb[:-2] + IND_PRES[i])
            self.ind_imp.append(verb[:-2] + IND_IMP[i])
            self.ind_pret.append(verb[:-2] + IND_PRET[i])
        
    def conjugate(self, mood, tense, subject):
        '''
        Conjugates the verb in that mood, tense, and for that subject
        
        Arguments:
            mood {str} -- indicative ('ind'), subjunctive ('sub'), or imperative ('imp')
            tense {str} -- none ('none'), present ('pres'), imperfect ('imp'), preterite ('pret'),
                            future ('fut'), conditional ('cond'), present perfect ('pres perf'),
                            past imperfect ('past perf'), conditional perfect ('cond perf')
            subject {int} -- 0-5 (yo-ellos)
        
        Returns:
            str -- conjugated verb
        '''

        if mood == 'ind':
            if tense == 'pres':
                result = self.ind_pres[subject]
            elif tense == 'imp':
                result = self.ind_imp[subject]
            elif tense == 'pret':
                result = self.ind_pret[subject]
            elif tense == 'fut':
                result = self.ind_fut[subject]
            elif tense == 'cond':
                result = self.ind_cond[subject]
            elif tense == 'pres perf':
                result = self.ind_pres_perf[subject]
            elif tense == 'past perf':
                result = self.ind_past_perf[subject]
            elif tense == 'cond perf':
                result = self.ind_cond_perf[subject]
        elif mood == 'sub':
            if tense == 'pres':
                pass
            elif tense == 'imp':
                pass
            elif tense == 'pret':
                pass
            elif tense == 'fut':
                pass
            elif tense == 'cond':
                pass
            elif tense == 'pres_perf':
                pass
            elif tense == 'pres_imp':
                pass
            elif tense == 'pres_pret':
                pass
        elif mood == 'imp':
            pass

        return result

    def __str__(self):
        pass
        # format nicely with verb tables?

    # write getters and setters


def get_command(valid_input):
    # copy from pyp
    pass

def main_menu():
    pass

def practice_verb_conjugation():
    pass

def add_verbs():
    pass

def save_data():
    pass

quit = False

print("Welcome to Spanish Conjugation!")


hablar = Verb("hablar", "to speak")
escribir = Verb("escribir", "to write")
aprender = Verb("aprender", "to learn")

verbs = [hablar, escribir, aprender]

for verb in verbs:
    print()
    print("ind pres")
    for i in range(6):
        conjugated = verb.conjugate("ind", "pres", i)
        print(SUBJECTS[i] + " " + conjugated)

    print()
    print("ind imp")
    for i in range(6):
        conjugated = verb.conjugate("ind", "imp", i)
        print(SUBJECTS[i] + " " + conjugated)

    print()
    print('ind pret')
    for i in range(6):
        conjugated = verb.conjugate('ind', 'pret', i)
        print(SUBJECTS[i] + " " + conjugated)

# while not quit:
#     print("Main Menu")
#     print('''
#     (1) Practice verb conjugation
#     (2) Add verbs
#     (3) Quit
# ''')
#     user_input = int(input("Enter 1, 2, or 3: "))
#     if user_input == 1:
#         # practice verb conjugation
#         print("Practice verb conjugation menu")
#         print('''
#         (1) Indicative
#         (2) Subjunctive
#         (3) Imperative
#         ''')
#     elif user_input == 2:
#         # add verbs
#         pass
#     else:
#         # ask user if they want to save data
#             # yes: save it
#             # no: quit
#         quit = True

#         # print credits
#         print("Credits")
#         print("Author: Rebecca Dang")
#         print("Project started: 10 Nov 2019")
#         print("Last update: 10 Nov 2019")


