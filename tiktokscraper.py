from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_O6vB0s3dvxz1eOYpkiS77HkNkt9ypB1aRKgT")

# Prepare the Actor input
run_input = {
    "hashtags": ["relatable","real","fortnite","adiosenero","viralvideotiktok","alastor","tiktokshopping","trendingbooks2024","multiaverso","acefamily","lanternrite2024"],
    "resultsPerPage": 10,
    "shouldDownloadVideos": False,
    "shouldDownloadCovers": False,
    "shouldDownloadSlideshowImages": False,
}

# Run the Actor and wait for it to finish
run = client.actor("OtzYfK1ndEGdwWFKQ").call(run_input=run_input)
count = 1
# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"==================TIKTOK #{count} CAPTION==================")
    print(item["text"])
    count += 1