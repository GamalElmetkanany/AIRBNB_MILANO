# AIRBNB_Milano

# Esecuzione 
## Fase iniziale
Installare SWIProlog (installare la versione a 64 bit)

<code>https://www.swi-prolog.org/download/stable/bin/swipl-8.2.4-1.x64.exe.envelope</code>

<code> cd AIRBNB_Milano </code>

Installare le dipendenze:

<code>pip install -r requirements.txt</code>

## Esecuzione del codice

**Importante eseguire i run nell'ordine in cui sono posti almeno per la prima volta**<br>

 Fase di preprocessing <br>

<code> python preprocessing/cleaning.py ./datasets/listings.csv </code>
 
 Creazione dei clusters <br>

<code> python clustering/clustering.py ./datasets/cleaned_dataset.csv [number of clusters] [number of iterations] </code>
 
 Creazione Knowledge Base <br>

<code> python KnowledgeBase/Kb.py ./datasets/prolog_dataframe.csv </code>
 
 User Interface per porre query al sistema<br>

<code> python BeliefNetwork/ui.py </code>


