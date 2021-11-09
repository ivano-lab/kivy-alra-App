from datetime import date, datetime
from dateutil.relativedelta import relativedelta

data = date.today()
#data_compra = f'{data.day}/{data.month}/{data.year}'
data_compra = data.strftime('%d/%m/%Y')
relativo = relativedelta(days=+365)
devolucao = data + relativo
#data_devolucao = f'{devolucao.day}/{devolucao.month}/{devolucao.year}'
data_devolucao = devolucao.strftime('%d/%m/%Y')
devolucao = str(devolucao)

print(data, type(data))
print(data_compra, type(data_compra))
print(relativo, type(relativo))
print(data_devolucao, type(data_devolucao))
print(devolucao, type(devolucao))
#print()