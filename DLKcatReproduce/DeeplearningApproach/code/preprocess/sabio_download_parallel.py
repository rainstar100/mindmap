import requests
from tools.parallel import parallel
from tools.decorator import timetry
from tools.tool import devideIterator
import numpy as np

# Extract EC number list from ExPASy, which is a repository of information relative to the nomenclature of enzymes.
def eclist():
    with open('./Data/EC_enzyme/enzyme.dat', 'r') as outfile :
        lines = outfile.readlines()

    ec_list = list()
    for line in lines :
        if line.startswith('ID') :
            ec = line.strip().split('  ')[1]
            ec_list.append(ec)
    # print(ec_list)
    print(len(ec_list)) # 7906
    return ec_list

@timetry   # try*100
def sabio_info(param):
        QUERY_URL = 'http://sabiork.h-its.org/sabioRestWebServices/kineticlawsExportTsv'

    # specify search fields and search terms

    # query_dict = {"Organism":'"lactococcus lactis subsp. lactis bv. diacetylactis"', "Product":'"Tyrosine"'}
    # query_dict = {"Organism":'"lactococcus lactis subsp. lactis bv. diacetylactis"',} #saccharomyces cerevisiae  escherichia coli
    # query_dict = {"ECNumber":'"1.1.1.1"',}
        EC=param
        print(EC)
        query_dict = {"ECNumber":'%s' %EC,}
        query_string = ' AND '.join(['%s:%s' % (k,v) for k,v in query_dict.items()])


        # specify output fields and send request

        query = {'fields[]':['EntryID', 'Substrate', 'EnzymeType', 'PubMedID', 'Organism', 'UniprotID','ECNumber','Parameter'], 'q':query_string}
        # the 'Smiles' keyword could get all the smiles included in substrate and product

        request = requests.post(QUERY_URL, params = query)
        # request.raise_for_status()


        # results
        results = request.text
        #print(results)
        #print('---------------------------------------------')

        if results :
            with open('./Data/database/Kcat_sabio_4/%s.txt' %EC, 'w',encoding='utf-8') as ECfile :
                ECfile.write(results)



if __name__ == '__main__' :
    #parallel request

    allEC = eclist() #all params
    params_pool=devideIterator(allEC,20)

    for params in params_pool:
        parallel(sabio_info,params)


