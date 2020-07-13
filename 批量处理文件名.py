import os

DIR_PATH = "C:\\Users\\Administrator\\Desktop\\test"
files = os.listdir(DIR_PATH)
i = 0
for filename in files:
    name, suffix = os.path.splitext(filename)
    new_name = os.path.join(DIR_PATH, str(i) + suffix)
    old_name = os.path.join(DIR_PATH, filename)
    os.rename(old_name, new_name)
    i = i + 1
