#-------------------------------------------------------------------------------
# Name:        List All Files in Folder and Its Subfolders with Paths
# Purpose:      Point to a folder containing files and/or subfolders you would like listed in a .csv. The output 
#               provides each file name and extension and the path to that file. Useful for file inventories and directories.
#
# Author:      keforwar
#
# Created:     10/12/2020 for Python 3
# Copyright:   (c) keforwar 2020
#-------------------------------------------------------------------------------

import pandas as pd
import os

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create the Tkinter app
root = tk.Tk()
root.withdraw()

# Show the first info box
messagebox.showinfo(
            "File name and path list generation tool",
            "Welcome, please provide a folder containing the files you'd like to list."
        )

dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory where the folders are created')

if not dirname:
    quit()


# Error handling variables
file_error_list = []
error_occurred = False



output_file = os.path.join(dirname,'FileNamesAndPaths.csv')

df = pd.DataFrame(columns=['File','Folder Location'])

for root, dir, files in os.walk(dirname):
    files = [f for f in files if not f.startswith('~') and f!='Thumbs.db']
    paths = [os.path.join(root, f) for f in files]
    folders = [p.rsplit('\\',1)[0] for p in paths]
    df1 = pd.DataFrame({'File': files,
                        'Folder Location': folders})
    df = df.append(df1)

df.to_csv(output_file, index= False)

# Show the last info box
messagebox.showinfo(
            "Output file is now complete.",
            "View 'FileNamesAndPaths.csv' in the root folder you entered.")
