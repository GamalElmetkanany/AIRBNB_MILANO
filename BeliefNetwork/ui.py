import pandas as pd
import pyswip as psw
import time
from os import path
from sys import argv
import re

from beliefNetwork import BeliefNetwork

prg = psw.Prolog() #oggetto prolog per eseguire query



def BF_help():
    """
    print dell'help della Belief Network
    """

    print("\nAttributi discrete Disponibili:")
    print("- Class of Price         --> Valori {economy, affordable, medium, expensive, top level}")
    print("- Host Response Rate     --> Valori {never responds, usually responds, often responds, always responds}")
    print("- Number of Reviews      --> Valori {no reviews, few reviews, some reviews, lot of reviews}")
    print("- Review Scores Rating   --> Valori {low rating, good rating, nice rating, top rating}")
    print("- Neighbourhood Cleansed --> Valori {NAVIGLI, Viale Monza, BUENOS AIRES, CENTRALE, DUOMO, BRERA, TICINESE, WASHINGTON, LAMBRATE, VILLAPIZZONE, GUASTALLA,")
    print("                                     ISOLA, CITTA STUDI, GIAMBELLINO, DE ANGELI ROSA, BANDE NERE, TORTONA, XXII MARZO, GHISOLFA, PORTELLO, UMBRIA, PARCO FORLANINI, SARPI,")
    print("                                     BOVISA, MAGENTA VITTORE, LORETO, STADERA, VIGENTINA, GARIBALDI REPUBBLICA, LODI, TIBALDI, FORZE ARMATE, S. CRISTOFORO, PAGANO,")
    print("                                     PARCO LAMBRO, FARINI, PORTA ROMANA, GRECO, PADOVA, ORTOMERCATO, MACIACHINI, MAGGIORE, LORENTEGGIO, TRE TORRI, BARONA, ADRIANO,")
    print("                                     CORSICA, RONCHETTO SUL NAVIGLIO, SCALO ROMANA, QUARTO CAGNINO, EX OM, DERGANO, ROGOREDO, SELINUTE, GALLARATESE, MECENATE, QT 8,")
    print("                                     NIGUARDA GRANDA, RIPAMONTI, AFFORI, BAGGIO, PARCO MONLUE LAMBRO, GRATOSOGLIO, PARCO SEMPIONE, QUARTO OGGIARO, COMASINA, BOVISASCA,")
    print("                                     PARCO AGRICOLO SUD, PARCO NORD, BICOCCA, CHIARAVALLE, QUINTO ROMANO, TRIULZO SUPERIORE, BRUZZANO, FIGINO, PARCO DEI NAVIGLI,")
    print("                                     CANTALUPA, TRENN0, PARCO DELLE ABBAZIE, GIARDINI PORTA VENETA, PARCO BOSCO IN CITTÀ}")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    print("\nAttributi boolean disponibili:\n"
          "- host_is_superhost\n"
          "- is_center\n"
          "- cooking_basics\n"
          "- heating\n"
          "- long_term_stays_allowed\n"
          "- tv\n"
          "- iron\n"
          "- dishes_and_silverware\n"
          "- essentials\n"
          "- hangers\n"
          "- dedicated_worksapce\n"
          "- bed_linens\n"
          "- washer\n"
          "- hot_water\n"
          "- hair_dryer\n"
          "- kitchen\n"
          "- elevator \n"
          "- shampoo \n"
          "- air_conditioning\n"
          "- wifi\n"
          "- stove\n"
          "- refrigerator\n"
          "- oven\n"
          "- dishwasher\n"
          "- microwave\n"
          "- coffee_maker")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("\nInserisci le evidenze per la  belief network rispettando il seguente formato:")
    print("NomeAttributo = valore, NomeAttributo = valore, ...\n"
        "I nomi degli attributi devono essere scritti in minuscolo.")
    print("\nEsempio: host_is_superhost = True, class_of_price = economy")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")



def correct_input(options):
    """
    Richiede un input all'utente e verifica se è tra le opzioni valide.
    """
    while True:
        command = input().lower().strip()
        if command in options:
            return command
        print("Comando sbagliato, puoi inserire: ", options)

def dropping(answer):
    """
    Elimina le righe del DataFrame in base alle variabili Prolog non istanziate.
    """
    dataframe = pd.DataFrame(answer)
    canc = {index for index, row in dataframe.iterrows() if any(isinstance(row[col], psw.Variable) for col in dataframe.columns)}
    dataframe.drop(index=canc, inplace=True)
    return dataframe

def BNetwork_query():
    """
    Gestisce le query per la Belief Network.
    """
    b = BeliefNetwork(1)
    BF_help()
    while True:
        print("\nInserire le tue preferenze:")
        preferences = input().replace(' ', '')
        if re.match('((([a-z]+)([_]([a-z]+))*)([=])(([a-z|A-Z]+)([_]([a-z]+))*)([,]*))+', preferences):
            try:
                results = b.inference(b.compute_query(preferences))
                print("{:<15} {:<15}".format('RATING', 'PROBABILITY'))
                for key, value in results.items():
                    print("{:<15} {:<15}".format(key, value))
            except Exception as e:
                print("Error:", e)

            print("\nVuoi inserire un'altra query? [si, no]")
            response = correct_input(['si', 'no'])
            if response == 'no':
                break
        else:
            print("Formato non corretto. RIPETERE!")

def kbquery():
    """
    Gestisce le query per la Knowledge Base.
    """
    try:
        print("\nInserire una query per il KnowledgeBase:")
        query = input()
        answer = prg.query(query)
        answer_list = list(answer)
        if not answer_list:
            print("false")
        elif len(answer_list) == 1 and not answer_list[0]:
            print("true")
        else:
            dataframe = dropping(answer_list)
            print("OUTPUT:\n")
            print(dataframe)
    except Exception as e:
        print("Error:", e)

def help():
    """
    Stampa un menu di aiuto per l'utente.
    """
    print("\nMENU'\n")
    print("'aiuto' -> per visualizzare la lista dei comandi")
    print("'query' -> per inserire una query nel KB")
    print("'inference' -> per fare un'inference con Belief Network")
    print("'esci' -> per uscire\n")

def main():
    """
    Funzione principale che coordina l'esecuzione del programma.
    """
    print("\nCaricamento knowledge base...", end="", flush=True)
    prg.consult("./datasets/kb.pl")
    pd.set_option('display.max_rows', 3000, 'display.max_columns', 10)
    while True:
        help()
        print("Inserire:")
        command = input().strip().lower()
        if command == 'esci':
            break
        elif command == 'aiuto':
            help()
        elif command == 'query':
            while True:
                kbquery()
                print("\nVuoi inserire un'altra query? [si, no]")
                cont = correct_input(['si', 'no'])
                if cont == 'no':
                    break
        elif command == 'inference':
            BNetwork_query()
        else:
            print("comando ERRATO. RIPETERE!")
            help()

if __name__ == "__main__":
    main()