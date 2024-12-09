import pandas as pd

usuarios = {}
eventos = {}
inscricoes = []
opcoes_menu_inical = ['0', '1', '2']
opcoes_menu_eventos = ['0', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


def criar_planilha_eventos_participantes(usuario_logado):
    dados = []

    for nome_evento, detalhes_evento in eventos.items():
        if detalhes_evento['criador'] == usuario_logado:
            for inscricao in inscricoes:
                if inscricao[0] == nome_evento:
                    dados.append({
                        'Email do participante': inscricao[1],
                        'Nome do Evento': nome_evento,
                        'Status de Pagamento': inscricao[2],
                        'Data do evento': detalhes_evento['data'],
                    })
    if dados:
        df = pd.DataFrame(dados)
        df.to_excel('eventos_participantes.xlsx', index=False)
        print("Planilha 'eventos_participantes.xlsx' criada com sucesso.")
    else:
        print("Você não tem permissão para gerar a planilha ou não há eventos com inscrições.")


def nomes_eventos(eventos):
    nomes_eventos_temp = []
    for evento in eventos:
        nomes_eventos_temp.append(eventos[evento]['nome'])
    return nomes_eventos_temp


def contar_participantes(nomes_eventos, inscricoes):
    if not nomes_eventos:
        print("Nenhum evento fornecido.")
        return 0
    contador = 0
    for nome_evento in nomes_eventos:
        for inscricao in inscricoes:
            print(inscricao[0])
            if inscricao[0] == nome_evento:
                contador += 1
    return contador


def verificar_valor_arrecadado(nome_evento, criador_email):
    total_arrecadado = 0
    numero_inscritos = 0

    for inscricao in inscricoes:
        if inscricao[0] == nome_evento:
            numero_inscritos += 1
            if nome_evento in eventos and eventos[nome_evento]['criador'] == criador_email:
                total_arrecadado += eventos[nome_evento]['valor']

    if numero_inscritos > 0:
        valor_por_participante = total_arrecadado / numero_inscritos
    else:
        valor_por_participante = 0

    print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
    print(f"Número de inscritos: {numero_inscritos}")
    print(f"Valor total por participante: R$ {valor_por_participante:.2f}")


def listar_participantes_evento(nome_evento, criador_email, usuario_email):
    if nome_evento in eventos and eventos[nome_evento]['criador'] == criador_email:
        if usuario_email != criador_email:
            print("Permissão negada: Apenas o criador do evento pode criar a lista de participantes.")
            return

        print(f"Lista de participantes do evento '{nome_evento}':")
        participantes_encontrados = False

        with open(f'participantes_{nome_evento}.txt', 'w') as arquivo:
            for inscricao in inscricoes:
                if inscricao[0] == nome_evento:
                    print(f"email: {inscricao[1]}, Status de Pagamento: {inscricao[2]}")
                    arquivo.write(f"email: {inscricao[1]}, Status de Pagamento: {inscricao[2]}\n")
                    participantes_encontrados = True
            
            if not participantes_encontrados:
                print("Nenhum participante inscrito neste evento.")
                arquivo.write("Nenhum participante inscrito neste evento.\n")
            else:
                print(f"Lista de participantes salva em 'participantes_{nome_evento}.txt'.")
    else:
        print("Evento não encontrado ou você não tem permissão para visualizá-lo.")
            



def inscricao(nome_do_evento, usuario_nome, pagamento):
    encontrado = False
    if nome_do_evento in eventos and pagamento.lower() == 'pago':
        encontrado = True
        print('Inscrição realizada com sucesso.')
        inscricoes.append([nome_do_evento, usuario_nome, pagamento])

    if not encontrado:
        print('O evento que você deseja se inscrever não foi encontrado ou pagamento não foi realizado.')


def buscar_eventos(busca):
    resultado = []
    for evento in eventos.values():
        if busca in evento['nome'] or busca in evento['descricao'] or busca in evento['data'] or busca in evento[
            'local']:
            resultado.append(evento)
    return resultado

def listar_eventos(email=None):
    if email is None:
        resultado = eventos.values()  
    else:
        resultado = [evento for evento in eventos.values() if evento['criador'] == email]

    if resultado:
        print("Eventos encontrados:")
        for evento in resultado:
            print(f"Nome do evento: {evento['nome']}")
            print(f"Descrição: {evento['descricao']}")
            print(f"Data: {evento['data']}")
            print(f"Local: {evento['local']}")
            print(f"Valor da inscrição: R${evento['valor']:.2f}\n")
    else:
        print("Nenhum evento encontrado.")

def remover_evento(email):
    if listar_eventos(email):
        nome_evento = input("Digite o nome do evento que deseja remover: ")

    if nome_evento in eventos and eventos[nome_evento]['criador'] == email:
        confirmacao = input("Tem certeza que deseja remover este evento? (s/n): ")
        if confirmacao.lower() == 's':
            del eventos[nome_evento]
            print("Evento removido com sucesso.")
        else:
            print("Remoção de evento cancelada.")
    else:
        print("Evento não encontrado ou você não tem permissão para removê-lo.")


def menu_eventos():
    print('[3] Cadastrar eventos')
    print('[4] Buscar eventos')
    print('[5] Listar todos os eventos')
    print('[6] Listar meus eventos')
    print('[7] Remover um evento')
    print('[8] Participar de um evento')
    print('[9] Listar participantes e criar arquivo txt')
    print('[10] Valor arrecadado')
    print('[11] criar grafico dos eventos')
    print('[12] criar planilha dos eventos')
    print('[0] Sair do menu de eventos')


def login(email, senha):
    if email in usuarios and usuarios[email]['senha'] == senha:
        return True
    else:
        print('Login ou senha errados, tente novamente.')
        return False


def verificar_usuario(email):
    for user in usuarios:
        if user == email:
            return True
    return False


def verificar_senha(senha, senha2):
    return senha == senha2


def cadastrar_evento(email):
    nome_evento = input('Digite o nome do evento: ')
    descricao = input('Descrição do evento: ')
    data = input('Informe a data do evento (DDMMAAAA): ')
    local = input('Informe o local do evento: ')
    valor = float(input('Informe o valor da inscrição: '))

    eventos[nome_evento] = {'nome': nome_evento, 'descricao': descricao, 'data': data, 'local': local, 'valor': valor,'criador': email}
    print("Evento cadastrado com sucesso!")
