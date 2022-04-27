#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
filepath = r'C:\Users\dholl\OneDrive\Documents\COMP_5650_DL\finalproject\Neck_Rotation.csv'
vicon = pd.read_csv(filepath, skiprows = [0, 1, 3, 4])
vicon = vicon.iloc[:, 2:]
vicon.head()


# In[13]:


# Obtain all segments for frame 1
RUPA_segmentX = vicon['Test1:RSHO'] - vicon['Test1:RUPA']
vicon['RUPA_segmentX'] = RUPA_segmentX
vicon['RUPA_segmentY'] = RUPA_segmentY
vicon


# In[10]:


RSHO_col = 'Test1:RSHO'
RUPA_col = 'Test1:RUPA'

RSHO_index_no = vicon.columns.get_loc(RSHO_col)
RSHO_X = vicon.iloc[:, RSHO_index_no]
RSHO_Y = vicon.iloc[:, RSHO_index_no + 1]

RUPA_index_no = vicon.columns.get_loc(RUPA_col)
RUPA_X = vicon.iloc[:, RUPA_index_no]
RUPA_Y = vicon.iloc[:, RUPA_index_no + 1]

RUPA_segmentX = RSHO_X - RUPA_X
RUPA_segmentY = RSHO_Y - RUPA_Y

len(RUPA_segmentX), len(RUPA_segmentY)


# In[12]:





# In[ ]:




