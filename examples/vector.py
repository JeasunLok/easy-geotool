import sys
sys.path.append(r'E:\project\ljs\easy_geotool\easy_geotool')

from easy_geotool.io.vector import read_vector, write_vector
from easy_geotool.transform.transform import vector_to_raster


data_vector = r"E:\project\ljs\easy_geotool\easy_geotool\examples\data\net3_gd.shp"
data_tif = r"E:\project\ljs\easy_geotool\easy_geotool\examples\data\net3_gd_raster.tif"

# example_vector = read_vector(data_vector, format="shp")
# print(example_vector)

# write_vector(r"E:\project\ljs\easy_geotool\easy_geotool\examples\data\net3_gd.geojson", example_vector, "geojson")

vector_to_raster(data_vector, data_tif, 1000, "field", 1, 1, "Id")

