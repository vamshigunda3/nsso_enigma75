#!/usr/bin/env python
# coding: utf-8

# In[24]:

# In[26]:
import nsso_enigma75 as ne

D1 = ("./Data/R75252L01.TXT")
L1 = ("./Levels/Level_1.csv")
D2 = ("./Data/R75252L02.TXT")
L2 = ("./Levels/Level_2.csv")
D3 = ("./Data/R75252L03.TXT")
L3 = ("./Levels/Level_3.csv")
D4 = ("./Data/R75252L04.TXT")
L4 = ("./Levels/Level_4.csv")
D5 = ("./Data/R75252L05.TXT")
L5 = ("./Levels/Level_5.csv")
D6 = ("./Data/R75252L06.TXT")
L6 = ("./Levels/Level_6.csv")
D7 = ("./Data/R75252L07.TXT")
L7 = ("./Levels/Level_7.csv")
D8 = ("./Data/R75252L08.TXT")
L8 = ("./Levels/Level_8.csv")


# In[27]:


Data1 = ne.data_cleaning(D1,L1)
Data2 = ne.data_cleaning(D2,L2)
Data3 = ne.data_cleaning(D3,L3)
Data4 = ne.data_cleaning(D4,L4)
Data5 = ne.data_cleaning(D5,L5)
Data6 = ne.data_cleaning(D6,L6)
Data7 = ne.data_cleaning(D7,L7)
Data8 = ne.data_cleaning(D8,L8)


# In[28]:


def level_1():
    Df1 = Data1.changed_values()
    return Df1
def level_2():
    Df2 = Data2.changed_values()
    return Df2
def level_3():
    Df3 = Data3.changed_values()
    return Df3
def level_4():
    Df4 = Data4.changed_values()
    return Df4
def level_5():
    Df5 =Data5.changed_values()
    return Df5
def level_6():
    Df6 = Data6.changed_values()
    return Df6
def level_7():
    Df7 = Data7.changed_values()
    return Df7
def level_8():
    Df8 = Data8.changed_values()
    return Df8
