import os
import wave
import numpy as np
import csv

# Path to your folder containing the .wav files
folder_path = r'C:\Users\laima\Downloads\(spliced) French male Mathieu -20250205T150942Z-001\(spliced) French male Mathieu'
pad_array = []

with open('Root_lengths.csv', newline='') as csvfile:
    next(csvfile)
    read = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in read:
        pad = 0.5 - float(row[1])
        pad_array.append([row[0], pad])
        # print(pad)

print(pad_array)
# Specify the duration of the silent padding (in seconds)
silent_duration_s = .25  


i = 0
# Go through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith("_root.mp3"):
        # Full path to the .wav file
        file_path = os.path.join(folder_path, filename)
        
        # # Open the .wav file
        with wave.open(file_path, 'rb') as audio_file:
            # Get the parameters from the original file
            params = audio_file.getparams()
            num_channels = params.nchannels
            sample_width = params.sampwidth
            frame_rate = params.framerate
            num_frames = params.nframes
            
            # Read the audio data
            audio_data = audio_file.readframes(num_frames)
        
        # Create silence (all zeroes) for the padding
        silence = np.zeros(int(frame_rate * pad_array[i][1] * 0.5) * num_channels * sample_width, dtype=np.int16)
        i = i + 1

        # Combine the silence with the original audio data
        padded_audio = silence.tobytes() + audio_data
        
        # Save the new padded file
        output_path = os.path.join(folder_path, "padded", f"padded_{filename}")
        with wave.open(output_path, 'wb') as output_file:
            output_file.setparams(params)
            output_file.writeframes(padded_audio)


        # Rename the file
        # new_filename = f"{filename[:-10]}_suffix.mp3"
        # new_path = os.path.join(folder_path, new_filename)
        # os.rename(file_path, new_path)

        print(f"Processed: {filename}, using {pad_array[i - 1][0]}")