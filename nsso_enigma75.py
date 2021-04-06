#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
class data_cleaning(object):
    def __init__(self, file, supportfile):
        self.file = file
        self.supportfile = supportfile
    def reading_file(self):
        Data = pd.read_csv(self.supportfile, engine = "python")
        Data.index = range(1,len(Data.index)+1)
        return Data
    def headerconv(self):
        R = self.reading_file()
        Clean = R.iloc[:,0].dropna().astype(str).to_list()
        return Clean
    def numconv(self):
        R = self.reading_file()
        Clean = R.iloc[:,1].dropna().astype(int).to_list()
        return Clean
    def reading_Data(self):
        con = self.numconv()
        Data1 = pd.read_fwf(self.file, widths = con,header = None)
        headers = self.headerconv()
        Data1.columns = headers
        return Data1
    def changed_values(self):
        file = self.reading_file()
        Encode = file.iloc[:,2]
        Data = self.reading_Data()
        for i in range(1,len(Encode)):
            if Encode[i] == "Yes":
                Dict = dict(file[file.iloc[:,0][i]].dropna().astype(str))
                Data.replace({file.iloc[:,0][i]:Dict},inplace = True)
                Dict = {}
        if Data.columns[0] == "Common-ID":
            Data["HHID"] = Data["Common-ID"].str.slice(3,34)
            Data['NSS_Region']= Data["HHID"].str.slice(12,15)
            Data["State_Code"] = Data['NSS_Region'].str.slice(0,2)
            Data["Dist_Code"] = Data["HHID"].str.slice(15,17)
        return Data

