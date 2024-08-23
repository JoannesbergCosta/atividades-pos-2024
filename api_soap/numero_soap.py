from zeep import Client
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = Client(wsdl=wsdl_url)

numero = int(input("Digite um número: "))

result = client.service.NumberToWords(
	ubiNum=numero
)
print(result)