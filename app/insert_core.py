from core import user_table, engine

con = engine.connect()
insert = user_table.insert()

# new = ins.values(idade=25, nome='Caio', senha='abacaxi123')
# con.execute(new)

con.execute(user_table.insert(), [
    {'nome': 'marcio', 'idade':20, 'senha':'limao321'},
    {'nome':'gustavo', 'idade':18, 'senha': 'goiaba123'},
    {'nome':'guilherme', 'idade':22, 'senha':'maracuja456'}

])
