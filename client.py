import cfg
import win32api
import make_filelist, process_commands

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

for drive in drives:
    if drive[0]=='A' : continue
    path = drive
    volume = cfg.host + '-' + drive[0]
    make_filelist.main(path,volume)

#process_commands.main()