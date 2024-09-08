from pymol import cmd
import pandas as pd 
cmd.load('test.pdb','test')
xyz=cmd.get_extent()
df=pd.DataFrame(xyz,columns=['x','y','z'])
size=(df.max()-df.min()).max()
print('the max estimated size --- {:.0f} ANG'.format(size))