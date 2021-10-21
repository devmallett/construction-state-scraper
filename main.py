import requests 
from bs4 import BeautifulSoup


# Make a list of each state
#map through that each state
#parse it to the base URL
#run through request protocol


states = ['Alabama'
,'Alaska'
,'Arizona'
,'Arkansas'
,'California'
,'Colorado'
,'Connecticut'
,'Delaware'
,'Florida'
,'Georgia'
,'Hawaii'
,'Idaho'
,'Illinois'
,'Indiana'
,'Iowa'
,'Kansas'
,'Kentucky'
,'Louisiana'
,'Maine'
,'Maryland'
,'Massachusetts'
,'Michigan'
,'Minnesota'
,'Mississippi'
,'Missouri'
,'Montana'
,'Nebraska'
,'Nevada'
,'New Hampshire'
,'New Jersey'
,'New Mexico'
,'New York'
,'North Carolina'
,'North Dakota'
,'Ohio'
,'Oklahoma'
,'Oregon'
,'Pennsylvania'
,'Rhode Island'
,'South Carolina'
,'South Dakota'
,'Tennessee'
,'Texas'
,'Utah'
,'Vermont'
,'Virginia'
,'Washington'
,'West Virginia'
,'Wisconsin' ,'Wyoming']

# print(states)

# def url_maker(states):

for state in states:
    # links= []
    main = f'https://www.zippia.com/company/best-construction-companies-{state}/' 
    # links.append(main)
    state_request = requests.get(main)
    state_pull = BeautifulSoup(state_request.content ,'html5lib')
    state_table = state_pull.findAll('h2' ,attrs = { 'class':'blueOpenSans' })
    for row in state_table:
        print(row.text)




# URL = "https://www.zippia.com/company/best-construction-companies-ohio/"
# r = requests.get(URL) 
# soup = BeautifulSoup(r.content ,'html5lib')
# table = soup.findAll('h1')
# for row in table:
#     print(row.text)

    
    
    # links.insert(main)
    # print(links)
        

    #59
    #TODO get all links into a single list 
        
# return links
    # print(links)
    # for link in links:
        # state_request = requests.get(link)
        # state_pull = BeautifulSoup(state_request.content ,'html5lib')
        # state_table = state_pull.findAll('h2' ,attrs = { 'class':'blueOpenSans' })
        # for row in state_table:
        #     print(row.text)
        

    


# URL = "https://www.zippia.com/company/best-construction-companies-ohio/"
# michigan_companies = 'https://www.zippia.com/company/best-construction-companies-michigan/'
# kentucky_companies = 'https://www.zippia.com/company/best-construction-companies-kentucky/'
# illinois_companies = 'https://www.zippia.com/company/best-construction-companies-illinois/'

# r = requests.get(URL) 
# michigan_requests = requests.get(michigan_companies) 
# kentucky_requests = requests.get(kentucky_companies)
# illinois_requests = requests.get(illinois_companies)

# # print(r.content) 

# soup = BeautifulSoup(r.content ,'html5lib')
# michigan_pull =  BeautifulSoup(michigan_requests.content ,'html5lib')
# kentucky_pull =  BeautifulSoup(kentucky_requests.content ,'html5lib')
# illinois_pull =  BeautifulSoup(illinois_requests.content ,'html5lib')


# # print(soup.prettify())

# michigan_table = michigan_pull.findAll('h2' ,attrs = { 'class':'blueOpenSans' })
# kentucky_table = kentucky_pull.findAll('h2' ,attrs = { 'class':'blueOpenSans' })
# illinois_table = illinois_pull.findAll('h2' ,attrs = { 'class':'blueOpenSans' })
# table = soup.findAll('h1')

# for row in illinois_table:
#     print(row.text)
