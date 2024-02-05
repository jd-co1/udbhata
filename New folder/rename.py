import os,glob

list_of_files = glob.glob(os.path.join("C:\\Users\\sheik jaheer\\Downloads\\", '*'))
latest_file = max(list_of_files, key=os.path.getctime)
latest_file_path = os.path.join("C:\\Users\\sheik jaheer\\Downloads\\", latest_file)
new_file_path = os.path.join("C:\\Users\\sheik jaheer\\Downloads\\", 'options.csv')

# Rename the file
os.rename(latest_file_path, new_file_path)