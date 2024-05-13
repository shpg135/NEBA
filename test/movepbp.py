import os
import shutil

# Define the start and end dates for the season
t = open(r'H:\NEBA_new\teamname.txt','r')
team_links = [x.replace('\n','') for x in t.readlines()]
t.close()
year_list = [year for year in range(1996, 2023)]
date = "0320"
# Create the subfolder for the season
#season_folder = f"H:\\NEBA_new\\pbp\\season\\{start_date[:4]}-{int(start_date[:4])+1}"
#os.makedirs(season_folder, exist_ok=True)
for year in year_list:
    season_folder = f"H:\\NEBA_new\\pbp\\season\\{year}-{int(year) + 1}"
    os.makedirs(season_folder, exist_ok=True)
# Loop through all the files in the current directory
    for team in team_links:
        for file_name in os.listdir(r"H:\NEBA_new\pbp\{}".format(team)):
    # Check if the file name matches the pattern
    # if len(file_name) == 10 and file_name.startswith(start_date) and file_name[8:].isalpha():
    #     # Extract the date and team name from the file name
            date_str = file_name[:8]
    #     team_name = file_name[8:]
    # Check if the date is within the season range
            if str(year)+date <= date_str <= str((int(year)+1))+date:
        # Move the file to the season subfolder
                shutil.move(os.path.join("H:\\NEBA_new\\pbp\\{}\\".format(team),file_name), os.path.join(season_folder, file_name))