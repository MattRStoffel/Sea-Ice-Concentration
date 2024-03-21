import earthaccess
import xarray as xr

earthaccess.login(persist=True)

satelites = []
short_names = 'AU_SI12', 'SENTINEL-1A_SLC', 'MYD29'

for short_name in short_names:
    satelites.append(earthaccess.search_data(
        short_name=short_name,
        cloud_hosted=True,
        bounding_box=(-10, 20, 10, 50),
        temporal=("2014-04-03", "2024-03-12"),
        count=1
    ))
    
    
# Download the data
# There are other ways to d oit so you dont need to download them locally
for results in satelites:
    earthaccess.download(results, "./local_folder")
    
# TODO - is the folloing comment true?
#This method works best if you are in the same Amazon Web Services (AWS) region as the data (us-west-2) and you are working with gridded datasets (processing level 3 and above). 

#  The following may slow us down while trinaing the model, so we may need to find a way to download the data in a more efficient way.

# for results in satelites:
#     files = earthaccess.open(results)
#     ds = xr.open_mfdataset(files)



'''Below info about satelites written by chat GPT accuracy may varry

AU_SI12             -   AMSRE/AMSR2 Unified L3 Daily 12.5km Brightness Temperatures, Sea Ice Concentration, Motion & Snow Depth V002: In addition to sea ice concentration, this dataset includes brightness temperatures, motion, and snow depth information. These additional variables can serve as features for your predictive model, potentially enhancing its performance.
SENTINEL-1A_SLC     -   SENTINEL-1A Single Look Complex: SENTINEL-1A provides SAR (Synthetic Aperture Radar) data, which can be valuable for observing sea ice dynamics, including ice motion and deformation. You can preprocess the SAR data to derive features such as backscatter intensity and texture, which can be used as inputs to your predictive model.
MYD29               -   MODIS/Aqua Sea Ice Extent 5-Min L2 Swath 1km: MODIS data provides high-resolution imagery of sea ice extent. You can use this dataset to extract spatial features related to sea ice morphology and distribution, which can complement the information obtained from other datasets.
'''