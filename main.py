from pytomaton import AFD, State

def main():
    print('Welcome to Pythomaton')
    keep_running = 1
    afd = AFD()     

    alphabet = input("Insira o alfabeto do autômato, separado por espaços (ex: 1 2 3): ")
    afd.set_alphabet(alphabet.split(' '))

    while keep_running == 1:
        print('1: Adicionar um novo estado')
        print('2: Consultar aceitação de palavras')
        print('0: Sair')
        option = int(input("Insira sua opção: "))

        if (option == 1):
            add_state(afd)
        elif (option == 2):
            accept_words(afd)

        keep_running = int(input("Deseja continuar a execução do programa? (0-Não, 1-Sim): "))

def add_state(afd):
    keep_adding_states = 1

    while (keep_adding_states):
        label = input("Insira o rótulo do estado: ex: 'q0': ")
        is_initial = int(input("O estado é inicial? (0-Não, 1-Sim): "))
        is_final = int(input("O estado é final? (0-Não, 1-Sim): "))
        state = State(label, is_initial, is_final)
        afd.add_state(state)
        keep_adding_states = int(input("Deseja continuar adicionando estados? (0-Não, 1-Sim): "))

    print("=========================================")
    print("Lendo funções de transições do arquivo txt", end='... ')
    afd.get_rules_from_file('afd.txt')    
    print("Feito! \n=========================================")

def accept_words(afd):
    words = input("Insira as palavras do autômato, separado por espaços (ex: 001 111 011): ")
    for word in words.split(' '):
        print(f"A palavra {word} foi ", afd.accepts(word))

main()