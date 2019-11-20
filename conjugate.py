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

MOODS = ['ind', 'sub', 'imp']
SUBJECTS = ['yo', 'tú', 'él/ella/usted', 'nosotros/as', 'vosotros/as', 'ellos/ellas/ustedes']
TENSES = ['pres', 'imp', 'pret', 'fut', 'cond', 'pres perf', 'past perf', 'fut perf', 'cond perf', 'none']

VALID_ENDINGS = ['ar', 'er', 'ir']
VALID_STEM_CHANGES = ['i', 'ie', 'ue']

REFLEXIVE_PRONOUNS = ['me', 'te', 'se', 'nos', 'os', 'se']

######### REGULAR #########

IND_PRES_AR = ['o', 'as', 'a', 'amos', 'áis', 'an']
IND_PRES_ER = ['o', 'es', 'e', 'emos', 'éis', 'en']
IND_PRES_IR = ['o', 'es', 'e', 'imos', 'ís', 'en']

IND_IMP_AR = ['aba', 'abas', 'aba', 'ábamos', 'abais', 'aban']
IND_IMP_ER_IR = ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían']

IND_PRET_AR = ['é', 'aste', 'ó', 'amos', 'asteis', 'aron']
IND_PRET_ER_IR = ['í', 'iste', 'ió', 'imos', 'isteis', 'ieron']

IND_FUT_AR_ER_IR = ['é', 'ás', 'á', 'emos', 'éis', 'án']

IND_COND_AR_ER_IR = ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían']

######### IRREGULAR #########

### INDICATIVE PRETERITE ###

# indicative -car, -gar, -zar, -guar yo endings preterite
IND_PRET_YO_CAR = 'qué'
IND_PRET_YO_GAR = 'gué'
IND_PRET_YO_ZAR = 'cé'
IND_PRET_YO_GUAR = 'güé'

# indicative -caer, -eer, -oer, -oír, -uir preterite endings (i > y)
IND_PRET_UIR = ['í', 'iste', 'yó', 'imos', 'isteis', 'yeron']
IND_PRET_VOWEL_ER = ['í', 'íste', 'yó', 'ímos', 'isteis', 'yeron']

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

######### PARTICIPLE & GERUND (PROGRESSIVE) ##########

# regular
PARTICIPLE_AR = 'ado'
PARTICIPLE_ER_IR = 'ido'

GERUND_AR = 'ando'
GERUND_ER_IR = 'iendo'

# irregular
# add verbs
IRREGULAR_VERBS = ['traer']
IRREGULAR_LAST_THREES = ['car', 'gar', 'zar', 'gir', 'ger', 'eer', 'oer', 'oir', 'oír', 'uir']
IRREGULAR_LAST_FOURS = ['guar', 'ucir', 'caer']

class Verb:    
    def __init__(self, verb, definition, reflexive=False, stem_changing=False, stem_change=None, starred=False):
        # checking if args are valid is the job of main
        
        # assign instance variables based on args
        self.verb = verb
        self.stem = verb[:-2]
        self.ending = verb[-2:]
        self.last_three = verb[-3:]
        self.last_four = verb[-4:]
        self.definition = definition
        self.reflexive = reflexive
        self.stem_changing = stem_changing
        self.stem_change = stem_change
        self.starred = starred

        # note that stem-changing verbs are not considered irregular
        self.regular = self.verb not in IRREGULAR_VERBS and self.last_three not in IRREGULAR_LAST_THREES \
            and self.last_four not in IRREGULAR_LAST_FOURS

        # assign regular endings depending on verb ending
        if self.ending == 'ar':
            IND_PRES = IND_PRES_AR.copy()
            IND_IMP = IND_IMP_AR.copy()
            IND_PRET = IND_PRET_AR.copy()

            self.participle = PARTICIPLE_AR
            self.gerund = GERUND_AR

            # add other tenses later

        elif self.ending == 'er':
            IND_PRES = IND_PRES_ER.copy()
            IND_IMP = IND_IMP_ER_IR.copy()
            IND_PRET = IND_PRET_ER_IR.copy()

            self.participle = PARTICIPLE_ER_IR
            self.gerund = GERUND_ER_IR

             # add other tenses later

        else:
            IND_PRES = IND_PRES_IR.copy()
            IND_IMP = IND_IMP_ER_IR.copy()
            IND_PRET= IND_PRET_ER_IR.copy()

            self.participle = PARTICIPLE_ER_IR
            self.gerund = GERUND_ER_IR

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

        # modify assigned endings if irregular
        if not self.regular:
            # -car, -gar, -zar verbs (irregular in yo form in preterite)
            if self.last_three == 'car':
                IND_PRES[0] = IND_PRET_YO_CAR
            elif self.last_three == 'gar':
                IND_PRET[0] = IND_PRET_YO_GAR
            elif self.last_three == 'zar':
                IND_PRET[0] = IND_PRET_YO_ZAR

            # -guar verbs (add umlat in yo form preterite)
            elif self.last_four == 'guar':
                IND_PRET[0] = IND_PRET_YO_GUAR

            # -ucir, -traer verbs (c > j, no accents in preterite)
            elif self.last_four == 'ucir' or self.verb[-5:] == 'traer':
                IND_PRET = IND_PRET_UCIR_TRAER

            # vowel + er verbs (e > y in preterite) [not counting -traer]
            elif self.last_four == 'caer' or self.last_three in ['eer', 'oir', 'oír', 'oer']:
                IND_PRET = IND_PRET_VOWEL_ER

            # -uir verbs (e > y, but no accent for tú in preterite)
            elif self.last_three == 'uir':
                IND_PRET = IND_PRET_UIR

            # -ger, -gir verbs (g > j in yo form in preterite)
            elif self.last_three == 'ger' or self.last_three == 'gir':
                IND_PRES[0] = 'jo'


        # conjugate verb in different subjects and 
        # tenses based on assigned regular endings
        for i in range(6):
            self.ind_pres.append(self.stem + IND_PRES[i])
            self.ind_imp.append(self.stem + IND_IMP[i])

            if self.last_three in ['car', 'gar', 'zar'] and i == 0:
                self.ind_pret.append(self.verb[:-3] + IND_PRET[i])
            else:
                self.ind_pret.append(self.stem + IND_PRET[i])

        # modify conjugations if irregular
        # add code

        

        # add stem changes if stem-changing
        
    def conjugate(self, mood, tense, subject):
        '''
        Conjugates the verb in that mood, tense, and for that subject
        
        Arguments:
            mood {str} -- indicative ('ind'), subjunctive ('sub'), or imperative ('imp')
            tense {str} -- none ('none'), present ('pres'), imperfect ('imp'), preterite ('pret'),
                            future ('fut'), conditional ('cond'), present perfect ('pres perf'),
                            past imperfect ('past perf'), future perfect ('fut perf'), 
                            conditional perfect ('cond perf')
            subject {int} -- 0-5 (yo-ellos)

        Raises:
            TypeError -- if args are not of correct type
            ValueError -- if args are not valid
        
        Returns:
            str -- conjugated verb
        '''
        # check if arg types are correct, raise exceptions otherwise
        if type(mood) != str:
            raise TypeError("arg: mood must be of type str")

        if type(tense) != str:
            raise TypeError("arg: tense must be of type str")

        if type(subject) != int:
            raise TypeError("arg: subject must be of type int")

        # check if arg values are valid, raise exceptions otherwise
        if mood not in MOODS:
            raise ValueError("arg: mood must be in " + MOODS)

        if tense not in TENSES:
            raise ValueError("arg: tense must be in " + TENSES)

        if subject not in [0, 1, 2, 3, 4, 5]:
            raise ValueError("arg: subject must be an int from 0-5 (inclusive)")

        # conjugate based on mood and tense

        # indicative
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
            elif tense == 'fut perf':
                result = self.ind_fut_perf[subject]
            elif tense == 'cond perf':
                result = self.ind_cond_perf[subject]
        
        # subjunctive
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
        
        # imperative
        elif mood == 'imp':
            pass
        

        return result

    def __str__(self):
        pass
        # format nicely with verb tables?

    # write getters and setters
    # for booleans, prefix with "is_"


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
cazar = Verb("cazar", "to hunt")
leer = Verb("leer", "to read")
oír = Verb("oír", "to hear")
destruir = Verb("destruir", "to destroy")
traer = Verb("traer", "to bring")

verbs = [hablar, escribir, aprender, cazar, leer, oír, destruir, traer]

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

    print("-----------------------------------------------")

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


