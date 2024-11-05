import os

# Define the path for the new output folder
output_folder_path = os.path.expanduser("~/Desktop/Stroke_Prediction/output")

# Create the output folder if it doesn't already exist
os.makedirs(output_folder_path, exist_ok=True)
print(f"Output folder created at: {output_folder_path}")

