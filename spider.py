import requests
import csv
import time
from urllib3.exceptions import InsecureRequestWarning

class Spider :
    def __init__(self, headers, url, output):
        self.headers = headers
        self.url = url
        self.output = output

    def crawl(self, times, duration=10):
        print("Collecting comments...")
        comments_text = []
        max_id = ""

        # Suppress only the single warning from urllib3 needed.
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        i = 0
        # for i in range(times):
        while i < times:
            try:
                # proxy = ip_addresses[random.randint(0, len(ip_addresses)-1)]
                # proxies = {
                #     "http" : proxy,
                #     "https" : proxy
                # }
                # r = requests.get(self.url+str(max_id), headers=self.headers, proxies=proxies,verify=False)
                r = requests.get(self.url+str(max_id), headers=self.headers,verify=False)
                # print("Request sent using ip: " + proxy)
                max_id = r.json()["max_id"]
                comments = r.json()["data"]
        
                # Append the text of each comment to the comments_text list
                for comment in comments:
                    comments_text.append(comment["text_raw"])
                print("Collection left: " + str(times-i))
                i += 1
            except Exception as e:
                print(f"Sleeping for {duration} seconds, don't exit the application...")
                time.sleep(duration)
                continue

        # Save the comments to a CSV file
        with open(self.output, "w", newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for comment_text in comments_text:
                writer.writerow([comment_text])
                # print(comment_text)

        return 'Comments collected.'
    


