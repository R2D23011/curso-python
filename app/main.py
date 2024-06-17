import utils
import read_csv
import charts
import pandas as pd

def run():
  Opciones = ('Asia', 'Africa', 'North America', 'South America', 'Europe', 'Oceania')
  df = pd.read_csv('data.csv')
  # data = read_csv.read_csv('data.csv')
  
  
  El_print= input('Elige una opción (World o Country) => ').lower()
 
  
  if El_print == 'world':

    print('Asia, Africa, North America, South America, Europe, Oceania')
    Continente = input('Ingrese el continente =>').title()

    if Continente in Opciones:
      # data = list(filter(lambda item: item['Continent'] == Continente, data))
      df = df[df['Continent'] == Continente]
    else:
      print('No se encuentra el continente, se imprimira la poblacion mundial')
    #countries = list(map(lambda x: x['Country/Territory'], data))
    countries = df['Country/Territory'].values

    #percentages = list(map(lambda x: x['World Population Percentage'], data))
    percentages = df['World Population Percentage'].values

    charts.generate_pie_chart(Continente, countries, percentages)
    

  elif El_print == 'country':

  
    country = input('Type Country => ').title()
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
      country = result[0]
      labels, values = utils.get_population(country)
      charts.generate_bar_chart(country['Country/Territory'], labels, values)

  if El_print != 'world' and El_print != 'country':
    print('No es una opción valida')
    
if __name__ == "__main__":
  run()