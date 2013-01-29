#relative path generator

#usage:set the home path and run the script from the current path


import os
home = 'c:\\work\\091_OFFER_G2_OnBoardCharger\\Project_Folder\\06_Sys_Design\\Sys_Com_Protocols\\00_CAN_Database\\'
cur_dir = os.path.realpath(__file__)

print os.path.relpath(home,cur_dir)