from pathlib import Path
import pandas as pd

data_dir = Path("data copy")#Path("2021")
df = pd.read_excel("Legend for LOAD100.xlsx")
mapping = dict(zip(df['Subject ID #'],df['Sort Order #']))

def rename_file(file, is_subdir):
    name = file.name
    l = 0
    if is_subdir:
        while name[l] != "_":
            l += 1
        l += 1
    else:
        while name[l] != "k":
            l += 1
        l += 2
    r = l
    while name[r] != "_":
        r += 1
    try:
        old_id = int(name[l:r])
        new_id = mapping[old_id]
    except (KeyError, ValueError) as e:
        print(f"Skipping file {file.name}: {e}")
        return -1
    new_name = name[:l] + "#" + str(new_id) + name[r:]
    new_path = file.with_name(new_name)
    file.rename(new_path)
    print(f"Renamed {name} to {new_name}")
    return 0

def rename_file(file):
    name = file.name
    l = 0
    while name[l] != "k":
        l += 1
    l += 2
    r = l
    while name[r] != "_":
        r += 1
    try:
        old_id = int(name[l:r])
        new_id = mapping[old_id]
    except (KeyError, ValueError) as e:
        print(f"  Skipping file {file.name}: {e}")
        return -1
    new_name = name[:l] + "#" + str(new_id) + name[r:]
    new_path = file.with_name(new_name)
    #file.rename(new_path)
    print(f"  Renamed {name} to {new_name}")
    return 0

for subdir in data_dir.iterdir():
    if not subdir.is_dir():
        continue
    print(f"{subdir}:")
    for file in subdir.iterdir():
        if file.is_dir():
            continue
        rename_file(file)
    #rename_file(subdir, True)