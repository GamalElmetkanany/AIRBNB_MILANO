from pgmpy.readwrite import XMLBIFReader
from pgmpy.inference import VariableElimination

class BeliefNetwork:
    model = None
    inference_method = None
    beliefNet_structure = None
    data_path = './datasets/bn_dataset.csv'

    def __init__(self, i):
        """
        Costruttore della classe BeliefNetwork.

        :param i: Parametro non utilizzato nel costruttore.
        """
        self.beliefNet_structure ='./datasets/bnStructure_1_parent.xml'
        reader = XMLBIFReader(self.beliefNet_structure)
        self.model = reader.get_model()
        self.inference_method = VariableElimination(self.model)

    def inference(self, preferences_dictionary):
        """
        Esegue un'infrazione sulla rete bayesiana e restituisce i risultati.

        :param preferences_dictionary: Dizionario contenente le preferenze come evidenza per l'infrazione.
        :return: Dizionario contenente i risultati dell'infrazione.
        """
        results_dictionary = {}
        result = self.inference_method.query(variables=['review_scores_rating'], evidence=preferences_dictionary)
        results_dictionary['top_rating'] = result.get_value(review_scores_rating='top_rating').round(4)
        results_dictionary['nice_rating'] = result.get_value(review_scores_rating='nice_rating').round(4)
        results_dictionary['good_rating'] = result.get_value(review_scores_rating='good_rating').round(4)
        results_dictionary['low_rating'] = result.get_value(review_scores_rating='low_rating').round(4)
        return results_dictionary

    def compute_query(self, input_string):
        """
        Elabora una stringa di input e restituisce un dizionario di preferenze.

        :param input_string: Stringa contenente le preferenze separate da virgola nel formato 'chiave=valore'.
        :return: Dizionario contenente le preferenze elaborate dalla stringa di input.
        """
        input_string = input_string
        preferences_list = input_string.split(",")
        preferences_dictionary = {}
        for item in preferences_list:
            key = (item.split("=")[0])
            value = str(item.split("=")[1])
            preferences_dictionary[key] = value
        return preferences_dictionary
