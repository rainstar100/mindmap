#show workspace
pwd
#come into workfile
cd d:/pdb
#load pdb
##note , between params
load test.pdb,protein 
#get min_max of x,y,z
get_extent 

# select atoms based x,y,z
## Name selection
###auto named selection
select ,x<-37.61
###difine selection name pk1
select pk1,x<-37.61 

##identifier
#connect by ' ' for the same identifier
select , x<-37.61 x>23


#cal distance 
## select pk1 ,pk2
select pk1 , x<-37.61 and y<0
select pk2 , x>23.38 and y<0

# get pk1 and pk2

#cal distance 
##command line
distance dist1, pk1,pk2
## pymol api
dist=cmd.distance('dist','pk1','pk2')
print dist
hide everything
log_close

log_close

log_close
