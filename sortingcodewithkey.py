# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:59:08 2023

@author: nikil
"""
import os
import shutil






keys = ['DRW','LPI','DCN','SPC','AIPI','AIMS','ABS','ABD','AIPS','CAN','CASA','DAN',
        'I+D-E','I+D-F','I+D-G','I+D-L','I+D-M','I+D-N','I+D-P','I+D-Q','ITP','IPS']


path = 'C:/Users/nikil/Desktop/berat'  # path of all stored files(use back slash)

store_path = 'C:/Users/nikil/Desktop/berat' #path to store files(use back slash)




def copy_file(path,store_path,file,ext_dr):
    if os.path.exists(store_path+'/'+ext_dr):
        shutil.copy(path+'/'+file, store_path+'/'+ext_dr+'/'+file)
  
    # This will create a new directory,
    # if the directory does not already exist
    else:
        os.makedirs(path+'/'+ext_dr)
        shutil.copy(path+'/'+file, store_path+'/'+ext_dr+'/'+file)
    

for file in os.listdir(path):
    if file.endswith('.CATPart'): ##checking for CATPart file
    
        ext_dr = 'CATPart'
        copy_file(path,store_path,file,ext_dr)
    else:
        sub  = [ele for ele in keys if(ele in file)] ## checking if file conatins a key
        if bool(sub):
            ext_dr  = sub[0]
            copy_file(path,store_path,file,ext_dr)
        
