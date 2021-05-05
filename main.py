import requests
from bs4 import BeautifulSoup
import os
import time
import random

def read_url(url : str) -> requests.models.Response :
    '''
    Reads a url with browser user agent and returns the response object.

            Parameters:
                    url (str): the URL

            Returns:
                    response (Response): Response returned
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0'
    }
    response = requests.get(url, headers=headers)
    ## Throws exception if not 200
    response.raise_for_status()
    return response

def check_argos() :
    response = read_url('https://www.argos.co.uk/product/8349000')
    soup = BeautifulSoup(response.text, 'html.parser')
    return 'add-to-trolley-button-button' in [x.get('data-test') for x in soup.find_all('button')]

def check_smyths() :
    try :
        response = read_url('https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259')
    except requests.HTTPError as exception:
        return False
    soup = BeautifulSoup(response.text, 'html.parser')
    #print([x.get('id') for x in soup.find_all('button')])
    return 'addToCartButton' in [x.get('id') for x in soup.find_all('button')]

def check_ao() :
    try :
        response = read_url('https://ao.com/product/p5hehwsny39500-sony-playstation-playstation-5-console-white-79528-291.aspx')
    except requests.HTTPError as exception:
        return False
    soup = BeautifulSoup(response.text, 'html.parser')
    #print([x.get('id') for x in soup.find_all('button')])
    return 'addToCartButton' in [x.get('id') for x in soup.find_all('button')]

def check_amazon() :
    try :
        response = read_url('https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=playstation+5&qid=1620222188&s=gift-cards&sr=1-1-catcorr')
    except requests.HTTPError as exception:
        return False
    soup = BeautifulSoup(response.text, 'html.parser')
    #print([x.get('id') for x in soup.find_all('button')])
    return 'add-to-cart-button' in [x.get('id') for x in soup.find_all('input')]

def check_asda() :
    try :
        response = read_url('https://direct.asda.com/george/toys-character/gaming/gaming-consoles/playstation5-console/050887006,default,pd.html?pid=837293&awc=3_1620222288_67e6396e80c1a59eb5782118cd9db878')
    except requests.HTTPError as exception:
        return False
    soup = BeautifulSoup(response.text, 'html.parser')
    return 'button-addtobag-pdp' in [x.get('data-id') for x in soup.find_all('button')]

def alert_found(name : str) :
    command = f'say "PlayStation Alert at {name}"'
    os.system(command)

if __name__ == '__main__' :
    while True :
        print("Checking...")
        if check_argos() :
            while True :
                print("FOUND ARGOS!")
                alert_found("Argos")
                time.sleep(2)
        if check_smyths() :
            while True :
                print("FOUND SMYTHS!")
                alert_found("Smyths")
                time.sleep(2)
        if check_ao() :
            while True :
                print("FOUND AO!")
                alert_found("A O")
                time.sleep(2)
        if check_amazon() :
            while True :
                print("FOUND AMAZON!")
                alert_found("AMAZON")
                time.sleep(2)
        if check_asda() :
            while True :
                print("FOUND ASDA!")
                alert_found("ASDA")
                time.sleep(2)
        # Wait to check again
        time.sleep(random.randint(5,20))
