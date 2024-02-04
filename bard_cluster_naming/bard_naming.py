import os
import pdb

import argparse
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff


SAFETY_SETTINGS = [
      {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
      },
      {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
      },
      {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
      },
      {
    "category": "HARM_CATEGORY_DANGEROUS",
    "threshold": "BLOCK_NONE"
      },
  ]


class GooglePredictor(object):
    def __init__(self, model_name):
        GOOGLE_API_KEY = "<INSERTKEYHERE>"
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model_name = model_name
        self.client = genai.GenerativeModel(model_name)

    @retry(wait=wait_random_exponential(min=1, max=5), stop=stop_after_attempt(6))
    def get_response(self,msg_list, max_tokens=None):
        try:
            response=self.client.generate_content(msg_list, safety_settings=SAFETY_SETTINGS, generation_config={"max_output_tokens": max_tokens})
            # print(response.text)
            return response.text
        except:
            print(response.prompt_feedback)
            return None

    def predict(self, dp):
        pred_str = self.get_response(dp["input_messages"], dp["max_decode_len"])
        return pred_str


def get_cluster_name(array_of_strings):
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, default="gemini-pro")
    args = parser.parse_args()

    model_name = args.model_name
    google_predictor = GooglePredictor(model_name=model_name)

    query = f"Give a name for the cluster of these strings that relates to the subject of all the strings in the format of ____Tok where ____ is strictly one word and strictly a noun:\n{array_of_strings}"
    msglist = [{"role":"user", "parts": [query]}]
    final_dp = {"input_messages": msglist, "max_decode_len":100}
    response = google_predictor.predict(final_dp)

    return(response)

if __name__=="__main__":
    hashtags_in_cluster = ['Book','Literature','Reading','Fiction','Nonfiction']
    print(get_cluster_name(hashtags_in_cluster))