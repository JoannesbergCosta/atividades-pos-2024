import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

country_city = "NO"

result = client.service.CapitalCity(
sCountryISOCode=country_city
)

print(f"O código de telefone do {country_city} é {result}")