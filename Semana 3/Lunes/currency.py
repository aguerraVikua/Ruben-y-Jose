currency_dict = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input("Please enter a currency (Euro, Dollar or Yen): ")
print(currency_dict.get(currency.title(),"Currency not found"))
