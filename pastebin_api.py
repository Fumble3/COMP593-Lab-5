import requests

DEVELOPER_KEY = 'n0cHxVcSnbEHap8DVH4rCSmCdn3be1tc'
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
    url = post_new_paste("This is the title", "This \nis \nthe body", '1H', True)
    print(f'New paste URL: {url}')

def post_new_paste(title, body_text, expiration='10M', listed=False):
    """Posts a new public paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): _description_. Defaults to '10M'.
        listed (bool, optional): _description_. Defaults to False.

    Returns:
        str: URL of the new paste, if successful. Otherwise it returns none
    """
    #Setup the parameters for the request message
    paste_params = {
        'api_dev_key': DEVELOPER_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date:': expiration,
        'api_paste_private': 0 if listed else 1

    }

    #Send POST request to the PasteBin API
    print('Sending POST request to PasteBin API...', end='')
    resp_msg = requests.post(PASTEBIN_API_URL, data=paste_params)

    #Check whether the POST request was successful or not
    if resp_msg.ok:
        print('Success!')
        return resp_msg.text
    else:
        print('Failed!')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')

    

if __name__ == '__main__':
    main()