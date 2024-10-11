import os 
import shutil
#print("os and shutil modules are available.")

def organise(directory):
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return  
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory,filename)

        if os.path.isdir(file_path):
           continue
        extension = os.path.splitext(filename)
        extension = extension[1:].lower()

        if not extension:
           continue
        extension_dir = os.path.join(directory,extension)
        if not os.path.exists(extension_dir):
          os.makedirs(extension_dir)


        shutil.move(file_path,os.path.join(extension_dir,filename))   
        print(f"Moved:{filename} -> {extension}/{filename}")     

directory = input("Enter the path to the directory to organise: ")       
organise(directory)