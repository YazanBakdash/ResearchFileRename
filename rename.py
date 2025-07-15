from pathlib import Path
import pandas as pd

data_dir = Path("data copy")#Path("2021")
df = pd.read_excel("Legend for LOAD100.xlsx")
mapping = dict(zip(df['Subject ID #'],df['Sort Order #']))

def rename(dir):
    name = dir.name

    new_name = ""
    for i in range(len(name)-4):
        if i+7 <= len(name) and name[i:i+7] == "63995_b":
            new_name = name[:i] + "#78" + name[i+7:]
            break
        
        s = name[i:i+5]
        if s.isdigit() and int(s) in mapping:
            new_id = mapping[int(s)]
            new_name = name[:i] + "#" + str(new_id) + name[i+5:]
    
    if new_name == "":
        return -1
    
    new_path = dir.with_name(new_name)
    dir.rename(new_path)
    print(f"   Renamed {name} to {new_name}")
    return 0

for subdir in data_dir.iterdir():
    if not subdir.is_dir():
        continue
    print(f"Checking '{subdir}':")
    for file in subdir.iterdir():
        if file.is_dir() or file.suffix != ".raw":
            continue
        rename(file)
    rename(subdir)