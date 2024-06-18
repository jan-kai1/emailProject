from simplegmail import Gmail
from simplegmail.query import construct_query
from regexes import replaceLinks
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

load_dotenv("gemini.env")
# API_KEY = gemini.env.ENV_API_KEY
API_KEY = os.getenv('ENV_API_KEY')
# if API_KEY:
#     print(API_KEY)
# else:
#     print("not found")
genai.configure(api_key = API_KEY )
model = genai.GenerativeModel("gemini-1.5-flash")
gmail = Gmail()

query_params = {
    "newer_than" : (4 , "day"),
    # "unread" : True,
    "in" : "inbox"

}
def summarizeEmail(text):
    maxTries = 5
    attempts = 0
    def trySummarize(text) :
        nonlocal attempts
        try:
            filtered = replaceLinks(text)
            # print(filtered)
            summary = model.generate_content(f"Summarize this: {filtered}").text
           
            if summary == None:
                attempts += 1
                return trySummarize(text)
            return summary

        except Exception as e:
            if attempts < maxTries:

                attempts += 1
                time.sleep(1)
                trySummarize(text)
            else:
                print("max tries reached")
                raise e
    return trySummarize(text)

            
def testData(): 
    messages = gmail.get_messages(query = construct_query(query_params))
    for msg in messages:
        print(msg.sender)
        print("---")
        if msg.plain:
            
            print(replaceLinks(msg.plain))
            print(f"summary: {summarizeEmail(msg.plain)}")
        else:
            print("no message")
   
def readEmail():

    messages = gmail.get_messages(query = construct_query(query_params))
    data =[]
    for msg in messages:
        summary = ""
        
        if msg.plain:
            summary = summarizeEmail(msg.plain)
          
            
        msgObj = { "sender" : msg.sender, "snippet" : msg.snippet, "plain" : msg.plain, "summary" : summary}
        data.append(msgObj)
   
    return data
    # for msg in messages:
    #     print ("To " + msg.recipient)
    #     print("From: " + msg.sender)
    #     if (msg.preview):
    #         print
    #     if (msg.plain):
    #         print("Text: " + replaceLinks(msg.plain))
        
    #     print("---")

def main():
    readEmail()

if __name__ == "__main__":
    main()