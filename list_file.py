#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
import os
import csv
from tkinter import messagebox as msg

try:
    from tkinter import *
    import ttk
except:
    import tkinter as tk #GUI package
    from tkinter import ttk


def fx_BasicListing():
    #argx mode = 1 pour basic listing
    #argx mode = 2 pour adv listing
    # "txt" pour type enreg csv txt/csv
    # tree.delete(*tree.get_children())
    fx_browseFoldersZ(1)
    return

def fx_AdvancedListing():
    #argx mode = 1 pour basic listing
    #argx mode = 2 pour adv listing
    # fx_browseFoldersZ(2,"txt")
    # tree.destroy()
    #tree.delete(*tree.get_children())
    fx_browseFoldersZ(2)
    return

def fx_browseFoldersZ(argy):
    #argx mode = 1 pour basic listing
    #argx mode = 2 pour adv listing
    # "txt" pour type enreg csv txt/csv
    tree.delete(*tree.get_children())
    fx_browseFolders(argy,"txt")

###############################################################################
###############################################################################
###############################################################################

def fx_writeCSV(*arr):

    csv_file_title = 'csv_1_baselisting.csv'
    # csv path entry box
    CSV_FILE = vcsv_path.get()

    if not os.path.exists(CSV_FILE):
        os.makedirs(CSV_FILE)

    CSV_FILE += csv_file_title
    print('%s' % CSV_FILE)

    with open(CSV_FILE,'w', newline ='\n') as f:
        write = csv.writer(f, doublequote=True, delimiter=';')
        for row in arr:
            write.writerows(row)

def fx_writeCSV_str(txt_str):
    csv_file_title = 'csvtxt_1_baselisting.csv'
    # csv path entry box
    CSV_FILE = vcsv_path.get()

    if not os.path.exists(CSV_FILE):
        os.makedirs(CSV_FILE)

    CSV_FILE += csv_file_title
    print('%s' % CSV_FILE)

    with open(CSV_FILE,'w') as f:
        f.write(txt_str)

    # fx_LoadCSV(CSV_FILE)

    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            col1 = row['Path']
            col2 = row['Folder-file']
            col3 = row['Size in Byte']
            col4 = row['Size in Kb']
            col5 = row['Size in Mb']
            col6 = row['Size in Gb']
            col7 = row['type']

            tree.insert('', 'end', values=(col1, col2, col3, col4, col5, col6,col7))

    return

###############################################################################
###############################################################################

def fx_chkPath(xzPath):
    isxFile = os.path.isfile(xzPath)
    isxDir = os.path.isdir(xzPath)
    print("DOSSIER OUI????",isxDir)
    if isxDir:
        return
    elif not isxDir:
        msg.showwarning("Folder path", "WD Path entered not found")
    return


###############################################################################
###############################################################################
###############################################################################


def fx_browseFolders(argz, tycsv):
    tree.delete(*tree.get_children())
    # /// /// ///
    csv_txt = ""
    csv_contents = ""
    counterPath = 0
    size = 0
    f_size = 0
    f_vscale = 0
    # /// /// ///

    # path WD
    Lpath = vtxt_path.get()
    print('%s' % Lpath)

    # include files
    vvchkboxF = vchkboxF.get()
    # print("include files:::", vchkboxF.get())

    # include modification date
    print(vchkboxD.get())

    # include creation date
    print(vchkboxC.get())

    # scale
    f_vscale = int(var_scale.get())
    print(f_vscale)

    # path WD 2
    if Lpath.endswith(os.path.sep):
       Lpath = Lpath[:-1]

    # isFile = os.path.isfile(Lpath)
    # print("fichier?",isFile)
    fx_chkPath(Lpath)

    counterPath = Lpath.count(os.path.sep)

    csv_contents = "Path;Folder-file;Size in Byte;Size in Kb;Size in Mb;Size in Gb;type\n"

    csv_txt = csv_contents

    # csv_contents
    #     1-FOLDER PATH
    #     2-FILENAME
    #     3-FOLDER PATH FULL
    #     4-Size in Byte
    #     5-Size in Kb
    #     6-Size in Mb
    #     7-Size in Gb
    #     8-type\n

    ### BASIC LISTING #########
    if argz == 1:
        print("basic listing")
        file_paths = []
        file_paths.append([csv_contents])
        for root, dirs, files in os.walk(Lpath, topdown=True):
            for file in files:
                if tycsv == "csv":
                    vfolder_path = root + os.sep
                    vfile_name = "'" + file + "'"
                    vfolder_path_full = root + os.sep + file
                    csv_contents = "%s;%s;%s;%s;%s;%s;%s" % (vfolder_path, vfile_name , 'na', 'na', 'na','na', "folder")
                    file_paths.append([csv_contents])
                elif tycsv == "txt":
                    vfolder_path = root + os.sep
                    vfile_name = file
                    vfolder_path_full = root + os.sep + file
                    f_size = os.path.getsize(vfolder_path_full)
                    csv_txt += "%s;%s;%.0f;%.2f;%.2f;%.2f;%s" % (vfolder_path, vfile_name, f_size, f_size/1024, f_size/1048576,f_size/1073741824, "file\n")

        # APPEL FONCTION ECRIT ARRAY TO CSV
        if tycsv == "csv":
            fx_writeCSV(file_paths)
        elif tycsv == "txt":
        # APPEL FONCTION ECRIT STR TO CSV
            fx_writeCSV_str(csv_txt)

        print("job basic listing ok")

    ### ADVANCED LISTING ########
    elif argz == 2:
        print("advanced listing")

        if vvchkboxF == 0:
        #                      *** FOLDERS ONLY ***
            for root, dirs, files in os.walk(Lpath, topdown=False):
            ### calcul taille dossier
                f_size = 0
                for x, y, z in os.walk(root):
                    for i in z:
                        ftmp_che = x + os.sep + i
                        f_size += os.path.getsize(ftmp_che)
                ### ecriture taille dossier
                counter = root.count(os.path.sep) - counterPath
                vfile_name = root
                vfile_name = vfile_name + os.path.sep
                vfile_name = os.path.split(os.path.dirname(vfile_name))[1]
                vfile_name += os.path.sep
                if counter <= f_vscale:
                    csv_txt += "%s;%s;%.0f;%.2f;%.2f;%.2f;%s" % (root, vfile_name, f_size, f_size/1024, f_size/1048576,f_size/1073741824, "folder\n")

            fx_writeCSV_str(csv_txt)
            print("job adv listing folders ok")

        elif vvchkboxF == 1:
        #                    *** FOLDERS AND FILES ONLY ***
            for root, dirs, files in os.walk(Lpath, topdown=False):
            ### calcul taille dossier
                size = 0
                for x, y, z in os.walk(root):
                    for i in z:
                        ftmp_che = x + os.sep + i
                        f_size += os.path.getsize(ftmp_che)
                ### ecriture taille dossier
                counter = root.count(os.path.sep) - counterPath
                vfile_name = root
                vfile_name = vfile_name + os.path.sep
                vfile_name = os.path.split(os.path.dirname(vfile_name))[1]
                vfile_name += os.path.sep
                if counter <= f_vscale:
                    csv_contents += "%s;%s;%.0f;%.2f;%.2f;%.2f;%s\n" % (root, vfile_name, f_size, f_size/1024, f_size/1048576,f_size/1073741824, "folder")

            ### calcul +ecriture taille fichier
            for f in os.listdir(Lpath):
                path = os.path.join(Lpath, f)
                if os.path.isfile(path):
                    f_size = 0
                    f_size = os.path.getsize(path)
                    csv_contents += "%s;%s;%.0f;%.2f;%.2f;%.2f;%s\n" % (path, f, f_size, f_size/1024, f_size/1048576,f_size/1073741824, "file")

            fx_writeCSV_str(csv_contents)
            print("job adv listing files ok")
    return



###############################################################################
###############################################################################
###############################################################################
#####################################GUI#######################################
###############################################################################
###############################################################################
###############################################################################

locale.setlocale(locale.LC_ALL, "")

## MAIN WINDOW
root = Tk()
width  = int(root.winfo_screenwidth()/1.3)
height = int(root.winfo_screenheight()/1.29)
positionRight = int(width/7)
positionDown = int(height/8)

root.geometry('%sx%s+%s+%s' % (width, height, positionRight, positionDown))
root.title("Folders and files tool")

### MAKE TABS
tabCtrl = ttk.Notebook(root)
tab1 = ttk.Frame(tabCtrl)
tab2 = ttk.Frame(tabCtrl)
tab3 = ttk.Frame(tabCtrl)
tab4 = ttk.Frame(tabCtrl)
tabCtrl.add(tab1, text ='    Folders mgmt   ')
tabCtrl.add(tab2, text ='    Renamer   ')
tabCtrl.add(tab3, text ='    Something3   ')
tabCtrl.add(tab4, text ='    More infos   ')
tabCtrl.pack(expand = 1, fill ="both")

### Display Tabs
global vtxt_path
global var_scale
global vchkboxF
global vchkboxD
global vchkboxC
global vcsv_path


#######################///...///...///...///...///#######################
#                               TAB 1                                   #
#######################///...///...///...///...///#######################

### FRAME GLOB
frm10 = tk.Frame(tab1, bg="gray5")
frm10.pack(expand = 1, fill ="both")
# frm10.pack( side = LEFT, expand = True, fill = BOTH)

#######################
### FRAME 11 TOP LABEL
frm11 = tk.Frame(frm10, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1)

frm11.place(width=475, height=140, x=20, y=20)

# Top label title
tk.Label(frm11,text ="Drive or folders", font=("Tahoma", 14, "normal"), fg='gray80', bg='gray5').place(x=20, y=10)

### LABEL PATH entry box
tk.Label(frm11, text="Enter Path (WD)", fg='gray80', bg='gray5').place(x=20, y=55)

# TEST FOLDER
new_text = "/media/ananas/HDD_500B/TEST_APP3/"

### PATH ENTRY BOX
vtxt_path=tk.StringVar(root,value=new_text) # Value saved here
txt_path = tk.Entry(frm11,width=43, textvariable=vtxt_path, fg='green').place(width=320, height=30, x=140, y=50)


# vtxt_path.set(new_text)
# TEST FOLDER zzz

### LABEL PATH example
tk.Label(frm11, text=r"Ex.: path for Windows: C:\Users\user\Documents\Dossier test", font=("Helvetica", 8, "italic"), fg='gray80', bg='gray5').place(width=320, height=30, x=130, y=80)

tk.Label(frm11, text=r"     path Linux: /home/user/Documents/Test dossier/", font=("Verdana", 8, "italic"), fg='gray80', bg='gray5').place(width=300, height=30, x=123, y=100)

### frame 11
###########################

###########################
### FRAME 12 TOP BUTTON SCAN ALL
frm12 = tk.Frame(frm10, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1)
frm12.place(width=150, height=40, x=494, y=20)

### button
btn_scanALL = tk.Button(frm12, text="Basic listing",  bg='lightblue4', font=("Verdana", 10,"normal"))

btn_scanALL.pack(expand = 1, fill ="both",padx=0, pady=0)

### BUTTON BROWSE entry fx BASIC LISTING
btn_scanALL['command'] = fx_BasicListing

### frame 12
###########################

###########################
### FRAME 13 TOP BTN SCAN ADV + SLIDER
frm13 = tk.Frame(frm10, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1, bd= 0)
frm13.place(width=540, height=100, x=494, y=60)

btn_scanADV = tk.Button(frm13, text="Advanced listing", bg='ivory4', font=("Verdana", 10,"normal"))
btn_scanADV.place(width=150, height=40, x=0, y=0)

### BUTTON BROWSE entry fx ADVANCED LISTING
btn_scanADV['command'] = fx_AdvancedListing

### slider
var_scale = tk.DoubleVar()
tk.Label(frm13, text="Subfolders level", font=("Verdana", 8, "italic"), fg='gray80', bg='gray5').place(width=150, height=10, x=0, y=46)

wslide = tk.Scale(frm13,bg='ivory4', fg='grey5', from_=0, to=10, variable = var_scale, orient=tk.HORIZONTAL)
wslide.place(width=150, height=40, x=0, y=58)
wslide.set(3)
### frame 13
###########################

###########################
### FRAME 14 TOP BTN SCAN ADV + CHECKBUTTONS
frm14 = tk.Frame(frm10, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1, bd= 0)
frm14.place(width=190, height=100, x=645, y=60)

vchkboxF=tk.IntVar()
chkbox=tk.Checkbutton(frm14, highlightthickness=0,bd=0,text="Include files", font=("Verdana", 9, "normal"), fg='gray80', bg='gray5', variable=vchkboxF, offvalue=0, onvalue=1)
chkbox.place(x=0, y=5)

vchkboxD=tk.IntVar()
chkbox=tk.Checkbutton(frm14, highlightthickness=0,bd=0,text="Include modification date", font=("Verdana", 9, "normal"), fg='gray80', bg='gray5', variable=vchkboxD, offvalue=0, onvalue=1)
chkbox.place(x=0, y=25)

vchkboxC=tk.IntVar()
chkbox=tk.Checkbutton(frm14, highlightthickness=0,bd=0,text="Include creation date", font=("Verdana", 9, "normal"), fg='gray80', bg='gray5', variable=vchkboxC, offvalue=0, onvalue=1)
chkbox.place(x=0, y=45)
### frame 14
###########################

###########################
### FRAME 15 TREEVIEW
frm15 = tk.Frame(frm10, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1, bd= 0)
frm15.place(width=1000, height=350, x=20, y=175)

container = ttk.Frame(frm15)
# container.place(width=1015, height=350, x=20, y=175)
container.pack()

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="lemonchiffon3",font=('Tahoma', 9),
                fieldbackground="lemonchiffon3", foreground="grey10")

style.configure("Treeview.Heading", font=('Tahoma', 10),foreground='orange4')

tree = ttk.Treeview(frm15, columns=('1', '2', '3', '4', '5', '6', '7'))
vsb = ttk.Scrollbar(orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(orient="horizontal", command=tree.xview)
vsb.place(x=1021, y=231,width=15, height=307,)
hsb.place(x=22, y=540,width=1000, height=15,)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
container.grid_columnconfigure(0, weight=1)
container.grid_rowconfigure(0, weight=1)

tree.column('#1', width=180, stretch=YES)
tree.column('#2', width=240, stretch=YES)
tree.column('#3', width=10, stretch=YES)
tree.column('#4', width=5, stretch=YES)
tree.column('#5', width=5, stretch=YES)
tree.column('#6', width=5, stretch=YES)
tree.column('#7', width=25, stretch=YES)

tree.heading('#1', text='Path')
tree.heading('#2', text='Folder-file')
tree.heading('#3', text='Byte')
tree.heading('#4', text='Kb')
tree.heading('#5', text='Mb')
tree.heading('#6', text='Gb')
tree.heading('#7', text='Object type')

tree['show'] = 'headings'

tree.pack(fill=BOTH,expand=1)

### frame 15
###########################

###########################
### FRAME 16 CSV DIAL
frm16 = tk.Frame(frm10, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1, bd= 0)
frm16.place(width=480, height=30, x=20, y=530)

# csv lbl
tk.Label(frm16,text ="Default folder for csv file (change...)", font=("Verdana", 8, "normal"), fg='gray80', bg='gray5').place(x=10, y=5)

# csv folder entry box
vcsv_path=tk.StringVar() # Value saved here
txt_csv = tk.Entry(frm16,width=43, textvariable=vcsv_path, fg='green').place(width=265, x=210, y=3)
full_path = os.path.realpath(__file__)
new_text = os.path.dirname(full_path) + os.sep + 'csv_folder' + os.sep
vcsv_path.set(new_text)

###############################################################################
###############################################################################
###############################################################################

###############################################################################
###############################################################################
###############################################################################

def fx_FileRen():

    Lpath = vtxt_path3.get()
    print('%s' % Lpath)

    # path WD 2
    if Lpath.endswith(os.path.sep):
       Lpath = Lpath[:-1]

    print('%s' % Lpath)

    msg.showwarning("File names", "File names changed")

    # with open(csv_file_title) as csvfile:
    #     csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    #     for row in csvreader:
    #         name = row[0]
    #         new = row[1]
    #         if os.path.exists(name):
    #             os.rename(name, new)
    #         else:
    #             print(name + " does not exist")


###############################################################################

def fx_FoldRen():

    csv_file_title = 'csv_1_baselisting.csv'
    print('%s' % csv_file_title)

    # with open(CSV_FILE,'w', newline ='\n') as f:
    #     write = csv.writer(f, doublequote=True, delimiter=';')
    #     for row in arr:
    #         write.writerows(row)


    msg.showwarning("Folder names", "Folders names changed")

###############################################################################
###############################################################################
###############################################################################

###############################################################################
###############################################################################
###############################################################################


#######################///...///...///...///...///#######################
#                               TAB 2                                   #
#######################///...///...///...///...///#######################

### FRAME GLOB
frm20 = tk.Frame(tab2, bg="gray5")
frm20.pack(expand = 1, fill ="both")
# frm10.pack( side = LEFT, expand = True, fill = BOTH)

#######################
### FRAME 21a FOLDER PATH
frm21a = tk.Frame(frm20, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1)

frm21a.place(width=950, height=100, x=20, y=45)

# Top label title
tk.Label(frm21a,text ="Folder path to list folders files to csv", font=("Tahoma", 14, "normal"), fg='gray80', bg='gray5').place(x=20, y=10)

vtxt_path1a=tk.StringVar(root, value=new_text) # Value saved here
txt_path1a = tk.Entry(frm21a,width=43, textvariable=vtxt_path1a, fg='blue').place(width=620, height=30, x=140, y=50)

#######################
### FRAME 21 LABEL FILES RENAME
frm21 = tk.Frame(frm20, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1)

frm21.place(width=775, height=100, x=20, y=185)

# Top label title
tk.Label(frm21,text ="Rename files only from csv file below", font=("Tahoma", 14, "normal"), fg='gray80', bg='gray5').place(x=20, y=10)

### LABEL FILES RENAME entry box
tk.Label(frm21, text="CSV file path", fg='gray80', bg='gray5').place(x=20, y=55)

# TEST FOLDER
full_path = os.path.realpath(__file__)
new_text = os.path.dirname(full_path) + os.sep + 'csv_folder' + os.sep + "csvtxt_1_filenamelisting.csv"
# vtxt_path2.set(new_text)

### PATH ENTRY BOX
vtxt_path2=tk.StringVar(root, value=new_text) # Value saved here
txt_path2 = tk.Entry(frm21,width=43, textvariable=vtxt_path2, fg='blue').place(width=620, height=30, x=140, y=50)

# TEST FOLDER zzz

###########################
### FRAME 22 TOP BUTTON FILE RENAME
frm22 = tk.Frame(frm20, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1)
frm22.place(width=150, height=40, x=820, y=220)

### button
btn_FileRen = tk.Button(frm22, text="Files rename",  bg='lightblue4', font=("Verdana", 10,"normal"))

btn_FileRen.pack(expand = 1, fill ="both",padx=0, pady=0)

### BUTTON BROWSE entry fx BASIC LISTING
btn_FileRen['command'] = fx_FileRen


#######################
### FRAME 23 LABEL FOLDERS RENAME
frm23 = tk.Frame(frm20, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1)

frm23.place(width=775, height=100, x=20, y=320)

# Top label title
tk.Label(frm23,text ="Rename folders only from csv file below", font=("Tahoma", 14, "normal"), fg='gray80', bg='gray5').place(x=20, y=10)

### LABEL PATH entry box
tk.Label(frm23, text="CSV file path", fg='gray80', bg='gray5').place(x=20, y=55)

# TEST FOLDER
full_path = os.path.realpath(__file__)
new_text = os.path.dirname(full_path) + os.sep + 'csv_folder' + os.sep + "csvtxt_1_foldernamelisting.csv"
# vtxt_path2.set(new_text)

### PATH ENTRY BOX
vtxt_path3=tk.StringVar(root, value=new_text) # Value saved here
txt_path3 = tk.Entry(frm23,width=43, textvariable=vtxt_path3, fg='brown').place(width=620, height=30, x=140, y=50)

# TEST FOLDER zzz

###########################
### FRAME 24 BUTTON FOLDERS RENAME
frm24 = tk.Frame(frm20, bg="gray5",highlightbackground="HoneyDew3", highlightcolor="HoneyDew3", highlightthickness=1)
frm24.place(width=150, height=40, x=820, y=345)

### button
btn_FoldRen = tk.Button(frm24, text="Folders rename",  bg='brown', font=("Verdana", 10,"normal"))

btn_FoldRen.pack(expand = 1, fill ="both",padx=0, pady=0)

### BUTTON BROWSE entry fx BASIC LISTING
btn_FoldRen['command'] = fx_FoldRen


#######################///...///...///...///...///#######################
#                               TAB 3                                   #
#######################///...///...///...///...///#######################




#######################///...///...///...///...///#######################
#                               zZZZz                                   #
#######################///...///...///...///...///#######################

if __name__ == '__main__':
    root.mainloop()