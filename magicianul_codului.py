# ==============================================================
#   MAGICIANUL CODULUI - Quiz Python pentru Incepatori
#   THE CODE WIZARD  - Python Quiz for Beginners
# ==============================================================
# Scop / Purpose : Sa inveti Python prin practica distractiva
# Nivel / Level  : Incepator / Beginner
# ==============================================================
#
# CONCEPTE ACOPERITE / CONCEPTS COVERED:
#   1. Variabile & Tipuri de Date  ->  str, int, float, bool
#   2. Input & Print               ->  citit si afisat date
#   3. Liste & Dictionare          ->  colectii de date
#   4. Conditionale                ->  if / elif / else
#   5. Bucle                       ->  for / while
#   6. Functii                     ->  def
#
# CITESTE COMENTARIILE! Ele sunt lectiile tale.
# READ THE COMMENTS! They are your lessons.
# ==============================================================

import random   # Modul standard pentru numere/selectii aleatoare
                # Standard module for random numbers/selections


# ==============================================================
# LECTIA 1: VARIABILE & TIPURI DE DATE
# LESSON 1:  VARIABLES & DATA TYPES
# ==============================================================
#
# O variabila este o "cutie" cu un nume in care stocam date.
# A variable is a named "box" where we store data.
#
#   Tip / Type  |  Ce stocheaza / What it stores  |  Exemplu / Example
#   ------------|----------------------------------|-------------------
#   str         |  text (sir de caractere)         |  "Ana", "Python"
#   int         |  numar intreg                    |  10, -3, 0
#   float       |  numar cu virgula                |  3.14, 2.5
#   bool        |  adevarat sau fals               |  True, False
#
# Sintaxa: nume_variabila = valoare
# Syntax:  variable_name = value
#
# type(variabila) -> iti spune tipul variabilei
# type(variable)  -> tells you the variable's type

VERSIUNE = "1.0"          # str  - versiunea jocului / game version
PUNCTE_PER_RASPUNS = 10   # int  - puncte pentru fiecare raspuns corect
VIETI_INITIALE = 3        # int  - vieti cu care incepi / starting lives
INTREBARI_PE_RUNDA = 5    # int  - cate intrebari per runda / questions per round


# ==============================================================
# LECTIA 2: LISTE SI DICTIONARE - COLECTII DE DATE
# LESSON 2:  LISTS AND DICTIONARIES - DATA COLLECTIONS
# ==============================================================
#
# LISTA / LIST:
#   Colectie ordonata de elemente. / Ordered collection of elements.
#   Sintaxa: lista = [element1, element2, element3]
#   Acces:   lista[0]  <- primul element (indexul porneste de la 0!)
#            lista[1]  <- al doilea element
#   Exemplu: culori = ["rosu", "verde", "albastru"]
#            print(culori[0])  # -> "rosu"
#
# DICTIONAR / DICTIONARY:
#   Perechi cheie:valoare. / Key:value pairs.
#   Sintaxa: dict = {"cheie1": valoare1, "cheie2": valoare2}
#   Acces:   dict["cheie1"]  <- valoarea asociata cheii
#   Exemplu: persoana = {"nume": "Ana", "varsta": 20}
#            print(persoana["nume"])  # -> "Ana"
#
# Mai jos avem o LISTA de DICTIONARE - fiecare intrebare e un dictionar.
# Below we have a LIST of DICTIONARIES - each question is a dictionary.

INTREBARI = [
    {
        "intrebare": "Ce tip de date este valoarea 'Python'?",
        "raspunsuri": ["A) int", "B) float", "C) str", "D) bool"],
        "corect": "C",
        "explicatie": "'Python' este text (sir de caractere), deci tipul este str."
    },
    {
        "intrebare": "Cat este 10 + 5 in Python?",
        "raspunsuri": ["A) 105", "B) 15", "C) 10.5", "D) 1+5"],
        "corect": "B",
        "explicatie": "Operatorul + aduna numere. 10 + 5 = 15."
    },
    {
        "intrebare": "Cum afisam text pe ecran in Python?",
        "raspunsuri": ["A) show('text')", "B) display('text')", "C) write('text')", "D) print('text')"],
        "corect": "D",
        "explicatie": "Functia print() este cea standard pentru afisat text."
    },
    {
        "intrebare": "Ce face input() in Python?",
        "raspunsuri": ["A) Afiseaza text", "B) Calculeaza suma", "C) Citeste text de la tastatura", "D) Sterge o variabila"],
        "corect": "C",
        "explicatie": "input() asteapta ca utilizatorul sa scrie ceva si returneaza acel text."
    },
    {
        "intrebare": "Care este tipul variabilei: varsta = 25 ?",
        "raspunsuri": ["A) str", "B) float", "C) bool", "D) int"],
        "corect": "D",
        "explicatie": "25 este numar intreg, deci tipul este int (integer)."
    },
    {
        "intrebare": "Ce afiseaza codul: print(3 * 4) ?",
        "raspunsuri": ["A) 34", "B) 3*4", "C) 12", "D) 7"],
        "corect": "C",
        "explicatie": "* este operatorul de inmultire. 3 * 4 = 12."
    },
    {
        "intrebare": "Cum scriem un comentariu intr-un fisier Python?",
        "raspunsuri": ["A) // comentariu", "B) # comentariu", "C) /* comentariu */", "D) -- comentariu"],
        "corect": "B",
        "explicatie": "In Python, comentariile incep cu #. Restul liniei e ignorat de Python."
    },
    {
        "intrebare": "Ce este True in Python?",
        "raspunsuri": ["A) Un numar intreg", "B) Un sir de caractere", "C) O valoare de tip bool", "D) O functie built-in"],
        "corect": "C",
        "explicatie": "True si False sunt cele doua valori ale tipului bool (boolean)."
    },
    {
        "intrebare": "Ce face acest cod: x = 10; x = x + 3 ?",
        "raspunsuri": ["A) x ramane 10", "B) x devine 3", "C) Eroare de sintaxa", "D) x devine 13"],
        "corect": "D",
        "explicatie": "Intai x=10, apoi x=x+3 adica x=10+3=13. Variabilele isi pot schimba valoarea!"
    },
    {
        "intrebare": "Cum stocam textul 'Salut' intr-o variabila numita mesaj?",
        "raspunsuri": ["A) mesaj == 'Salut'", "B) mesaj : 'Salut'", "C) mesaj = 'Salut'", "D) mesaj => 'Salut'"],
        "corect": "C",
        "explicatie": "= este operatorul de ATRIBUIRE. Il folosim sa dam o valoare unei variabile."
    },
    {
        "intrebare": "Ce afiseaza: print(type(3.14)) ?",
        "raspunsuri": ["A) <class 'int'>", "B) <class 'str'>", "C) <class 'float'>", "D) <class 'bool'>"],
        "corect": "C",
        "explicatie": "3.14 are virgula, deci este float. type() ne spune tipul unei valori."
    },
    {
        "intrebare": "Care dintre acestea este un sir de caractere (str) valid?",
        "raspunsuri": ["A) 42", "B) True", "C) 3.14", "D) 'buna ziua'"],
        "corect": "D",
        "explicatie": "Un str se scrie intre ghilimele simple ' ' sau duble \" \". Celelalte sunt int, bool si float."
    },
]


# ==============================================================
# LECTIA 3: FUNCTII - BLOCURI DE COD REUTILIZABILE
# LESSON 3:  FUNCTIONS - REUSABLE CODE BLOCKS
# ==============================================================
#
# O functie este un bloc de cod cu un NUME pe care il CHEMAM ori
# de cate ori avem nevoie. Scriem codul o data, il folosim de n ori.
# A function is a named code block we CALL whenever we need it.
# Write the code once, use it n times.
#
# Sintaxa / Syntax:
#   def numele_functiei(parametru1, parametru2):
#       # codul functiei / function code
#       return rezultat  # optional
#
# Exemplu / Example:
#   def saluta(nume):
#       print("Buna, " + nume + "!")
#
#   saluta("Maria")   # -> Buna, Maria!
#   saluta("Ion")     # -> Buna, Ion!
#
# DE CE FUNCTII? / WHY FUNCTIONS?
#   - Nu repetam cod / We don't repeat code
#   - Codul e mai lizibil / Code is more readable
#   - Usor de modificat intr-un singur loc / Easy to change in one place


def linie(caracter="=", lungime=56):
    # Operatorul * aplicat pe un str il REPETA: "=" * 5 -> "====="
    # The * operator applied on a str REPEATS it
    print(caracter * lungime)


def titlu():
    linie()
    print("    MAGICIANUL CODULUI  |  THE CODE WIZARD")
    print(f"    Quiz Python pentru Incepatori  |  v{VERSIUNE}")
    linie()


def cere_nume():
    # ==============================================================
    # RECAPITULARE LECTIA 2: INPUT
    # RECAP LESSON 2: INPUT
    # ==============================================================
    # input("prompt") afiseaza promptul si ASTEAPTA input de la user.
    # input("prompt") displays the prompt and WAITS for user input.
    # Returneaza MEREU un str. Daca vrei int, folosesti: int(input(...))
    # It ALWAYS returns a str. For int use: int(input(...))
    # .strip() elimina spatiile de la inceput si sfarsit / removes whitespace

    print()
    print("  Cum te cheama? / What is your name?")
    nume = input("  >> ").strip()

    # Conditie de validare / Validation conditional
    if nume == "":
        nume = "Jucatorul Misterios"   # valoare implicita / default value

    return nume   # returnam valoarea ca sa o folosim in alta parte


def afiseaza_intrebare(nr, total, q, vieti):
    print()
    linie("-", 56)
    # f-string: scriem variabile direct in text cu {}
    # f-string: we write variables directly in text with {}
    # Exemplu: f"Salut {nume}!" cu nume="Ana" -> "Salut Ana!"
    inimi = "♥ " * vieti
    print(f"  Intrebarea {nr}/{total}   Vieti / Lives: {inimi}")
    linie("-", 56)
    print()
    print(f"  {q['intrebare']}")
    print()

    # ==============================================================
    # LECTIA 5a: BUCLA FOR - PARCURGEREA UNEI LISTE
    # LESSON 5a:  FOR LOOP - GOING THROUGH A LIST
    # ==============================================================
    # Bucla for parcurge fiecare element al unei liste, unul cate unul.
    # The for loop goes through each list element, one by one.
    #
    # Sintaxa / Syntax:
    #   for variabila_temporara in lista:
    #       # cod executat pentru fiecare element
    #
    # Exemplu / Example:
    #   legume = ["morcov", "ceapa", "ardei"]
    #   for leguma in legume:
    #       print(leguma)
    #   # Afiseaza pe rand: morcov, ceapa, ardei

    for raspuns in q["raspunsuri"]:
        print(f"    {raspuns}")

    print()


def cere_raspuns_valid():
    # ==============================================================
    # LECTIA 5b: BUCLA WHILE - REPETA CAT TIMP O CONDITIE E ADEVARATA
    # LESSON 5b:  WHILE LOOP - REPEAT WHILE A CONDITION IS TRUE
    # ==============================================================
    # Sintaxa / Syntax:
    #   while conditie:
    #       # cod repetat
    #
    # Exemplu / Example:
    #   nr = 0
    #   while nr < 3:
    #       print(nr)
    #       nr = nr + 1
    #   # Afiseaza: 0, 1, 2
    #
    # ATENTIE: Asigura-te ca bucla se termina la un moment dat!
    # CAREFUL: Make sure the loop ends at some point!
    # Aici while ruleaza pana cand userul da A, B, C sau D.
    # Here while runs until the user gives A, B, C, or D.

    while True:   # bucla infinita oprita de return / infinite loop stopped by return
        raspuns = input("  Raspunsul tau (A/B/C/D) / Your answer: ").strip()

        if raspuns.upper() in ["A", "B", "C", "D"]:
            return raspuns.upper()   # raspuns valid, iesim / valid answer, we exit
        else:
            print("  ⚠  Introdu doar A, B, C sau D / Enter only A, B, C or D")


def evalueaza_scor(scor, total):
    # ==============================================================
    # RECAPITULARE LECTIA 4: CONDITIONALE INLANTUITE
    # RECAP LESSON 4: CHAINED CONDITIONALS
    # ==============================================================
    # if -> elif -> elif -> else : verificam conditii in ordine.
    # Python verifica de sus in jos si executa PRIMUL bloc adevarat.
    # Python checks top to bottom and executes FIRST true block.

    procent = (scor / total) * 100   # float - procentajul scorului

    if procent == 100:
        nivel = "MAESTRU PYTHON"
        emoji = "★★★"
        mesaj = "Perfect! Ai raspuns corect la TOATE intrebarile!"
    elif procent >= 80:
        nivel = "EXPERT"
        emoji = "★★ "
        mesaj = "Excelent! Esti pe drumul cel bun!"
    elif procent >= 60:
        nivel = "AVANSAT"
        emoji = "★  "
        mesaj = "Bine! Inca un pic si esti expert."
    elif procent >= 40:
        nivel = "INCEPATOR"
        emoji = "·  "
        mesaj = "Continua sa inveti! Fiecare greseala te invata ceva."
    else:
        nivel = "NOVICE"
        emoji = "·  "
        mesaj = "Nu te descuraja! Reciteste lectiile si incearca din nou."

    return nivel, emoji, mesaj, procent


def joaca_runda(nume):
    """Ruleaza o runda completa si returneaza scorul. / Runs a full round and returns score."""

    # random.sample(lista, n) -> selecteaza n elemente unice in ordine aleatoare
    # random.sample(list, n)  -> selects n unique elements in random order
    intrebari_runda = random.sample(INTREBARI, min(INTREBARI_PE_RUNDA, len(INTREBARI)))

    scor = 0               # int - puncte acumulate / accumulated points
    vieti = VIETI_INITIALE # int - vieti ramase / remaining lives
    total = len(intrebari_runda)

    # ==============================================================
    # LECTIA 5c: enumerate() - INDEX SI ELEMENT IN ACELASI TIMP
    # LESSON 5c:  enumerate() - INDEX AND ELEMENT AT THE SAME TIME
    # ==============================================================
    # enumerate(lista) -> ne da perechi (index, element)
    # enumerate(list)  -> gives us (index, element) pairs
    #
    # Exemplu / Example:
    #   fructe = ["mar", "para", "kiwi"]
    #   for i, fruct in enumerate(fructe):
    #       print(i, fruct)
    #   # 0 mar
    #   # 1 para
    #   # 2 kiwi

    for i, intrebare in enumerate(intrebari_runda):
        nr_curent = i + 1   # +1 pentru ca indexul porneste de la 0

        afiseaza_intrebare(nr_curent, total, intrebare, vieti)

        raspuns = cere_raspuns_valid()

        # ==============================================================
        # RECAPITULARE LECTIA 4: if / else
        # RECAP LESSON 4: if / else
        # ==============================================================
        # == este operatorul de COMPARATIE (egal cu)
        # == is the COMPARISON operator (equal to)
        # NU confunda cu = care este ATRIBUIRE!
        # Do NOT confuse with = which is ASSIGNMENT!

        if raspuns == intrebare["corect"]:
            scor += PUNCTE_PER_RASPUNS   # += e prescurtare pentru scor = scor + PUNCTE_PER_RASPUNS
            print()
            print("  ✓ CORECT! Bravo! / CORRECT! Well done!")
            print(f"  + {PUNCTE_PER_RASPUNS} puncte / points  |  Total: {scor}")
        else:
            vieti -= 1   # -= e prescurtare pentru vieti = vieti - 1
            print()
            print(f"  ✗ Gresit. Raspuns corect: {intrebare['corect']}")
            print(f"  → {intrebare['explicatie']}")
            print(f"  Vieti ramase / Lives left: {'♥ ' * vieti}")

            # break opreste bucla for imediat / break stops the for loop immediately
            if vieti == 0:
                print()
                print("  ✗ Ai ramas fara vieti! / You ran out of lives!")
                break

        input("\n  [ ENTER pentru urmatoarea / for next ] ")

    return scor, total


def rezultat_final(nume, scor, total):
    """Afiseaza ecranul de rezultat. / Displays the result screen."""
    nivel, emoji, mesaj, procent = evalueaza_scor(scor, total)

    print()
    linie()
    print("    REZULTAT FINAL / FINAL RESULT")
    linie()
    print()
    print(f"  Jucator / Player  : {nume}")
    print(f"  Scor / Score      : {scor} puncte / points")
    print(f"  Raspunsuri corecte: {scor // PUNCTE_PER_RASPUNS} din {total}")
    print(f"  Procent / Pct     : {round(procent)}%")
    print()
    print(f"  Nivel / Level : {emoji} {nivel}")
    print(f"  {mesaj}")
    print()
    linie()


def joaca_din_nou():
    """Returneaza True daca vrea sa joace din nou. / Returns True if they want to play again."""
    print()
    print("  Vrei sa joci din nou? / Want to play again?")
    print("  [D] Da / Yes     [N] Nu / No")
    print()

    while True:
        alegere = input("  >> ").strip().upper()
        if alegere in ["D", "DA", "Y", "YES"]:
            return True
        elif alegere in ["N", "NU", "NO"]:
            return False
        else:
            print("  ⚠  Apasa D (da) sau N (nu) / Press D (yes) or N (no)")


# ==============================================================
# PUNCTUL DE START AL PROGRAMULUI / PROGRAM START POINT
# ==============================================================
#
# Aceasta constructie este conventia Python pentru "codul principal".
# This construct is the Python convention for "main code".
#
# __name__ este o variabila speciala. Cand rulezi DIRECT fisierul,
# Python ii da automat valoarea "__main__". Cand il importezi
# dintr-un alt fisier, __name__ va fi numele modulului.
# __name__ is a special variable. When you run the file DIRECTLY,
# Python automatically sets it to "__main__". When you import it
# from another file, __name__ will be the module name.
#
# Rezultat practic / Practical result:
#   python magicianul_codului.py  -> codul de jos RULEAZA
#   import magicianul_codului     -> codul de jos NU ruleaza

if __name__ == "__main__":

    titlu()

    print()
    print("  Bine ai venit! Acesta este un quiz despre Python.")
    print("  Welcome! This is a Python knowledge quiz.")
    print()
    print(f"  Reguli / Rules:")
    print(f"  - {INTREBARI_PE_RUNDA} intrebari per runda / questions per round")
    print(f"  - {VIETI_INITIALE} vieti / lives  |  {PUNCTE_PER_RASPUNS} puncte per raspuns corect / points per correct answer")
    print()

    # Obtinem numele jucatorului / Get player name
    jucator = cere_nume()   # variabila primeste valoarea returnata de functie

    print()
    print(f"  Salut, {jucator}! Sa incepem! / Hi, {jucator}! Let's go!")

    # ==============================================================
    # BUCLA PRINCIPALA A JOCULUI / MAIN GAME LOOP
    # ==============================================================
    # Variabila joaca controleaza daca while continua sau se opreste.
    # The joaca variable controls whether while continues or stops.
    # Cand joaca_din_nou() returneaza False, bucla se termina.
    # When joaca_din_nou() returns False, the loop ends.

    continua = True         # bool - flag pentru bucla principala
    runde_jucate = 0        # int  - contor de runde / round counter

    while continua:

        runde_jucate += 1   # incrementam contorul / increment counter
        print()
        print(f"  ─── Runda {runde_jucate} / Round {runde_jucate} ───")

        # Rulam runda si primim scorul inapoi / Run round and get score back
        scor, total = joaca_runda(jucator)

        # Afisam rezultatul / Display result
        rezultat_final(jucator, scor, total)

        # Intrebam daca continua / Ask if they continue
        continua = joaca_din_nou()

    # Mesaj de final / Final message
    print()
    linie()
    print(f"  Pa, {jucator}! Ai jucat {runde_jucate} runde.")
    print(f"  Bye, {jucator}! You played {runde_jucate} rounds.")
    print()
    print("  Continua sa inveti Python - practica face perfectul!")
    print("  Keep learning Python - practice makes perfect!")
    linie()
    print()


# ==============================================================
# EXERCITII PENTRU TINE / EXERCISES FOR YOU
# ==============================================================
# Rezolva-le dupa ce ai citit si inteles codul de mai sus!
# Solve them after reading and understanding the code above!
#
# ★ EXERCITIU 1 (USOR / EASY) - Variabile & Liste
#   Adauga 2 intrebari noi la lista INTREBARI de sus.
#   Add 2 new questions to the INTREBARI list above.
#   Urmeaza exact acelasi format ca intrebarile existente.
#   Follow the exact same format as existing questions.
#
# ★★ EXERCITIU 2 (MEDIU / MEDIUM) - Conditionale
#   Modifica functia evalueaza_scor() sa afiseze un mesaj
#   SPECIAL daca scorul este 0.
#   Modify evalueaza_scor() to show a SPECIAL message if score is 0.
#   Indiciu: adauga un if inainte de celelalte conditii.
#   Hint: add an if before the other conditionals.
#
# ★★ EXERCITIU 3 (MEDIU / MEDIUM) - Bucle & Variabile
#   Adauga un sistem de HIGH SCORE: tine minte cel mai bun scor
#   din toate rundele si afiseaza-l la sfarsit.
#   Add a HIGH SCORE system: remember the best score from all
#   rounds and display it at the end.
#   Indiciu: ai nevoie de o variabila high_score = 0 inainte de while,
#            si un if in bucla care o actualizeaza.
#   Hint: you need a high_score = 0 variable before while,
#         and an if inside the loop that updates it.
#
# ★★★ EXERCITIU 4 (DIFICIL / HARD) - Functii
#   Creeaza o functie afiseaza_statistici(runde, scoruri) care
#   primeste numarul de runde si o lista de scoruri si afiseaza:
#   - scorul total / total score
#   - media scorurilor / average score
#   - cel mai bun scor / best score
#   Create a function afiseaza_statistici(runde, scoruri) that
#   takes number of rounds and a list of scores and displays:
#   total, average, and best score.
# ==============================================================
