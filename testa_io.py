arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

print(type(arquivo.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes', 'latin_1')

contato = bytes('15,Verônica,veronica@email.com.br', 'latin_1\n')
arquivo.buffer.write(contato)

arquivo.close()