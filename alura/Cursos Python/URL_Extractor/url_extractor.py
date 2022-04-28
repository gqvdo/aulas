url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

question_mark = url.find("?")
url_base = url[:question_mark]
url_parameter = url[question_mark+1:]
parameter_search = "moedaOrigem"
parameter_index = url_parameter.find(parameter_search)
value_index = parameter_index + len(parameter_search) + 1
value = url_parameter[value_index:]

print("URL:", url)
print("Base:", url_base)
print("Parameter:", url_parameter)
print("Value: ", value)