# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:56:09 2018

@author: alexkreamas
"""

from pydlm import dlm, trend, seasonality
import pandas as pd
import numpy as np
import scipy.stats
import rpy2.robjects as ro
from rpy2.robjects.packages import importr



class formulario:
    
    @staticmethod    
    def forecazt(datos, predice, zeazon):
        qq = scipy.stats.norm.ppf(0.5 * (1+0.95))

        n1 = datos
        m1 = dlm(n1) + trend(1, discount = 1, name = 'a') + seasonality(zeazon, discount = 1, name = 'b')
        m1.fit()

        
        cons = list(n1)
        opti = list(n1)
        pesi = list(n1)
        
        
        for i in range(predice):
            if i == 0:
                (p1Mean, p1Var) = m1.predict(date = m1.n-1)        
            else:
                (p1Mean, p1Var) = m1.continuePredict()
        
            mean1 = str(p1Mean[[0]])[3:]
            mean2 = np.float(mean1[:-2])
            
            cons.append(mean2)
        
            vari1 = str(np.sqrt(p1Var[[0]]))[3:]
            vari2 = np.float(vari1[:-2])
            
            opti.append(mean2 + qq * vari2)
            pesi.append(mean2 - qq * vari2)
        
        
            
        df = pd.DataFrame()
        df['optimista'] = opti
        df['conservador'] = cons
        df['pesimista'] = pesi
        
        return df