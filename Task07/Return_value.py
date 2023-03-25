# Exercise 8.6
def city_country(city,country):
    info=city.title()+' '+country.title()
    return info
detail=city_country('santiago','chile')
detail_1=city_country('kolkata','India')
detail_2=city_country('london','America')
print(detail,'\n',detail_1,'\n',detail_2)

# Exercise 8.7 &  8
def make_Album(artist_name,album_title,track=''):
    '''Return a dictionary of information about the Album '''
    dict={'name':artist_name,'title':album_title}
    if track:
        dict['track']=track
    return dict
while True:
    print('Enter q at any time to quit')
    a_name=input("artist_name:")
    if a_name=='q':
        break
    a_title=input('album_title:') 
    if a_title=='q':
        break  
    Album=make_Album(a_name,a_title)
    print(Album)  

muscian=make_Album('Atif Aslam','by year')
muscian_1=make_Album('ali zafar','psl songs','audio')
print(muscian)
print(muscian_1)