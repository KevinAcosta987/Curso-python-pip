import utilis
import charts
import read_csv

'''
def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type country => ')
  result = utilis.population_by_countri(data,country)
  if len(result) > 0:
    #print(result)
    country = result[0]
    años,pop = utilis.get_population(country)
    #print("años =>",años,"poblacion =>",pop)
    charts.generate_bar_chart(años, pop)
'''

'''
def Grafico_torta():
  data = read_csv.read_csv('./app/data.csv')
  dato_graficar = input("Ingrese la columna que desea graficar => ")
  #print(data)
  #print("***" *4)
  print(dato_graficar)
  result,paises = utilis.elemento_grafica(data,dato_graficar)
  #print(result)
  #print(paises)
  charts.generate_pie_chart(paises, result)
  '''
  
#Como se hizo en platzi:
def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type country => ')
  result = utilis.population_by_countri(data,country)
  print(result)

  if len(result) > 0:
    datos_pais = result[0]
    labels, values = utilis.get_population(datos_pais)
    charts.generate_bar_chart(country, labels, values)

'''
  keys, values = utilis.get_population()
  dict_pop_pais = [{keys[0]:values[0]},{keys[1]:values[1]}]
  
  print(keys,values)
  print(dict_pop_pais)
  print(utilis.A)
  
  data =[
    {
      'country':'col',
      'pop':500
    },
    {
      'country':'bol',
      'pop':300
    }
  ]
'''  

if __name__ == '__main__':
  run()
  #Grafico_torta()