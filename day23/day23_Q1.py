import requests
import threading
import time

# List of URLs
urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]

# ---------------------------------------
# Function to download and save content
# ---------------------------------------
def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Extract filename from URL
        filename = url.split("/")[-1] + ".txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")



start_time = time.time()

for url in urls:
    download_file(url)

end_time = time.time()
print("\nSequential Download Time:", round(end_time - start_time, 2), "seconds")



threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print("Threaded Download Time:", round(end_time - start_time, 2), "seconds")
