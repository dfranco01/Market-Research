import requests
import os
from dotenv import load_dotenv
from datetime import date

# SAM.gov API endpoint
SAM_API_URL = "https://api.sam.gov/prod/opportunities/v2/search"

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_sam_opportunities():
    formatted = date.today().strftime("%m/%d/%Y")
    headers = { 'Accept': 'application/json' }
    params = { 'api_key': API_KEY, 'limit':1,
              'postedFrom': '04/01/2026', 'postedTo': formatted, 
              'ptype': ['p', 'o', 'r', 'k'], #'state':['CA', 'TX'],
              'ncode':'561720', 'typeofsetaside':'SBA' 
            }

    #Solicitations only
    response = requests.get(SAM_API_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    opportunities = data.get('opportunitiesData', [])
    
    for opp in opportunities:
        print(f"Solicitation Number: {opp.get("solicitationNumber")}")
        print(f"Title: {opp.get('title')}")
        print(f"Agency: {opp.get('fullParentPathName')}")
        print(f"Posted: {opp.get('postedDate')}")
        print(f"Deadline: {opp.get('responseDeadLine')}")
        print(f"Type: {opp.get('type')}")
        print(f"Place of Performance: {opp.get('placeOfPerformance')}")
        #Contact info is in an array
        contacts = opp.get('pointOfContact', [])
        if contacts:
            print(f"Contact: {contacts[0].get('email', 'N/A')}")
            print("---")
    return opportunities

#get_sam_opportunities()
    
            
