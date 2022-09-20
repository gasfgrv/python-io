arquivos_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w+')

contatos =  [
    '11,Carol,carol@email.com.br\n'
    '12,Ana,ana@email.com.br\n',
    '13,Tais,tais@email.com.br\n',
    '14,Felipe,felipe@email.com.br\n'
]

for contato in contatos:
    arquivos_contatos.write(contato)

arquivos_contatos.flush()

arquivos_contatos.seek(28)

for linha in arquivos_contatos:
    print(linha, end='')
