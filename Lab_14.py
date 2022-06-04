import os

# Initialize current user's directories
pic_path = "%homepath%\\pictures\\"
snd_path = "%homepath%\\music\\"

# Give instructions
print("This program will open an image file and a sound file from the current user's \'Music\' and \'Pictures\' folders.")

# Get the file names with file extensions
p_file = input("Please enter the name of the image file, including file extension: ")
s_file = input("Please enter the name of the sound file, including file extension: ")

# Join path and file name/extension. Explicitly add quotes and open the file.
cmd = ("\"" + pic_path + p_file + "\"")
os.system("\"" + cmd + "\"")

# Join path and file name/extension. Explicitly add quotes and open the file.
cmd = ("\"" + snd_path + s_file + "\"")
os.system("\"" + cmd + "\"")

