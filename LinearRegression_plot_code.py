# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:04:13 2020

@author: ray
"""

def linearRegression():
    
    import csv
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.linear_model import LinearRegression
    
    with open ('hubble_data.csv') as csv_file: #open your .csv file here
        
        datax=[]
        datay=[]
        
        csv_reader= csv.reader (csv_file, delimiter=',') # it will read your data line by line
        csv_reader.__next__() # it will ignore the first line, that describes the columns
        
        for row in csv_reader: #adding the data to the empty lists (datax and datay)
            datax.append(float(row[0]))
            datay.append(int(row[1]))
        
        x=np.array(datax) #nedded transformations to LinearRegression() works
        y=np.array(datay) 
        regr = LinearRegression()
        regr.fit(x.reshape(-1,1),y)
        
        a = regr.coef_ #angular coefficient
        b = regr.intercept_ #linear coefficient
        
        plt.scatter(x,y, s=15, color='green') #to plot your data
        
        ax=plt.axes()
        plt.style.use('fivethirtyeight')
        plt.title('Linear Regression')
        ax= ax.set(xlabel='distance', ylabel='velocity')
        plt.plot(datax,(x*a+b), color= 'purple') #calculating the linear regression, where y=x*a+b
        plt.savefig('LinearRegression.png') #choose the directory and the figure name to save
        plt.show()
linearRegression()