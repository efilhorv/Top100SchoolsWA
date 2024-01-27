import geopandas as gpd
import folium
from folium import plugins
import pandas as pd

# Caminhos para os arquivos GeoJSON
file1_path = r'C:\Users\efilh\OneDrive\Documentos\PROJECT_18\Data_Geojson\Cycle_Routes.geojson'
file2_path = r'C:\Users\efilh\OneDrive\Documentos\PROJECT_18\Data_Geojson\Schools_Public.geojson'

# Carregar os dados GeoJSON usando geopandas
gdf1 = gpd.read_file(file1_path)
gdf2 = gpd.read_file(file2_path)

# Assuming the GeoDataFrames already have a CRS, get the EPSG code
crs_code = gdf1.crs.to_epsg()

# Set CRS for both GeoDataFrames
gdf1 = gdf1.to_crs(epsg=crs_code)
gdf2 = gdf2.to_crs(epsg=crs_code)

# Unir os dois DataFrames GeoPandas
merged_gdf = gpd.GeoDataFrame(pd.concat([gdf1, gdf2], ignore_index=True))

# Convert timestamp columns to string format
for col in merged_gdf.columns:
    if isinstance(merged_gdf[col].iloc[0], pd.Timestamp):
        merged_gdf[col] = merged_gdf[col].dt.strftime('%Y-%m-%d %H:%M:%S')

# Calcular o centro do mapa
center_lat = merged_gdf.geometry.centroid.y.mean()
center_lon = merged_gdf.geometry.centroid.x.mean()

# Criar um mapa folium centrado no ponto médio
my_map = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# Adicionar as geometrias ao mapa
folium.GeoJson(merged_gdf).add_to(my_map)

# Adicionar controle de camadas para alternar entre os mapas
folium.LayerControl().add_to(my_map)
my_map.save('merged_map.html')  

