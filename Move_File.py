import os
import shutil

from_dir = "C:/Users/HP/Downloads/school"
to_dir = "C:/Users/HP/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

path = "Downloads/school/class.png"
root,extension = os.path.splitext(path)
print("THe root of the path:" , root)
print("THe extension of the path:" , extension)

path1 = "Downloads/school/coloring.jpg"
root,extension = os.path.splitext(path1)
print("THe root of the path:" , root)
print("THe extension of the path:" , extension)

path2 = "Downloads/school/RULES.png"
root,extension = os.path.splitext(path2)
print("THe root of the path:" , root)
print("THe extension of the path:" , extension)
#for list_of_files in range(from_dir):

   # root,extension = os.path.splitext(list_of_files)
   # print("Root of the tha path: ", root)
 #    shutil.move(from_dir,to_dir)

#print(to_dir)
