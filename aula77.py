# Exercício - sistema de pergunsa e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'], '\n')

    for indeices, opcoes in enumerate(pergunta['Opções']):
        print(f'{indeices}) {opcoes}')

    user = input('\nEscolha a sua opção')

    user_int = None
    if user.isdigit():
        user_int = int(user)