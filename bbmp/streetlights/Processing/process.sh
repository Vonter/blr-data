#!/bin/bash

python process.py

ogr2ogr -f GeoJSON BommanahalliZoneStreetlights.geojson BommanahalliZoneStreetlights_Cleaned.csv -oo X_POSSIBLE_NAMES='Pole Longitude' -oo Y_POSSIBLE_NAMES='Pole Latitude'
ogr2ogr -f GeoJSON DasarahalliZoneStreetlights.geojson DasarahalliZoneStreetlights_Cleaned.csv -oo X_POSSIBLE_NAMES='Pole Longitude' -oo Y_POSSIBLE_NAMES='Pole Latitude'
ogr2ogr -f GeoJSON EastZoneStreetlights.geojson EastZoneStreetlights_Cleaned.csv -oo X_POSSIBLE_NAMES='Pole Longitude' -oo Y_POSSIBLE_NAMES='Pole Latitude'
ogr2ogr -f GeoJSON RajarajeshwarinagarZoneStreetlights.geojson RajarajeshwarinagarZoneStreetlights_Cleaned.csv -oo X_POSSIBLE_NAMES='Pole Longitude' -oo Y_POSSIBLE_NAMES='Pole Latitude'

geojson-merge BommanahalliZoneStreetlights.geojson EastZoneStreetlights.geojson RajarajeshwarinagarZoneStreetlights.geojson > Combined.geojson

ogr2ogr Streetlights.fgb Combined.geojson -skipfailures
