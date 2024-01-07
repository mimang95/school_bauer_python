import pandas as pd

# Dateinamen der CSV-Dateien
file1 = 'personaldatenbank_asv.csv'
file2 = 'server_schulkonsole.csv'
file3 = 'untis.csv'

# Einlesen der CSV-Dateien
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
print(df1)
print(df2)
print(df3)

# Zusammenführen der Daten basierend auf der Schüler-ID
merged_df = pd.merge(df1, df2, on='Schüler-ID', how='outer')
merged_df = pd.merge(merged_df, df3, on='Schüler-ID', how='outer')

# Umbenennen der Klassenspalten
merged_df = merged_df.rename(columns={
    'Klassenname_x': 'ASV',
    'Klassenname_y': 'Schulkonsole',
    'Klassenname': 'Untis'
})

# Speichern der Ergebnisse in einer neuen CSV-Datei
output_file = 'merged_schueler_daten.csv'
merged_df.to_csv(output_file, index=False)

print(f'Daten wurden erfolgreich in "{output_file}" gespeichert.')
