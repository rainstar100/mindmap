'''
Author:T.Student
Date:20240907 

'''
import math

def EquilibriumConcentrate(pKa,HA,A):
    '''
    #######################################################
    Params:
        pKa: the dissociation equilibrium constant of [HA] in water
        HA:  concentrate of [HA] when equilibrium
        A:   concentrate of [A-] when equilibrium 
    
    ###################################################### 
    Calculate the pH according as follow:
        [HA]+[H2O]=[A-]+[H3O+]
    when equilibrium:
        Ka=[A-][H3O+]/[HA]
    Derivation:
        [H3O+]=Ka[HA]/[A-]
        log10([H3O+])=log10(Ka)+log10([HA]/[A-])
    Replace:
        pka=-log10(Ka)
        pH=-log10([H3O+])    
    Resultes:
        pH=pKa-log10([HA]/[A-])
    '''
    pH=pKa-math.log10(HA/A)
    print('the buffer ph---->{:.2f}'.format(pH))
    return pH

def InitialConcentrate(pKa,HA,approximate=True):
    '''
    #######################################################
    Params:
        pKa: the dissociation equilibrium constant of [HA] in water
        HA:  initial concentrate of [HA] 
            [HA] of equilibrium ≈initial [HA] ,because 10**-pKa is very small
        approximate: 
            True:[HA] of equilibrium ≈initial [HA] ,because 10**-pKa is very small,dissociate fewly
    ###################################################### 
    Calculate the pH according as follow:
        [HA]+[H2O]=[A-]+[H3O+]
    when equilibrium:
        Ka=[A-][H3O+]/[HA]
    Derivation:
        [H3O+]2=Ka[HA]
        2*log10([H3O+])=log10(Ka)+log10([HA])
        log10([H3O+])=(log10(Ka)+log10([HA]))/2
    Replace:
        pka=-log10(Ka)
        pH=-log10([H3O+])    
    Resultes:
        pH=(pKa-log10([HA]))/2
    '''
    pH=(pKa-math.log10(HA))/2
    print('the buffer ph approximate---->{:.2f}'.format(pH))
    return pH