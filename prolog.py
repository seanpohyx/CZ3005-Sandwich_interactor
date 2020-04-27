from pyswip import Atom
from mtpl import PrologMT

class PrologLogic:

    def __init__(self):
        self.p = PrologMT()
        self.p.consult("knowledge_base.pl")

    def atoms_to_strings(self, answer):
        if isinstance(answer, dict):
            result = {}
            for k in answer.keys():
                result[k] = self.atoms_to_strings(answer[k])
        elif isinstance(answer, list):
            result = [self.atoms_to_strings(val) for val in answer]
        elif isinstance(answer, Atom):
            result = answer.value
        elif isinstance(answer, int) or isinstance(answer, str):
            result = answer
        else:
            print("Unsupported result from Prolog: " + str(type(answer)) + str(answer))
        return result

    def get_query(self, query):
        val = list(self.p.query(query))
        return self.atoms_to_strings(val)

    def assert_query(self, query):
        self.p.asserta(query)

    def retract_all_query(self, query):
        self.p.retractall(query)





