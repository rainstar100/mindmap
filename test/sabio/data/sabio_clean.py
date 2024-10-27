import pandas as pd
def replace_substrate(row):
    longest=max(row,key=len)
    if len(longest)>=6:
        return longest
    else:
        return None

#import data
df=pd.read_csv('sabio_combine_csv.csv',encoding='utf-8',low_memory=False)
#query kcat
#query interested data
kcat_query=(df['parameter.type']=='kcat')
kcat=df[kcat_query]
print(f'before clean1, the shape is {kcat.shape}')
#query kcat
#query interested data
kcat_query=(df['parameter.type']=='kcat')
kcat=df[kcat_query]
print(f'before clean1, the shape is {kcat.shape}')
#replace substrate
df_split=kcat['Substrate'].str.split(';',expand=True).fillna('1')

newSubstrate=df_split.apply(replace_substrate,axis=1)
print(newSubstrate.index==kcat.index)
kcat.loc[:,'Substrate']=newSubstrate
#clean kcat
#clean dataset
##clean1 clean unit UniprotID,startValue
clean_unit=(kcat['parameter.unit']=='s^(-1)')
clean_UniprotID=(kcat['UniprotID'].notna())&(df['UniprotID'].str.len()==6)
clean_startValue=(kcat['parameter.startValue'].notna())
clean_substrate=(kcat['Substrate'].notna())
kcat_cleaned=kcat[clean_unit&clean_UniprotID&clean_startValue&clean_substrate]
print(f'after clean1 the shape is {kcat_cleaned_unique.shape}')
#value data
data=pd.DataFrame()
data.loc[:,'ECNumber']=kcat_cleaned['ECNumber']
data.loc[:,'Organism']=kcat_cleaned['Organism']
data.loc[:,'Smiles']=''
data.loc[:,'Sequence']=''
data.loc[:,'Substrate']=kcat_cleaned['Substrate']
data.loc[:,'Value']=kcat_cleaned['parameter.startValue']
data.loc[:,'Unit']=kcat_cleaned['parameter.unit']
data.loc[:,'UniprotID']=kcat_cleaned['UniprotID']
data.to_csv('sabio_cleaned.csv',index=False,encoding='utf-8')