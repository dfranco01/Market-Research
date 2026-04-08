import requests
import json
import os
from dotenv import load_dotenv
# SAM.gov API endpoint
SAM_API_URL = "https://api.sam.gov/prod/opportunities/v2/search"

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_sam_opportunities():
    headers = { 'Accept': 'application/json' }
    params = { 'api_key': API_KEY, 'limit': 25, 'postedFrom': '01/01/2026', 'postedTo': '01/31/2026', 'ptype': ['p', 'o'] }

    #Solicitations only
    response = requests.get(SAM_API_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    opportunities = data.get('opportunitiesData', [])
    for opp in opportunities:
        print(f"Title: {opp.get('title')}")
        print(f"Agency: {opp.get('fullParentPathName')}")
        print(f"Posted: {opp.get('postedDate')}")
        print(f"Deadline: {opp.get('responseDeadLine')}")
        print(f"Type: {opp.get('type')}")
        #Contact info is in an array
        contacts = opp.get('pointOfContact', [])
        if contacts:
            print(f"Contact: {contacts[0].get('email', 'N/A')}")
            print("---")
            
get_sam_opportunities()


#if __name__ == "__main__":
#    main()