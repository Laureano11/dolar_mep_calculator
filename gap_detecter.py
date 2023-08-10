import requests
from bs4 import BeautifulSoup
global BLUE_PRICE
global GD30_PRICE
global GD30D_PRICE
global MEP_PRICE
saldo= 5500

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




dolar_hoy = requests.get("https://dolarhoy.com/")
soup= BeautifulSoup(dolar_hoy.text, 'html.parser')
sell_price = soup.find_all('div',class_='venta')

string_BLUE= sell_price[9].text.replace(".","")
BLUE_PRICE=int(string_BLUE[0:3])


gd_30= requests.get("https://iol.invertironline.com/titulo/cotizacion/BCBA/GD30/BONOS-REP.-ARG.-U-S-STEP-UP-V.09-07-30/")
gd_30d= requests.get("https://iol.invertironline.com/titulo/cotizacion/BCBA/GD30D/BONOS-REP.-ARG.-U-S-STEP-UP-V.09-07-30/")

soup1= BeautifulSoup(gd_30.text,'html.parser')
spans_gd30=soup1.find('span', id='IdTitulo').text

soup2=BeautifulSoup(gd_30d.text,'html.parser')
spans_gd30d=soup2.find('span', id='IdTitulo').text

GD30_PRICE= int(spans_gd30[3:9].replace(".",""))
GD30D_PRICE= int(spans_gd30d[5:9].replace(",", ""))/10
MEP_PRICE= round((GD30_PRICE/GD30D_PRICE),3)

diferencia=round((BLUE_PRICE-MEP_PRICE),1)
ganancia=round(((diferencia*saldo)/MEP_PRICE ), 2)


print("La diferencia es de \033[92m {} \033[0m y la ganancia es de \033[92m {} \033[0m".format(diferencia,ganancia))


print("Blue PRICE: \033[94m {} \033[0m".format(BLUE_PRICE))
print("MEP PRICE: \033[94m {} \033[0m".format(MEP_PRICE))


#print("Price GD30:",GD30_PRICE)
#print("Price GD30D:", GD30D_PRICE)
















    
    
    

