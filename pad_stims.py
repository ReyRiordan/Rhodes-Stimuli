import os
import wave
import numpy as np

# Path to your folder containing the .wav files
folder_path = r'C:\Users\mattp\Downloads\French male Mathieu-20250122T000241Z-001\French male Mathieu'

# Specify the duration of the silent padding (in seconds)
silent_duration_s = .5  

# Go through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith("_root.mp3"):
        # Full path to the .wav file
        file_path = os.path.join(folder_path, filename)
        
        # Open the .wav file
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
        silence = np.zeros(int(frame_rate * silent_duration_s) * num_channels * sample_width, dtype=np.int16)

        # Combine the silence with the original audio data
        padded_audio = silence.tobytes() + audio_data
        
        # Save the new padded file
        output_path = os.path.join(folder_path, "padded", f"padded_{filename}")
        with wave.open(output_path, 'wb') as output_file:
            output_file.setparams(params)
            output_file.writeframes(padded_audio)

        print(f"Processed: {filename}")