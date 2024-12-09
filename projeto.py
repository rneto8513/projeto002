from funcoes import *
import matplotlib.pyplot as plt

logado = False
op = -1

while op != '0':
    print('[1] Cadastrar usuário')
    print('[2] Login')
    print('[0] Fechar programa')
    op = input('Digite a opção desejada: ').strip()

    while op not in opcoes_menu_inical:
        print("Opção inválida. Tente novamente.")
        op = input('Digite a opção desejada: ')

    if op == "1":
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')

        while '@gmail.com' not in email or verificar_usuario(email):
            if '@gmail.com' not in email:
                print("Email inválido, tente novamente.")
            else:
                print("Email já cadastrado, tente outro.")
            email = input('Digite seu email novamente: ')

        senha1 = input("Digite sua senha: ")
        senha2 = input("Confirme sua senha: ")

        while not verificar_senha(senha1, senha2):
            print("As senhas não coincidem. Tente novamente.")
            senha1 = input("Digite sua senha: ")
            senha2 = input("Confirme sua senha: ")

        usuarios[email] = {'nome': nome, 'senha': senha1}
        print("Usuário cadastrado com sucesso.")

    elif op == '2':
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')

        if login(email, senha):
            print('Usuário logado com sucesso.')
            logado = True

        while logado:
            menu_eventos()
            op_eventos = input('Digite a opção desejada: ')

            while op_eventos not in opcoes_menu_eventos:
                print("Opção inválida. Tente novamente.")
                op_eventos = input('Digite a opção desejada: ')

            if op_eventos == '3':
                cadastrar_evento(email)

            elif op_eventos == '4':
                busca = input('Digite o nome do evento que deseja encontrar: ')
                resultados = buscar_eventos(busca)
                if resultados:
                    print("Eventos encontrados:")
                    for evento in resultados:
                        print(f"Nome do evento: {evento['nome']}")
                        print(f"Descrição: {evento['descricao']}")
                        print(f"Data: {evento['data']}")
                        print(f"Local: {evento['local']}")
                        print(f"Valor da inscrição: {evento['valor']:.2f}")
                else:
                    print("Nenhum evento encontrado, tente novamente.")

            elif op_eventos == '5':
                listar_eventos(email)

            elif op_eventos == '6':
                listar_eventos(email)

            elif op_eventos == '7':
                remover_evento(email)

            elif op_eventos == '8':
                nome_do_evento = input('Digite o nome do evento: ')
                pagamento = input('Informe se o evento está pago ou não: ')
                inscricao(nome_do_evento, email, pagamento)

            elif op_eventos == '9':
                nome_do_evento = input("Digite o nome do evento: ")
                listar_participantes_evento(nome_do_evento, email, email)


            elif op_eventos == '10':
                nome_evento = input("Digite o nome do evento: ")
                verificar_valor_arrecadado(nome_evento, email)

            elif op_eventos == '11':
                if eventos:
                    nomes_evento = nomes_eventos(eventos)
                
                    qtd_participantes = contar_participantes(nomes_evento, inscricoes)

                    participantes_existem = False
                    if qtd_participantes > 0:
                        participantes_existem = True

                    if participantes_existem:
                        plt.bar(nomes_evento, qtd_participantes, color=['red', 'green', 'blue', 'yellow'])
                        plt.xlabel('Eventos')
                        plt.ylabel('Quantidade de Participantes')
                        plt.title('Quantidade de Participantes por Evento')
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Nenhum participante inscrito para exibir no gráfico.")
                else:
                    print("Nenhum evento cadastrado para exibir no gráfico.")
            elif op_eventos == '12':
                criar_planilha_eventos_participantes(email)

            elif op_eventos == '0':
                print('Saindo do menu de eventos...')
                logado = False
                break