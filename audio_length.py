import wave
import contextlib
import csv
import os

csvoutput = open('Root_lengths.csv', 'w', newline='')
writer = csv.writer(csvoutput)
writer.writerow(['Word', 'Length'])

folder_path = r'C:\Users\mattp\Downloads\French male Mathieu-20250122T000241Z-001\French male Mathieu'

# List all files in the folder
files_in_folder = os.listdir(folder_path)

# Filter files that end with '_root.mp3'
root_mp3_files = [file for file in files_in_folder if file.endswith('_root.mp3')]

# Process each '_root.mp3' file
for file in root_mp3_files:
    file_path = os.path.join(folder_path, file)
    print(f'Reading file: {file_path}')

    with contextlib.closing(wave.open(file_path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print(str(file) + "  " + str(duration))
        writer.writerow([file, duration])
csvoutput.close()
