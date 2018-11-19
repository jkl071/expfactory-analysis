"""
expanalysis.api: functions for retrieving experiment factory results

"""
import pandas as pd
import os
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
   
access_token = "" # expfactory.org/token
results = get_results(access_token=access_token)
   
#This snippet creates a folder called expfactory_online_data in your /Users/elliott/Desktop directory.  
#If you don't like the path where the folder is created, change the file path variable to your desired location
file_path = "~/Desktop/expfactory_online_data"
if not os.path.exists(file_path):
    os.makedirs(file_path)

#Line 69 returns each sub as a csv file, inside the directory, /Desktop/expfactory_online_data
#change the directory given in order to match up with yours.
all_subs_df = []
for i in range(0, len(results)):
    if results[i]['completed'] == True:
        single_sub_df = pd.DataFrame(results[i]['data'][0]['trialdata'])
        single_sub_df.to_csv('~/Desktop/expfactory_online_data/all_subs_df_'+str(i)+'.csv',sep=',')
        
