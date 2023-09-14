#Como crear tus propios módulos
#cada .py es un modulo
def get_population(country):
  '''
  keys = ['col','bol']
  values = [300,400]
  '''
  population = {
    '2022':int(country['2022 Population']),
    '2020':int(country['2020 Population']),
    '2015':int(country['2015 Population']),
    '2010':int(country['2010 Population']),
    '2000':int(country['2000 Population']),
    '1990':int(country['1990 Population']),
    '1980':int(country['1980 Population']),
    '1970':int(country['1970 Population'])
  }
  return population.keys(), population.values()

A = 'Hola'

def population_by_countri(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,data))
  return result

def elemento_grafica(data,elemento):
  result = []
  paises = []
  for element in data:
    #print(elemento)
    #element.keys()
    for columnas in element:
      #print(columnas)
      if columnas == elemento:
        paises.append(element.get('Country/Territory'))
        result.append(int(element.get(columnas)))
  return result, paises