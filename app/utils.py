import re

def World_population(percentage):
  world = {}
  for t in percentage:
    country = t['Country/Territory']
    world[country] = float(t['World Population Percentage'])
  return world
    

def get_population(country_dict):
  dic = {}
  for k in country_dict:
    key = re.findall('Population', k)
    if key != []:
      values = country_dict[k]
      keys = re.findall('[0-9]+', k)
      if keys != []:
        dic[keys[0]] = int(values)
  k = dic.keys()
  v = dic.values()
  return k, v

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result
