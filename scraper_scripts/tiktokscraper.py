from apify_client import ApifyClient
from dotenv import load_dotenv
load_dotenv()
import os

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_ID"))


hashtags_file = open('tophashtags.txt', 'r')

array_of_hashtags = hashtags_file.readlines()
array_of_hashtags = [hashtag.strip() for hashtag in array_of_hashtags]

# Prepare the Actor input
run_input = {
    "hashtags": array_of_hashtags,
    "resultsPerPage": 20,
    "shouldDownloadVideos": False,
    "shouldDownloadCovers": False,
    "shouldDownloadSlideshowImages": False,
}

# Run the Actor and wait for it to finish
run = client.actor("OtzYfK1ndEGdwWFKQ").call(run_input=run_input)

hashtag_outfile = open('videohashtags2.csv', 'w')
hashtag_outfile.write("id,webVideoUrl,hashtags\n") #header

count = 1
# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    # print(item) #print this out for all the possible data
    # print(item["hashtags"])
    hashtag_outfile.write(item["id"] + "," + item["webVideoUrl"] + ",")
    for hashtag in item["hashtags"]:
        hashtag_outfile.write(hashtag["name"] + " ")
    hashtag_outfile.write('\n')
    