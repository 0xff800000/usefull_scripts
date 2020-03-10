import glob
import pathlib
import sys
import os

root_dir = "/home/d01000100/Videos/"
file_name = sys.argv[1][:-8]
max_depth = 50

print(root_dir)
print(file_name)

def find_torrent(root_dir, torrent_file, max_depth):
    # Sanitize file name
    torrent_file = torrent_file[:-8] # Remove extension
    torrent_file = torrent_file.replace("[","*")
    torrent_file = torrent_file.replace("]","*")
    for i in range(max_depth):
        path = root_dir + "*/" * i + torrent_file + "*"
        match = glob.glob(path)
        if len(match) == 1:
            return match[0]
    return ''

def get_file_list(root_dir, torrent_dir, max_depth):
    file_list = glob.glob(torrent_dir + "*.torrent")
    res = []
    for f in file_list:
        match = find_torrent(root_dir, f, max_depth)
        if match == '':
            print(10*'#' + "ERROR" + 10*'#')
            print(f)
            print(10*'#' + "#####" + 10*'#')
        else:
            res.append((f,match))
    return res

def add_qbittorrent(file_list):
    for files in file_list:
        torrent, path = files
        path = pathlib.Path(path).parent
        command = "qbittorrent \"{}\" --save-path=\"{}\"".format(torrent,path)
        print(command)
        os.system(command)


file_list = get_file_list(root_dir, '', max_depth)
print(file_list)
add_qbittorrent(file_list)
