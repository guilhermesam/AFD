from collections import defaultdict

class State:
    def __init__(self, label, is_initial=False, is_final=False):
        self.label = label
        self.transitions = {}
        self.is_initial = is_initial
        self.is_final = is_final

    def add_transiction(self, key, state):
        self.transitions.update({(self.label, key):state.label})

    def get_label(self):
        return self.label

class AFD:
    def __init__(self):
        self.initial_state = None
        self.final_states = []
        self.alphabet = []
        self.states = []
        self.rules = {}

    def get_state_by_label(self, label):
        for state in self.states:
            if state.label == label:
                return state

    def set_initial_state(self, state):
        self.initial_state = state

    def set_final_states(self, states):
        self.final_states = states

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def add_state(self, state):
        if state.is_initial and self.initial_state is None:
            self.initial_state = state
        if state.is_final:
            self.final_states.append(state)
        
        for key in state.transitions.keys():
            if key[1] not in self.alphabet:
                raise SymbolOutOfAlphabet("Símbolo não pertence ao alfabeto!")

        self.states.append(state)
        self.rules.update(state.transitions)

    def accepts(self, word):
        if self.initial_state is None:
            raise InitialStateNotDefinedException("Estado inicial não está definido!")
        if len(self.final_states) == 0:
            raise FinalStateNotDefinedException("Estados finais não definidos")

        current_state = self.initial_state.label
        for letter in word:
            query = self.rules[(current_state, letter)]
            current_state = query
        if current_state in list(map(State.get_label, self.final_states)):
            return 'aceita'
        else:
            return 'rejeitada'

    def _delete_unreachable_states(self):
        values = self.rules.values()
        useless_states = []
        for state in self.states:
            if state.label not in values:
                useless_states.append(state.label)
                self.states.remove(state)
        for key in list(self.rules):
            if (key[0] in useless_states):
                del self.rules[key]

    def _get_rules(self):
        for state in self.states:
            self.rules.update(state.transitions)

    def get_rules_from_file(self, filepath):
        with open(filepath) as f:
            for line in f.readlines():
                key, value = line.split(':')
                key = tuple(eval(key.replace('\n', '')))
                if key[1] not in self.alphabet:
                    raise SymbolOutOfAlphabet('Símbolo não pertence ao alfabeto!')
                self.rules[key] = value.replace('\n', '').replace("'", '')


class InitialStateNotDefinedException(Exception):
    """Estado inicial do AFD não foi definido"""
    pass


class FinalStateNotDefinedException(Exception):
    """Estado(s) final(is) não definidos"""
    pass


class SymbolOutOfAlphabet(Exception):
    """Símbolo não pertence ao alfabeto"""
    pass

#rules = {('q1','0'):'q1',('q1','1'):'q2',('q2','1'):'q2',('q2','0'):'q3',('q3','0'):'q2',('q3','1'):'q2'}

"""
afd = AFD()
q1 = State('q1', is_initial=True)
q2 = State('q2', is_final=True)
q3 = State('q3')

q1.add_transiction('0', q1)
q1.add_transiction('1', q2)
q2.add_transiction('0', q3)
q2.add_transiction('1', q2)
q3.add_transiction('0', q2)
q3.add_transiction('1', q2)

afd.set_alphabet(['0', '1'])

afd.add_state(q1)
afd.add_state(q2)
afd.add_state(q3)

afd.accepts('011')
"""
