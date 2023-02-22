import requests

DAD_JOKES_API_URL = 'https://icanhazdadjoke.com/'
DAD_JOKES_SEARCH_URL = f'https://icanhazdadjoke.com/search'



def main():
    jokes_list = search_for_dad_jokes('cow')
    print(*jokes_list, sep='\n')
    
    return

def search_for_dad_jokes(search_term):
    """Gets a list of dad jokes that contains a search term

    Args:
        search_term (str): Search Term

    Returns:
        list: List of jokes containing the search term
    """
    
    
    #Setup the header parameters
    header_params = {
        'Accept': 'application/json',


    }
    
    #Setup the Query string parameters
    query_str_params = {
    'term': search_term
    }

      #Send GET request to the DadJokes API
    print('Searching Dad jokes API for "{search_term}".', end='')
    resp_msg = requests.get(DAD_JOKES_API_URL, headers=header_params, params=query_str_params)

    #Check whether the GET request was successful or not
    if resp_msg.ok:
        print('Success!')
        body_dict = resp_msg.json()
        jokes_portion = body_dict['results']
        jokes_list = [j['joke'] for j in jokes_portion]
        return jokes_list
                      
    
    else:
        print('Failed!')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')

    return




def get_random_dad_joke():
    """Gets a random dad joke

    Returns:
        str: Dad joke
    """


    #Setup the header parameters
    header_params = {
        'Accept': 'application/json',


    }
    
      #Send GET request to the DadJokes API
    print('Sending GET request to DadJokes API...', end='')
    resp_msg = requests.get(DAD_JOKES_API_URL, headers=header_params)

    #Check whether the GET request was successful or not
    if resp_msg.ok:
        print('Success!')
        joke_dict = resp_msg.json()
        return joke_dict['joke']
    
    else:
        print('Failed!')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')

    return




if __name__ == '__main__':
    main()