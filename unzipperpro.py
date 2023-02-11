#Author:Siddharth deo
import zipfile
import tarfile
def unzip(filename):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall()
def untar(filename):
    with tarfile.open(filename, 'r') as tar_ref:
        tar_ref.extractall()

print('Select an option:')
print('1. Unzip a file')
print('2. Untar a file')
option = input('Enter an option number: ')

if option == '1':
    filename = input('Enter the filename to unzip: ')
    unzip(filename)
    print('File unzipped successfully.')
elif option == '2':
    filename = input('Enter the filename to untar: ')
    untar(filename)
    print('File untarred successfully.')
else:
    print('Invalid option selected.')
