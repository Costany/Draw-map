import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

#
#fname = r'D:\Python\pythonca\区划\市.shp'
#fname1 = r'D:\Python\pythonca\dongli China map\china.shp'
#fname2 = r'D:\Python\pythonca\dongli China map\china_nine_dotted_line.shp'
projection = ccrs.LambertConformal(central_longitude=105, central_latitude=90)
fig = plt.figure(figsize=(20, 18))
ax = plt.axes(projection=projection)
ax.set_extent([82, 129, 13, 55])

ax.add_feature(cfeature.LAND.with_scale('50m'),facecolor='#e8e1c4',edgecolor='#d0a85e')
ax.add_feature(cfeature.COASTLINE.with_scale('50m'),lw=0.25,facecolor='#e8e1c4',edgecolor='#d0a85e')
ax.add_feature(cfeature.OCEAN.with_scale('50m'),color='#e6e6ff')
#shape_feature = ShapelyFeature(Reader(fname2).geometries(),
#                                ccrs.PlateCarree(), facecolor='white',edgecolor='#d0a85e')
#ax.add_feature(shape_feature)
#shape_feature = ShapelyFeature(Reader(fname1).geometries(),
#                                ccrs.PlateCarree(), facecolor='#e8e1c4',edgecolor='#d0a85e')
#ax.add_feature(shape_feature)
#shape_feature = ShapelyFeature(Reader(fname).geometries(),
#                                ccrs.PlateCarree(), facecolor='#e8e1c4',alpha=0.4,linewidth=1,edgecolor='#d0a85e')
#ax.add_feature(shape_feature)

plt.show()
