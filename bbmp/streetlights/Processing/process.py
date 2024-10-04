import numpy as np
import pandas as pd

def shift_row_and_repopulate(df, columns):
    # Get the number of columns
    num_cols = len(df.columns)
    
    # Function to shift a single row
    def shift_single_row(row):
        if pd.isna(row.iloc[-columns:]).all():
            shifted = pd.Series([np.nan] * columns + list(row.iloc[:-columns]), index=row.index)
            return shifted
        return row
    
    # Apply the shift function to each row
    df_shifted = df.apply(shift_single_row, axis=1)
    
    # Repopulate the first columns columns of shifted rows
    for i in range(1, len(df_shifted)):
        if pd.isna(df_shifted.iloc[i, :columns]).all():
            df_shifted.iloc[i, :columns] = df_shifted.iloc[i-1, :columns]
    
    return df_shifted

files = ['BommanahalliZoneStreetlights', 'DasarahalliZoneStreetlights', 'EastZoneStreetlights', 'RajarajeshwarinagarZoneStreetlights']

for file in files:

    df = pd.read_csv(f'{file}.csv')

    df.columns = ['Sl. No.', 'RR No.', 'Energy Meter Latitude', 'Energy Meter Longitude', 'Pole No.', 'Pole Latitude', 'Pole Longitude', 'Type', 'No. of Lights', 'Road Category', 'Rated Wattage', 'Rated Wattage (Proposed)']
    if 'EastZone' in file:
        df.columns = ['Sl. No.', 'RR No.', 'Energy Meter Latitude', 'Energy Meter Longitude', 'Pole No.', 'Pole Latitude', 'Pole Longitude', 'Type', 'Road Category', 'Rated Wattage', 'No. of Lights', 'Rated Wattage (Proposed)']

    df = df.dropna(thresh=len(df.columns) - 5)
    df = df.drop('Sl. No.', axis=1)

    df = df[~df.apply(lambda r: r.astype(str).str.contains('Rated').any(), axis=1)]

    shift_by = 3
    if 'Dasarahalli' in file:
        shift_by = 1
    df = shift_row_and_repopulate(df, shift_by)

    df.to_csv(f'{file}_Cleaned.csv', index=False)
