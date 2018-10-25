import zeep

# client = Client('https://aircon-select1-server.herokuapp.com/server.php?wsdl')
# result = client.service.post_aircon('81-987,31.5,40.56')
# print(result)

client = zeep.Client('https://aircon-select1-server.herokuapp.com/server.php?wsdl')
result = client.service.get_personal_data()
print(result)