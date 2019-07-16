###############################################################################
# LICENSE
#Copyright (C) 2018 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
###############################################################################
#======================================================================================================
# GNC-A Blog Python Tutorial: Part IX
#======================================================================================================
# Required libraries ==================================================================================
import matplotlib
matplotlib.use('Agg') # use a non-interactive backend
import matplotlib.pyplot as plt # Import the Matplotlib package
from mpl_toolkits.basemap import Basemap # Import the Basemap toolkit
import numpy as np # Import the Numpy package
from remap import remap # Import the Remap function
from cpt_convert import loadCPT # Import the CPT convert function
from matplotlib.colors import LinearSegmentedColormap # Linear interpolation for color maps
import datetime # Library to convert julian day to dd-mm-yyyy
from matplotlib.patches import Rectangle # Library to draw rectangles on the plot
from netCDF4 import Dataset # Import the NetCDF Python interface
import sys # Import the "system specific parameters and functions" module
import os # Miscellaneous operating system interfaces
import subprocess
from math import sin
import glob
#======================================================================================================
# Load the Data =======================================================================================
# Path to the GOES-16 image file
path = sys.argv[1]

# Getting information from the file name ==============================================================
# Search for the Scan start in the file name
Start = (path[path.find("_s")+2:path.find("_e")])
# Search for the GOES-16 channel in the file name
if path.find("M6C") != -1:
  Band = int((path[path.find("M6C")+3:path.find("_G16")]))
else:
  Band = int((path[path.find("M3C")+3:path.find("_G16")]))

# Create a GOES-16 Bands string array
Wavelenghts = ['[]','[0.47 .m]','[0.64 .m]','[0.865 .m]','[1.378 .m]','[1.61 .m]','[2.25 .m]','[3.90 .m]','[6.19 .m]','[6.95 .m]','[7.34 .m]','[8.50 .m]','[9.61 .m]','[10.35 .m]','[11.20 .m]','[12.30 .m]','[13.30 .m]']
 
# Converting from julian day to dd-mm-yyyy
year = int(Start[0:4])
dayjulian = int(Start[4:7]) - 1 # Subtract 1 because the year starts at "0"
dayconventional = datetime.datetime(year,1,1) + datetime.timedelta(dayjulian) # Convert from julian to conventional
date = dayconventional.strftime('%d/%m/%Y') # Format the date according to the strftime directives
time = Start [7:9] + ":" + Start [9:11] + " UTC" # Time of the Start of the Scan

#Channel name:
if Band<=9:
  CHname='0'+str(Band)
else:
  CHname=str(Band)

# Condition for Band02 - Times Constraints:
if Band==2:
  n = dayjulian
  hr = int(Start[7:9])
  mn = int(Start[9:11])
  a = 3.141592654/180
  ###
  hrs = hr + (mn/60)
  hi=9.25+0.75*sin(a*(360/365)*(284+n))
  hf=20.25-0.75*sin(a*(360/365)*(284+n))
  if hrs<hi or hrs>hf:
    with open('//produtos//ch' + CHname + '//G16_Log.txt', 'a') as log:
      log.write(path.replace('\\\\', '\\') + '\n')
    sys.exit()# Stop script immediately

# Get the unit based on the channel. If channels 1 trough 6 is Albedo. If channels 7 to 16 is BT.
if Band <= 6:
  Unit = "Reflectance"
else:
  Unit = "Brightness Temperature [oC]"

# Choose a title for the plot:
if Band==2:
  Title = " GOES-16  -   " +"CH" + CHname + "                                                            " + date + " - " + time
elif Band==8 or Band==9:
  Title = " GOES-16  -   " +"CH" + CHname + "                                                                         " + date + " - " + time
elif Band!=2:
  Title = " GOES-16  -   " +"CH" + CHname + "                                   " + date + " - " + time
# Insert the institution name
Institution = "FURNAS/GPH.O"
# =====================================================================================================
# Open the file using the NetCDF4 library
nc = Dataset(path)
# Get the latitude and longitude image bounds
geo_extent = nc.variables['geospatial_lat_lon_extent']
min_lon = float(geo_extent.geospatial_westbound_longitude)
max_lon = float(geo_extent.geospatial_eastbound_longitude)
min_lat = float(geo_extent.geospatial_southbound_latitude)
max_lat = float(geo_extent.geospatial_northbound_latitude)
 
# Choose the visualization extent (min lon, min lat, max lon, max lat)
# South America
if Band==8 or Band==9:
  extent = [-110.0, -60.0, -25.0, 15.0]
else:
  extent = [-90.0, -60.0, -30.0, 15.0]
# Full Disk
#extent = [min_lon, min_lat, max_lon, max_lat]
 
# Choose the image resolution (the higher the number the faster the processing is)
if Band == 2:
  resolution = 1
else:
  resolution = 2
 
# Calculate the image extent required for the reprojection
H = nc.variables['goes_imager_projection'].perspective_point_height
x1 = nc.variables['x_image_bounds'][0] * H
x2 = nc.variables['x_image_bounds'][1] * H
y1 = nc.variables['y_image_bounds'][1] * H
y2 = nc.variables['y_image_bounds'][0] * H
#x1 = -5434894.885056
#x2 = 5434894.885056
#y1 = -5434894.885056
#y2 = 5434894.885056
 
print(x1)
print(x2)
print(y1)
print(y2)
 
# Call the reprojection funcion
#grid = remap(path, extent, resolution, x1, y1, x2, y2)
grid = remap(path, extent, resolution, x1, y1, x2, y2)
 
# Read the data returned by the function
if Band <= 6:
  data = grid.ReadAsArray()
else:
  # If it is an IR channel subtract 273.15 to convert to Celsius

  data = grid.ReadAsArray() - 273.15
  # Make pixels outside the footprint invisible
  data[data <= -180] = np.nan
 
print("The total number of pixels is:")
print(data.shape)
#======================================================================================================
# Define the size of the saved picture=================================================================
#print (data.shape)
DPI = 150
fig = plt.figure(figsize=(data.shape[1]/float(DPI), data.shape[0]/float(DPI)), frameon=False, dpi=DPI)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax = plt.axis('off')
#======================================================================================================
# Plot the Data =======================================================================================
# Create the basemap reference for the Rectangular Projection
bmap = Basemap(llcrnrlon=extent[0], llcrnrlat=extent[1], urcrnrlon=extent[2], urcrnrlat=extent[3], epsg=4326)
# Draw the countries and Brazilian states shapefiles

if Band == 2:
  bmap.readshapefile('/dados/backup_homefazzt/download/ne_10m_admin_0_countries','ne_10m_admin_0_countries',linewidth=0.50,color='#FFFFFF')
  bmap.readshapefile('/dados/backup_homefazzt/download/shape/Brasil_com_estados','estados_2010',linewidth=0.40,color='#FFFFFF')

else:
  bmap.readshapefile('/dados/backup_homefazzt/download/ne_10m_admin_0_countries','ne_10m_admin_0_countries',linewidth=0.50,color='#000000')
  bmap.readshapefile('/dados/backup_homefazzt/download/shape/Brasil_com_estados','estados_2010',linewidth=0.40,color='#000000')


#Sahpes - Furnas:
bmap.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/138kV_2D','138kV',linewidth=1.0,color='#FF0000')
bmap.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/230kV_2D','230kV',linewidth=1.0,color='#00FF09')
bmap.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/345kV_2D','345kV',linewidth=1.0,color='#FFC400')
bmap.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/500kV_2D','500kV',linewidth=1.0,color='#001AFF')
bmap.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/600kV_2D','600kV',linewidth=1.0,color='#FF00EF')
bmap.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/750kV_2D','750kV',linewidth=1.0,color='#00FFFF')

# Draw parallels and meridians
#bmap.drawparallels(np.arange(-90.0, 90.0, 5.0), linewidth=0.2, dashes=[4, 4], color='white', labels=[False,False,False,False], fmt='%g', labelstyle="+/-", xoffset=-0.80, yoffset=-1.00, size=7)
#bmap.drawmeridians(np.arange(0.0, 360.0, 5.0), linewidth=0.2, dashes=[4, 4], color='white', labels=[False,False,False,False], fmt='%g', labelstyle="+/-", xoffset=-0.80, yoffset=-1.00, size=7)
#if Band = 7 and Band = 10:
# Converts a CPT file to be used in Python
if Band == 2:
  cpt = loadCPT('/dados/backup_homefazzt/download/GMT_grey.cpt')
  cpt_convert = LinearSegmentedColormap('cpt', cpt)
  bmap.imshow(data, origin='upper', cmap=cpt_convert, vmin=0, vmax=1)
elif Band==8 or Band==9: #WV
  cpt= loadCPT('/dados/backup_homefazzt/download/WVCOLOR35.cpt')
  cpt_convert = LinearSegmentedColormap('cpt', cpt)
  bmap.imshow(data, origin='upper', cmap=cpt_convert, vmin=-105,vmax=105)
else:
  cpt = loadCPT('/dados/backup_homefazzt/download/IR4AVHRR6.cpt')
  cpt_convert = LinearSegmentedColormap('cpt', cpt)
  bmap.imshow(data, origin='upper', cmap=cpt_convert, vmin=-103, vmax=84)
# Makes a linear interpolation
#cpt_convert = LinearSegmentedColormap('cpt', cpt)
# Plot the GOES-16 channel with the converted CPT colors (you may alter the min and max to match your preference)
#bmap.imshow(data, origin='upper', cmap=cpt_convert, vmin=-103, vmax=84)
# Insert the colorbar at the bottom
 
if Band <= 6:
# Insert the colorbar at the bottom
# Plot the GOES-16 channel with the converted CPT colors (you may alter the min and max to match your preference)
  cb = bmap.colorbar(location='bottom', size = '2.5%', pad = '-1.2%', ticks=[20, 40, 60, 80])
  cb.ax.set_xticklabels(['20', '40', '60', '80'])
else:
  # Insert the colorbar at the bottom
  cb = bmap.colorbar(location='bottom', size = '2.5%', pad = '-1.2%')
  cb.outline.set_visible(False) # Remove the colorbar outline
  cb.ax.tick_params(width = 0) # Remove the colorbar ticks
  cb.ax.xaxis.set_tick_params(pad=-30) # Put the colobar labels inside the colorbar
  cb.ax.tick_params(axis='x', colors='yellow', labelsize=30) # Change the color and size of the colorbar labels
 
# Add a black rectangle in the bottom to insert the image description
lon_difference = (extent[2] - extent[0]) # Max Lon - Min Lon
currentAxis = plt.gca()
#Correction of ySize
if Band!=8 and Band!=9:
  crt=0.85
  factor=0.040
elif Band==8 or Band==9:
  crt=0.85
  factor=0.030
currentAxis.add_patch(Rectangle((extent[0], extent[1] + crt) ,lon_difference-0.01 , lon_difference*factor , alpha=0.8, zorder=3, facecolor='black'))
 
# Add the image description inside the black rectangle
lat_difference = (extent[3] - extent[1]) # Max lat - Min lat
#if Band==2:
#  figx=80
#  figy=280
#  wsize=40
#elif Band!=2:
#  figx=40
#  figy=110
#  wsize=30

# Set position and imagefile to be used (Furnas logo):
if Band==2:
  figx=80
  figy=230
  logo_read='logo3.png'
  wsize=45
elif Band==8 or Band==9:
  figx=30
  figy=120
  logo_read='logo2_modificado.png'
  wsize=30
elif Band!=2:
  figx=40
  figy=120
  logo_read='logo2_modificado.png'
  wsize=30

#Text position:
if Band!=8 or Band!=9:
  ypc=1.5
else:
  ypc=2.5

plt.text(extent[2]-0.5, extent[1] +ypc  ,Title,horizontalalignment='right', color = 'white', size=wsize)
plt.text(extent[0]+2, extent[1] + ypc  ,Institution, horizontalalignment='left', color = 'yellow', size=wsize)
 
# Add logos / images to the plot
#Logo - Furnas:
logo_elet = plt.imread('/dados/backup_homefazzt/download/' + logo_read)
plt.figimage(logo_elet, figx,figy , zorder=3, alpha = 1, origin = 'upper')

#logo_GNC = plt.imread('/dados/backup_homefazzt/download/GNC Logo.png')
#logo_INPE = plt.imread('/dados/backup_homefazzt/download/INPE Logo.png')
#logo_NOAA = plt.imread('/dados/backup_homefazzt/download/NOAA Logo.png')
#logo_GOES = plt.imread('/dados/backup_homefazzt/download/GOES Logo.png')
#ax.figimage(logo_GNC, 10, 50, zorder=3, alpha = 1, origin = 'upper')
#ax.figimage(logo_INPE, 400, 50, zorder=3, alpha = 1, origin = 'upper')
#ax.figimage(logo_NOAA, 500, 50, zorder=3, alpha = 1, origin = 'upper')
#ax.figimage(logo_GOES, 585, 50, zorder=3, alpha = 1, origin = 'upper')
 
date_save = dayconventional.strftime('%Y%m%d')
time_save = Start [7:9] + Start [9:11]
 
# Save the result
plt.savefig('//produtos//ch' + CHname + '//G16_C' + CHname + '_' + date_save + time_save + '.png', dpi=DPI, pad_inches=0, transparent=True)
plt.close()

# Add to the log file (called "G16_Log.txt") the NetCDF file name that I just processed.
# If the file doesn't exists, it will create one.
with open('//produtos//ch' + CHname + '//G16_Log.txt', 'a') as log:
 log.write(path.replace('\\\\', '\\') + '\n')

# Create links for loops in html 
path = "/produtos/ch" + CHname + "/loop" 
os.chdir(path)
lista=glob.glob('*.png')

if len(lista)<20:
  ind = 1
  name=[]
  for arqv in os.popen("ls -tr1 /produtos/ch" + CHname + "/G16_C* | tail -20"):
    numimg = str(ind)
    z = "convert " + arqv + " -resize 25% /produtos/ch" + CHname + "/loop/img" + numimg + ".png"
    name.append(z)
    ind += 1
  for string in name:
    string = string.replace('\n', ' ').replace('\r', '')
    os.system(string)

elif len(lista)>=20:
  for i in range(2,len(lista)+1,1):
      name_img ='img%s.png' %(i)
      name_new='img%s.png' %(i-1)
      os.rename(name_img, name_new)
    #Faz apenas a ultima imagem gerada
  path= "/produtos/ch" + CHname
  lst_furnas=sorted(os.listdir(path))
  last=lst_furnas[-4]
  arqv = path + '/' + last
  string = "convert " +  arqv +  " -resize 50% /produtos/ch" + CHname +  "/loop/img20.png"
  os.system(string)

#======================================================================================================
#======================================================================================================

#======================================================================================================
# Crop image and create legend using "Imagemagick" 

leg = dayconventional.strftime('%d') + "/" + dayconventional.strftime('%m') + "/" + dayconventional.strftime('%Y') + "  " + Start [7:9] + ":" + Start [9:11] + "Z"

if Band == 13:
  arqorig = '//produtos/ch13/G16_C13_' + date_save + time_save + '.png'
  arqdest = '//produtos/ch13/furnas/' + date_save + time_save + '_G16_C13_Furnas.png'
  flagsvar = " -crop 1200x1400+1700+1300 -font helvetica -fill yellow -pointsize 32 -gravity center -draw " + '"text 1050,595' + "'" + leg + "'" + '"'
  os.system("/usr/bin/convert " + arqorig + flagsvar + " " + arqdest)

if Band == 2:
  arqorig = '//produtos/ch02/G16_C02_' + date_save + time_save + '.png'
  arqdest = '//produtos/ch02/furnas/' + date_save + time_save + '_G16_C02_Furnas.png'
  flagsvar = " -crop 2400x2800+3400+2600 -font helvetica -fill yellow -pointsize 56 -gravity center -draw " + '"text 2150,1190' + "'" + leg + "'" + '"'
  os.system("/usr/bin/convert " + arqorig + flagsvar + " " + arqdest)


#Furnas areas:
if Band == 2 or Band == 13:
  if Band==2:
    path='/produtos/ch02/furnas/loop'
    os.chdir(path)
    lst=glob.glob('*.png')
  elif Band==13:
    path='/produtos/ch13/furnas/loop'
    os.chdir(path)
    lst=glob.glob('*.png')
  #Se nesta pasta nao houver 20 imagens criadas, vai executar o script para criar: 
  if len(lst)<=20:
    ind = 1
    name=[]
    for arqv in os.popen("ls -1 /produtos/ch" + CHname + "/furnas/*.png | tail -20"):
      numimg = str(ind)
      if Band == 2:
        z = "convert " + arqv + " -resize 50% /produtos/ch02/furnas/loop/img" + numimg + ".png"
      else:
        z = "cp " + arqv + " /produtos/ch13/furnas/loop/img" + numimg + ".png"
      name.append(z)
      ind += 1

    for string in name:
      string = string.replace('\n', ' ').replace('\r', '')
      os.system(string)
  #Se a lista tiver 20 imagens, pega as ultimas 19 e atualiza o nome, em seguida busca a ultima imagem gerada no /produtos e faz a conversao apenas desta.
  elif len(lst)>20:
    for i in range(2,len(lst)+1,1):
      name_img ='img%s.png' %(i)
      name_new='img%s.png' %(i-1)
      os.rename(name_img, name_new)
    #Faz apenas a ultima imagem gerada
    if Band==2:
      path='/produtos/ch02/furnas'
      lst_furnas=sorted(os.listdir(path))
      last=lst_furnas[-2]
      arqv = path + '/' + last
      string = "convert " +  arqv +  " -resize 50% /produtos/ch02/furnas/loop/img20.png"
    elif Band==13:
      path='/produtos/ch13/furnas'
      lst_furnas=sorted(os.listdir(path))
      last=lst_furnas[-2]
      arqv = path + '/' + last
      string  = "cp " + arqv + " /produtos/ch13/furnas/loop/img20.png"
    os.system(string)
#======================================================================================================
