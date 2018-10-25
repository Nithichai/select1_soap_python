import zeep

client = zeep.Client('https://aircon-select1-server.herokuapp.com/server.php?wsdl')

def post_aircon():
  result = client.service.post_aircon('81-987,31.5,40.56')
  print(result)

def show_personal():
  result = client.service.get_personal_data()
  print(result)

show_personal()