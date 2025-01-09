import os, shutil

path=r"C:/Users/HP1/Documents/"

complete_files=os.listdir(path)

#  check for folders if exists are not.
print(os.path.exists(path+'txt files'))

folder_names=['csv files','text files','pdf files','excel files','image files','video files']

for folders in folder_names:
    if not  os.path.exists(path+folders):
       os.makedirs(path+folders)
       print('created')

for file in complete_files:

    if '.txt' in file and not os.path.exists(path+'text files/'+file):
        shutil.move(path+file,path+'text files/'+file)

    elif'.csv' in file and not os.path.exists(path+'csv files/'+file):
        shutil.move(path+file,path+'csv files/'+file)

    elif '.pdf' in file and not os.path.exists(path+'pdf files/'+file):
        shutil.move(path+file,path+'pdf files/'+file)

    elif '.xlsx' in file and not os.path.exists(path+'excel files/'+file):
        shutil.move(path+file,path+'excel files/'+file)

    elif '.jpg' in file and not os.path.exists(path+'image files/'+file):
        shutil.move(path+file,path+'image files/'+file)

    elif '.mp4' in file and not os.path.exists(path+'video files/'+file):
        shutil.move(path+file,path+'video files/'+file)

else:
    print('done execution!')
