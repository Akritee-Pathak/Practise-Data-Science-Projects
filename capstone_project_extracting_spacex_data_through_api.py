

import requests
import pandas as pd
import numpy as np

spacex_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
response = requests.get(spacex_url).json()

df=pd.DataFrame(response)

df

df.info()

"""**Making different functions to fetch the data from APIs**"""

creating_data=pd.DataFrame(columns=[])

def get_rocketname(data):

  rocket_name=[]
  for element in data['rocket']:
    if element!=None:
      rocket_url = f'https://api.spacexdata.com/v4/rockets/{element}'
      response=requests.get(rocket_url).json()
      rocket_name.append(response['name'])

    else:
      rocket_name.append(None)


  creating_data['rocket_name']= rocket_name

get_rocketname(df)

creating_data

def get_launchpad_details(data):
  global creating_data
  launch_site=[]
  longitude=[]
  latitude=[]

  for element in data['launchpad']:
    if element!=None:
      launchpad_url = f'https://api.spacexdata.com/v4/launchpads/{element}'
      response=requests.get(launchpad_url).json()
      launch_site.append(response['name'])
      longitude.append(response['longitude'])
      latitude.append(response['latitude'])

    else:
      launch_site.append(None)
      longitude.append(None)
      latitude.append(None)


  creating_data['launch_site']= launch_site
  creating_data['longitude']= longitude
  creating_data['latitude']= latitude

get_launchpad_details(df)

creating_data

def get_payload_data(data):

  global creating_data
  payload_mass=[]
  orbit=[]

  for element in data['payloads']:
    if element!= None:
      payload_url=f"https://api.spacexdata.com/v4/payloads/{element[0]}"
      response = requests.get(payload_url).json()
      payload_mass.append(response['mass_kg'])
      orbit.append(response['orbit'])

    else:
      payload_mass.append(None)
      orbit.append(None)

  creating_data['payload_mass']= payload_mass
  creating_data['orbit']=orbit

get_payload_data(df)

creating_data

def get_core_data_1(data):

  global creating_data

  outcome=[]
  flight=[]
  gridfins=[]
  reused=[]
  legs=[]
  landing_pad=[]

  for element in data['cores']:
    outcome.append( str(element[0]['landing_success']) + ' ' + str(element[0]['landing_type']))
    flight.append(element[0]['flight'])
    gridfins.append(element[0]['gridfins'])
    reused.append(element[0]['reused'])
    legs.append(element[0]['legs'])
    landing_pad.append(element[0]['landpad'])

  creating_data['outcome']=outcome
  creating_data['flight']= flight
  creating_data['gridfins']=gridfins
  creating_data['reused']=reused
  creating_data['legs']=legs
  creating_data['landing_pad']=landing_pad

get_core_data_1(df)

creating_data

def get_cores_data_2(data):
 global creating_data
 block=[]
 reuse_count=[]
 serial=[] # engine name

 for element in data['cores']:
  if element[0]['core']!= None:
    core_url=f"https://api.spacexdata.com/v4/cores/{element[0]['core']}"
    response= requests.get(core_url).json()
    block.append(response['block'])
    reuse_count.append(response['reuse_count'])
    serial.append(response['serial'])

  else:
    block.append(None)
    reuse_count.append(None)
    serial.append(None)


 creating_data['block']=block
 creating_data['reuse_count']=reuse_count
 creating_data['serial']=serial

get_cores_data_2(df)

creating_data

"""**After collecting all the data, we will create new data set only containing information about Falcon 9**"""

data_falcon9= creating_data[creating_data['rocket_name']=='Falcon 9']

data_falcon9
