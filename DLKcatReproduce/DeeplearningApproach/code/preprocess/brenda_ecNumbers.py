#import packages
from zeep import Client
import hashlib
import pandas as pd

#create client of brenda
wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
client = Client(wsdl).service

#set email and password
email="23122842@qq.com"
password="12345678"
password = hashlib.sha256(password.encode("utf-8")).hexdigest()

#request
response=client.getEcNumbersFromTurnoverNumber(email,password)

#save response in currentpath
df=pd.DataFrame(response)
output_path='./DLKcat-reproduce/DeeplearningApproach/code/preprocess/'
df.to_csv(output_path+'brenda_ecNumbers.csv',index=False,encoding='utf-8') # without index
print('saved')