##libraries to be imported
import pandas as pd
import shutil
import itertools
import os
import time
import csv

start_time = time.time()
print("start")



# this function converts the excel file at the specified path into a dictionary
def excel_to_dict(path):

    dataframe = pd.read_excel(path)  ##reads files to fetch
    columnNames = list(dataframe.columns)
    # print('columns',columnNames)

    if len(columnNames) == 1:
        temp = []
        dct = dataframe[columnNames[0]].tolist()
        data_type = 0
    else:
       
        temp = [i.split(",") for i in dataframe[columnNames[1]].tolist()]

        data_type = 1
        dct = dict(zip(dataframe[columnNames[0]], temp))

    return dct, data_type


# this function takes in a dictionary with required files and a path and outputs a list of all required file paths
def get_path(reqFiles, path, data_type):

    dataframe2 = pd.read_excel(path)
    frame = []
    not_found = []
    if data_type == 1:

        for key, value in itertools.chain.from_iterable(
            [itertools.product((k,), v) for k, v in reqFiles.items()]
        ):
            temp = dataframe2[dataframe2.FileName.str.contains(key)]
            temp2 = temp[temp.FileName.str.contains(value)]
            if temp2["File Path"].to_list():
                frame += temp2["File Path"].to_list()
            else:
                not_found.append((key, value))
    else:
        for values in reqFiles:
            temp = dataframe2[dataframe2.FileName.str.contains(values)]
            if temp["File Path"].to_list():
                frame += temp["File Path"].to_list()
            else:
                not_found.append(values)

    return frame, not_found


# this functions copies the files into the given path
def copy_file(store_path, lst):

    for i in lst:

        temp = i.split("\\")

        try:

            shutil.copy(os.path.abspath(i), store_path + "/" + temp[-1])
            # print("File copied successfully.")

        # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")

        # For other errors
        except:
            print("Error occurred while copying file.")
            
def not_found_excel(not_found,data_type,path):
    if data_type == 1:     
        header = ['FileName', 'FileType']
        with open(path, 'w',encoding='UTF8', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(header)
            for key, value in not_found:
                writer.writerow([key, value])
            
    else:
        header = ['FileName']
        with open(path, 'w',encoding='UTF8', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(header)
            for value in not_found:
                writer.writerow([value])


# path containing the excel sheet with requirements(USE BACK SLASH!!!)
excel_path1 = "D:/requiredfilelist.xlsx"

# path containing the excel sheet with required files(USE BACK SLASH!!!)
excel_path2 = "D:/masterfilerecd.xlsx"

# path for the destination of the copied files
destination = "D:/requiredfiles"

#path for excel files of not found
CSV_path = 'C:/Users/nikil/Desktop/output.csv'

# getting file the data from excel sheet to dictionary
reqFiles, data_type = excel_to_dict(excel_path1)

# getting required path names into a list
lst, Not_found = get_path(reqFiles, excel_path2, data_type)

if Not_found:
    print("files not found are:", Not_found)
else:
    print("All files are found")
    
#creates excel file with all files not found    
not_found_excel(Not_found, data_type, CSV_path)    
    
# copying files to destination folder
copy_file(destination, lst)



print("done")
 
end_time = time.time()
 
print("excecution time", end_time - start_time)

