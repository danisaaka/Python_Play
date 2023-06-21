import os

# Get the current working directory
current_directory = os.getcwd()

# File paths
starting_letter_path = "Input/Letters/starting_letter.txt"
invited_names_path = "Input/Names/invited_names.txt"
output_folder = "Output/ReadyToSend"

# Construct the full paths
starting_letter_path = os.path.join(current_directory, starting_letter_path)
invited_names_path = os.path.join(current_directory, invited_names_path)
output_folder_path = os.path.join(current_directory, output_folder)

# Open the starting letter template file
with open(starting_letter_path) as letter_file:
    letter_contents = letter_file.read()

# Open the invited names file
with open(invited_names_path) as names_file:
    invited_names = names_file.readlines()

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through each name
for name in invited_names:
    # Replace the [name] placeholder with the actual name
    personalized_letter = letter_contents.replace("[name]", name.strip())

    # Save the output to a file in the Output folder
    filename = os.path.join(output_folder_path, f"{name.strip()}.txt")
    with open(filename, "w") as output_file:
        output_file.write(personalized_letter)
