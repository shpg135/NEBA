import pandas as pd
import glob
folder_path = r'I:\playoffs\pbp'
file_list = glob.glob(folder_path + "/*.csv")
data_frames = []

for file in file_list:
    data_frames.append(pd.read_csv(file))
merged_df = pd.concat(data_frames)
merged_df.to_csv(r'I:\playoffs\pbp\merged_file.csv', index=False)