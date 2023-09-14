#los csv son los archivos mas comunes a trabajar
#pasos a seguir:

#importo las funciones
import csv

#defino una funcion para leerlo:
'''
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      print('***' * 5)
      print(row)
'''
#como tenerlo como un dict en ves de una lista y asi poder usar keys:

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      #print(country_dict)
      data.append(country_dict)
    return data

#inicializo:
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])


