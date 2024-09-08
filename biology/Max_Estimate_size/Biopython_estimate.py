from Bio.PDB import PDBParser
import pandas as pd

# parser pdb
parser=PDBParser()
struc=parser.get_structure(id="1",file="test.pdb")

#get xyz of atom
atoms=struc.get_atoms()
coords=[]
for atom in atoms:
    coords.append(atom.get_coord())
    
# calculate 
df=pd.DataFrame(coords,columns=['x','y','z'])
size=(df.max()-df.min()).max()
print('the max estimated size --- {:.0f} ANG'.format(size))