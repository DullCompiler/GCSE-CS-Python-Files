#file manegment python test

#create path variable
path = '/mnt/chromeos/removable/Media/Coding/testfile.txt'

#select the file
file = open(path, 'r')

#reading the file
#file.readline() - just one line
#file.readlines() - all lines
#file.read() - all lines

#creating a new file
title='testfile_cbp/n'

#looking at old path
path = '/mnt/chromeos/removable/Media/Coding/testfile.txt'
file_path = open(path, 'r')
file = file_path.read()

#creating new path
new_path = '/mnt/chromeos/removable/Media/Coding/testfile_cbp.txt'
newfile_cbp= open(new_path, 'w')

#writes and prints title
newfile_cbp.write(title)
print(title)

#writes and prints text
newfile_cbp.write(file)
print(file)

#closes files
##file.close()## - doesn't work
newfile_cbp.close()
