import pandas as pd

# Az egyesítendő Excel fájlok elérési útvonalai
file1_path = 'elso_fajl.xlsx'
file2_path = 'masodik_fajl.xlsx'

# Az Excel fájlok beolvasása DataFrame-ekbe
df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)

# A DataFrame-ek összefűzése (a sorok alá kerülnek)
merged_df = pd.concat([df1, df2], ignore_index=True)

# Az egyesített DataFrame mentése egy új Excel fájlba
output_path = 'egyesitett_fajl.xlsx'
merged_df.to_excel(output_path, index=False)

print(f'A két Excel fájl egyesítve lett a "{output_path}" fájlba.')
