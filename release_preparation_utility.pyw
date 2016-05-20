__author__ = "Joel Webster"

import os
import shutil
import subprocess
import ctypes

from datetime import datetime, timedelta
from Tkinter import *

######Global Variables ########
release_folder = "Releases"
docs_folder = "Docs"
roll_back_folder = "Rollback"
################################

# GUI
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        # create path label
        self.label = Label(
            frame, text="Enter release folder path: "
        )
        self.label.grid(row=0, column=0, columnspan=4, pady=2)
        # create text entry widget
        self.entry = Entry(
            frame, width=40
        )
        self.entry.focus
        self.entry.grid(row=1, column=0, columnspan=4, pady=2)
        # create generate button
        self.genbutton = Button(
            frame, text="Generate Structure", fg="black", height=1, width=34, command=self.generate_structure
        )
        self.genbutton.grid(row=2, column=0, columnspan=4)
        # create prepare button
        self.prepbutton = Button(
            frame, text="Prepare Timestamps", fg="black", height=1, width=34, command=self.prepare_timestamps
        )
        self.prepbutton.grid(row=3, column=0, columnspan=4)
        #create gitRename
        self.prepbutton = Button(
            frame, text="Git Timestamps Rename", fg="darkgreen", height=1, width=34, command=self.git_rename
        )
        self.prepbutton.grid(row=4, column=0, columnspan=4)

        self.rollback_button = Button(
            frame, text="Git Rollback", fg="darkgreen", height=1, width=34, command=self.git_rollback
        )
        self.rollback_button.grid(row=5, column=0, columnspan=4)

        # create add Vs button
        self.addbutton = Button(
            frame, text="Add Vs", fg="black", height=1, width=34, command=self.add_v
        )
        self.addbutton.grid(row=6, column=0, columnspan=4)
        # create rem Vs button
        self.rembutton = Button(
            frame, text="Remove Vs", fg="black", height=1, width=34, command=self.remove_v
        )
        self.rembutton.grid(row=7, column=0, columnspan=4)

        # record directory util run from
        global git_dir
        git_dir = os.getcwd()

    ############## Common functions ############################################

    def m_box(self, title, text, style):
        ctypes.windll.user32.MessageBoxA(0, text, title, style)

    def set_directory(self):
        rpath = self.entry.get()
        if not rpath:
            self.m_box('Error', 'Please enter a release directory', 1)
            result = False
        else:
            os.chdir(rpath)
            result = rpath
        return result

    def get_current_timestamp(self):
        now = datetime.utcnow()
        timestamp = now
        return timestamp

    def increment_time_stamp(self, timestamp):
        # add minute increment to timestamp
        timestamp += timedelta(seconds=5)
        # create new timestamp string
        return timestamp

    def format_date_stamp(self, timestamp):
        return str('{:%Y%m%d%H%M%S}'.format(timestamp))


    def rename_artifact(self, rpath, fname):
        if re.search('\d+_+', fname) is not None:
            ext_prefix = re.search('\d+_+', fname).group(0)
        if re.search('[a-zA-Z]+.sql', fname) is not None:
            ext_postfix = re.search('[a-zA-Z]+.sql', fname).group(0)
        return ext_prefix + rpath[rpath.rfind('\\') + 1:] + "_" + ext_postfix
    #################################################################################

    def generate_structure(self):
        # os.chdir(self.set_directory())
        # create dirs
        rpath = self.set_directory()
        if rpath:
            os.makedirs(release_folder)
            os.makedirs(docs_folder)
            os.makedirs(roll_back_folder)

            # copy release file templates
            src_files = os.listdir(git_dir + "\\templates")

            for fname in src_files:
                if re.search('.*rollback', fname) is not None:
                    full_file_name = os.path.join(git_dir + "\\templates", fname)
                    shutil.copy(full_file_name, roll_back_folder)
                else:
                    full_file_name = os.path.join(git_dir + "\\templates", fname)
                    shutil.copy(full_file_name, release_folder)

            # rename templates to release name
            for fname in os.listdir(os.getcwd() + "\\" + roll_back_folder):
                    newfname =  self.rename_artifact(rpath, fname)
                    os.chdir(roll_back_folder)
                    os.rename(fname, newfname)
                    os.chdir("..")

            for fname in os.listdir(os.getcwd() + "\\" + release_folder):
                    newfname =  self.rename_artifact(rpath, fname)
                    os.chdir(release_folder)
                    os.rename(fname, newfname)
                    os.chdir("..")
            self.m_box('Success', 'Structures and templates have been created', 1)

    def add_v(self):
        # change to releases directory
        if self.set_directory():

            if os.path.exists(release_folder):
                #print "Release folder found"

                os.chdir(release_folder)
                for f in os.listdir(os.getcwd()):
                        # acquire file name
                        filename = f
                        p = re.compile('\d*_{2}.*')
                        # if match then rename
                        if p.match(filename) is not None:
                            newname = "V" + filename
                            os.rename(f, newname)
                os.chdir("..")

            else:
                #print "Release folder not found"
                self.m_box('Error', 'Releases folder not found', 1)
            self.m_box('Success', 'Vs have been added', 1)

    def remove_v(self):
        # change to releases directory
        if self.set_directory():
            #print("printing message to console [" + os.getcwd() + "]")

            if os.path.exists(release_folder):
                os.chdir(release_folder)
                for f in os.listdir(os.getcwd()):
                    # acquire file name
                    filename = f
                    # set regex
                    p = re.compile('V{1}\d+.*')
                    if p.match(filename) is not None:
                        # remove first character of filename
                        newname = f[1:]
                        # rename file
                        os.rename(f, newname)
                os.chdir("..")

            else:
                self.m_box('Error', 'Releases folder not found', 1)
            self.m_box('Success', 'Vs have been removed', 1)

    def prepare_timestamps(self):
        # change to Releases directory
        if self.set_directory():

            if os.path.exists(release_folder):
                #print "Release folder found"

                os.chdir(release_folder)
                listdir = os.listdir(os.getcwd())

                timestamp = self.get_current_timestamp()
                # file dir loop
                for f in listdir:
                    timestamp = self.increment_time_stamp(timestamp)
                    formatted_timestamp = self.format_date_stamp(timestamp)
                    if re.search('_{2}.*', f) is not None:
                        ext_fn = re.search('_{2}.*', f).group(0)
                        # rename file
                        if f[-4:] == ".sql":
                           # print f, ".sql extension detected"
                            os.rename(f, "V" + formatted_timestamp + ext_fn)
                        else:
                           # print f, ".sql extension not found, renaming file"
                            os.rename(f, "V" + formatted_timestamp + ext_fn + ".sql")
                    else:
                        prefix = re.search('\d+_', f).group(0)
                        prefix_len = len(prefix)
                        # rename file
                        if f[-4:] == ".sql":
                           # print f, ".sql extension detected"
                            os.rename(f, "V" + formatted_timestamp + "__" + f[prefix_len:])
                        else:
                           # print f, ".sql extension not found, renaming file"
                            os.rename(f, "V" + formatted_timestamp + "__" + f[prefix_len:] + ".sql")
                os.chdir("..")

            else:
                self.m_box('Error', 'Releases folder not found', 1)

            # change to rollback directory

            if os.path.exists(roll_back_folder):
                #print "Rollback folder found"

                os.chdir(roll_back_folder)
                listdir = os.listdir(os.getcwd())

                for f in listdir:
                    timestamp = self.increment_time_stamp(timestamp)
                    formatted_timestamp = self.format_date_stamp(timestamp)
                    if re.search('_{2}.*', f) is not None:
                        ext_fn = re.search('_{2}.*', f).group(0)
                        if f[-4:] == ".sql":
                           # print f, ".sql extension detected"
                            os.rename(f, formatted_timestamp + ext_fn)
                        else:
                           # print f, ".sql extension not found, renaming file"
                            os.rename(f, formatted_timestamp + ext_fn + ".sql")
                    else:
                        prefix = re.search('\d+_', f).group(0)
                        prefix_len = len(prefix)
                        # rename file
                        if f[-4:] == ".sql":
                           # print f, ".sql extension detected"
                            os.rename(f, formatted_timestamp + "__" + f[prefix_len:])
                        else:
                           # print f, ".sql extension not found, renaming file"
                            os.rename(f, formatted_timestamp + "__" + f[prefix_len:] + ".sql")
                os.chdir("..")

            else:
                self.m_box('Error', 'Rollback folder not found', 1)

            self.m_box('Success', 'Timestamps have been generated', 1)

    def git_rename(self):

        # change to Releases directory
        if self.set_directory():
            timestamp = self.get_current_timestamp()
            os.chdir(release_folder)
            listdir = os.listdir(os.getcwd())

            # file dir loop
            for f in listdir:
                # extract remaining filename
                timestamp = self.increment_time_stamp(timestamp)
                formatted_timestamp = self.format_date_stamp(timestamp)
                if re.search('_{2}.*', f) is not None:
                    ext_fn = re.search('_{2}.*', f).group(0)
                    # rename file
                    # -------------------------------------------------
                    newname = "V" + formatted_timestamp + ext_fn
                    subprocess.call(["git", "mv", f, newname])
                    # ------------------------------------------------
                else:
                    prefix = re.search('\d+_', f).group(0)
                    prefix_len = len(prefix)
                    # -------------------------------------------------
                    newname = "V" + formatted_timestamp + "__" + f[prefix_len:]
                    subprocess.call(["git", "mv", f, newname])
                    # ------------------------------------------------
            os.chdir("..")

            # change to rollback directory
            os.chdir(roll_back_folder)
            listdir = os.listdir(os.getcwd())

            for f in listdir:
                timestamp = self.increment_time_stamp(timestamp)
                formatted_timestamp = self.format_date_stamp(timestamp)
                if re.search('_{2}.*', f) is not None:
                    ext_fn = re.search('_{2}.*', f).group(0)
                    subprocess.call(["git", "mv", f, formatted_timestamp + ext_fn])
                else:
                    prefix = re.search('\d+_', f).group(0)
                    prefix_len = len(prefix)
                    filename = f
                    # rename file
                    subprocess.call(
                        ["git", "mv", f, formatted_timestamp + "__" + filename[prefix_len:]])
            os.chdir("..")
            self.m_box('Success', 'Files have been renamed', 1)

    def git_rollback(self):
        if self.set_directory():
            # change to rollback directory
            timestamp = self.get_current_timestamp()
            os.chdir(roll_back_folder)
            listdir = os.listdir(os.getcwd())
            timestamp = self.increment_time_stamp(timestamp)
            formatted_timestamp = self.format_date_stamp(timestamp)
            for f in listdir:
                if re.search('_{2}.*', f) is not None:
                    ext_fn = re.search('_{2}.*', f).group(0)
                    newname = "V" + formatted_timestamp + ext_fn
                    print "newname=" + newname
                    subprocess.call(["git", "mv", f, newname])
                else:
                    prefix = re.search('\d+_', f).group(0)
                    prefix_len = len(prefix)
                    filename = f
                    # rename file
                    newname = "V" + formatted_timestamp + "__" + filename[prefix_len:]
                    subprocess.call(["git", "mv", f, newname])
            os.chdir("../../../../..")
            print("printing message to console [" + os.getcwd() + "]")
            # subprocess.call(["git", "checkout", "HEAD^", "--", "objects"])

            self.m_box('Success', 'Rollback script is ready for deployment', 1)


# create tk frame
root = Tk()
# frame options
root.wm_title("")
root.resizable(width=FALSE, height=FALSE)
app = App(root)
root.mainloop()
