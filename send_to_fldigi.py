import os
import shutil
import time
import pyfldigi
import datetime

def send_to_fldigi(content):
    current_datetime = datetime.datetime.now()
    message = '\n\n### Callsign here - Radiotext - ' + current_datetime.strftime("%Y-%m-%d %H:%M:%S") + '###\n' + content + '\n### END Radiotext ###\n\n'
    fldigi.main.send(message,True,200000)
    fldigi.delay(1000)  # wait a bit
    fldigi.main.rx()  # Put flgidigi into receive mode


def remove_file(file_path):
    # Code to remove the file
    os.remove(file_path)
    print(f"File {file_path} removed.")

def process_txt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt") or filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"File {file_path} sending.")
                send_to_fldigi(content)
            remove_file(file_path)
            time.sleep(10) # wait a bit

# Specify the directory where the .txt files are located
directory = "txtfiles"

# Initialize fldigi
fldigi = pyfldigi.Client()

#Loop
while True:
	# Process the .txt files in the directory
	process_txt_files(directory)
	time.sleep(10) # wait a bit
