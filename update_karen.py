import subprocess
from discordwebhook import Discord

discord =Discord(url="https://discord.com/api/webhooks/1159367662258892810/ay4nRvPFhN7qxYAJoa2lMKjZFTwljCvfPBHFs9bkK5amQ96QYCGblxvzgzmiJxnHVdMx")

notebook_file1 = r"D:\vs code\python\DeepLearning\Projects\Karen\v2\training.py"
notebook_file2 = r"D:\vs code\python\DeepLearning\Projects\Karen\v2\Networks\functional.py"
notebook_file3 = r"D:\vs code\python\DeepLearning\Projects\Karen\v2\Networks\non_functional.py"

def execute(notebook_file):
    try:
        return_code = subprocess.call(notebook_file, shell=True)
        if return_code == 0:
            print(f"Conversion of {notebook_file} successful.")
        else:
            print(f"Conversion of {notebook_file} failed with return code {return_code}.")
    except Exception as e:
        print(f"An error occurred while converting {notebook_file}: {str(e)}")
        discord.post(content=f"An error occurred while converting {notebook_file}: {str(e)}")

execute(notebook_file1)
execute(notebook_file2)
execute(notebook_file3)

discord.post(content="Karen v2 Training Completed...")