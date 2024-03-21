from pyhdf.SD import SD

import matplotlib.pyplot as plt
import numpy as np

#loop through all .nc files in the folder
import os
import zipfile
import h5py

for file in os.listdir('./local_folder'):
    try:
        file_path = os.path.join('./local_folder', file)
        if file_path.endswith('.he5') and os.path.isfile(file_path):
            # Open the HE5 file in read mode
            with h5py.File(file_path, 'r') as h5_file:
                # List all datasets in the file
                print("Datasets in the HE5 file:")
                for dataset_name in h5_file.keys():
                    print(dataset_name)
                print("\n")
                
        if file_path.endswith('.hdf') and os.path.isfile(file_path):
            # Open the HDF file in read mode
            hdf_file = SD(file_path)

            datasets = hdf_file.datasets()
            print("Datasets in the HDF file:")
            for dataset_name in datasets.keys():
                print(dataset_name)
            print("\n")
            
            hdf_file.end()
            
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # zip_ref.extractall('./local_folder')
                # open the .tiff file in unzipped folder/measurment
                unzipped = file_path[:-4]+".SAFE"
                for file in os.listdir(unzipped+'/measurement'):
                    unzipped_file_path = os.path.join(unzipped+'/measurement', file)
                    if file.endswith('.tiff'):
                        # Open the .tiff file
                        img = plt.imread(unzipped_file_path)
                        plt.imshow(img)
                        plt.show()
                        
        
    except Exception as e:
        print("Error:", e)
        continue