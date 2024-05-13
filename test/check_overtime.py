import os

directory = r"I:\NEBA_new\pbp\season\2023"
sum = 0
# Loop through all files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        # Check if the file is an HTML file
        if file.endswith(".html"):
            # Open the file and search for the desired word
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                content = f.read()
                if "overtime" in content:
                    print(file)
                    sum += 1

print(sum)