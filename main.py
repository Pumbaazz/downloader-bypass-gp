import requests
import os

url = input("Enter the URL of the file: ")
file_name = url.split("/")[-1]  # Extracting the file name from the URL
output_path = os.path.join(os.path.expanduser("~"), "Downloads", file_name)

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception if there's an error in the response

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 KB
    bytes_downloaded = 0

    with open(output_path, "wb") as file:
        for data in response.iter_content(block_size):
            file.write(data)
            bytes_downloaded += len(data)
            progress = (bytes_downloaded / total_size) * 100
            print(f"Downloading... {progress:.2f}%")

    print("File downloaded successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error occurred during download: {str(e)}")
