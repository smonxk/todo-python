import FreeSimpleGUI as gui
import zip_creator as zip

label_import = gui.Text("Select files")
input_import = gui.Input(key="import")
choose_files_btn = gui.FilesBrowse("Choose", key="files")

label_export = gui.Text("Select destination folder")
input_export = gui.Input(key="export")
choose_dir_btn = gui.FolderBrowse("Choose", key="directory")

compress_btn = gui.Button("Compress")
output_label = gui.Text(key="output")

window = gui.Window("File compressor", layout=[[label_import], 
                                                [input_import, choose_files_btn],
                                                [label_export], [input_export, choose_dir_btn],
                                                [compress_btn, output_label]])

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["directory"]
    window["output"].update(value="Completed!")
    window["export"].update(value="")
    window["import"].update(value="")
    zip.create_archive(filepaths, folder)
window.close()