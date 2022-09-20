contato_carol = '11,Carol,carol@email.com.br\n'
contato_andreza = '12,Andreza,andreza@email.com.br\n'

with open('dados/contatos-escrita.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('dados/contatos-escrita.csv', encoding='latin_1', mode='a')as arquivo2:
    arquivo2.write(contato_andreza)