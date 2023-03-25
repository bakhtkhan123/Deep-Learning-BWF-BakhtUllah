# Exercise 8.12
def sandwich(*items):
    for i in items:
        print(i)
sandwich('chicken','egg','seafood','grilled')
sandwich('grilled chees','hum','roast','beef','nutella')

# Exercise 8.13
def user_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']= last
    for key, value in user_info.items():
        profile[key]=value
    return profile
detail=user_profile('bakht','maseed',location='waziristan',age='23',field='cs') 
print(detail)

# Exercise 8.14
def car_detail(manifacturer,model_name,**car_info):
    car={}
    car['manfacturer']=manifacturer
    car['model']=model_name
    for key, value in car_info.items():
        car[key]=value
    return car
details=car_detail('subaru', 'outback', color='blue', tow_package=True)
print(details)