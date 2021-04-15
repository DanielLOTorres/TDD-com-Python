from src.leilao.dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
Alex = Usuario('Alex')

lance_do_gui = Lance(gui, 100.0)
lance_do_alex = Lance(Alex, 150.0)

leilao = Leilao('Celular')
leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_alex)



print(f'{leilao.menor_lance} foi o menor lance e {leilao.maior_lance} foi o maior lance')