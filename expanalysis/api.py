"""
expanalysis.api: functions for retrieving experiment factory results

"""

from expanalysis.utils import get_pages

def findWorker(arg):
    found = 0
    for i in range(0, len(results)):
        if results[i]['worker']['id'] == arg:
            print("found worker, please look at index: " + str(i) )
            found = found + 1
    if found == 0:
        print("No worker by that ID")
        
        
        
def get_results(url=None,access_token=None):
    '''get_results is a wrapper for get_url, to first check that the user has provided an access token
    :param url: the expfactory/results/api url
    :param access_token: a token obtained at expfactory.org/token when the user is logged in
    '''
    if url == None:
        url = "http://expfactory.org/new_api/results/81/"
    if access_token != None:
        return get_pages(url=url,access_token=access_token)
    else:
        print("You must provide an access_token to authenticate to the API.")
   
access_token = "5163be7d0a6a347ebce46dac018547a6846ed47c" # expfactory.org/token
results = get_results(access_token=access_token)
   
