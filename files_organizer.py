"""
A Script to organize files in "Downloads" into directories by their type.
"""

import os
import shutil
import filecmp

if os.name == "nt":
    delim = "\\"
else:
    delim = "/"

fileTypes = { 
            "Audio": [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"],
            "Code": [".py", ".ipynb", ".c", ".h", ".cpp", ".js", ".java", ".class", ".cs", ".sh", ".php", ".html", ".xhtml", ".css", ".asp", ".cgi", ".pl", ".swift", ".vb", ".dart", ".jl", ".m", ".mat", ".lisp", ".lsp", ".l", ".cl", ".fasl"],
            "Compressed": [".7z", ".arj", ".deb", ".gz", ".pkg", ".rar", ".rpm", ".tar", ".z", ".zip"],
            "Data": [".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml"],
            "Discs": [".dmg", ".iso", ".toast", ".vsc"],
            "Documents": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".tex", ".odt", ".txt", ".pages", ".md", ".key", ".wpd"],
            "Executable": [".apk", ".bat", ".bin", ".com", ".exe", ".gadget", ".jar", ".msi", ".wsf"],
            "Fonts": [".fnt", ".fon", ".otf", ".ttf"],
            "Images": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff"],
            "Presentations": [".ppt", ".pptx", ".odp", ".pps", ".key"],
            "Spreadsheets": ["xls", ".xlsm", ".xlsx", ".ods", ".numbers"],
            "System": [".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ini", ".lnk", ".sys", ".tmp"],
            "Videos": [".3g2", ".3gp", ".avi", ".flv", "h264", "m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv"],
            "Other": []
}

def get_download_path():
    if os.name == "nt":
        import winreg

        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]

        return location
    else:
        return os.path.join(os.path.expanduser("~"), "Downloads")


def create_folders(path: str):
    for k in fileTypes.keys():
        dir = path + delim
        dir += k
        if not os.path.exists(dir):
            os.mkdir(dir)


def main():    
    download = get_download_path()
    create_folders(download)

    for file in os.listdir(download):
        f = os.path.join(download, file)
        if os.path.isfile(f) and file[0] != ".":
            found = False
            f_ext = os.path.splitext(f)[1]
            for k, v in fileTypes.items():
                if f_ext in v:
                    dest = download + delim + k
                    if not os.path.exists(dest + delim + f.rsplit(delim)[-1]):
                        found = True
                        shutil.move(f, dest)
                        break
                    elif filecmp.cmp(f, dest):
                        os.remove(f)
            if not found:
                shutil.move(f, download + "/Other")


if __name__ == "__main__":
    main()
