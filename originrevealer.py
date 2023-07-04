import requests
import mmh3
import codecs
import argparse
from tld import get_tld
import configparser

CONFIG_FILE = 'config.ini'


def banner():
    print("""
     OriginRevealer                    
     Powered By CriminalIP : https://www.criminalip.io/
    """)



def parse_arguments():
    parser = argparse.ArgumentParser(description="Tool for extracting possible Origin IPs given a favicon url")
    parser.add_argument('--init', metavar='API_KEY', help='Initialize and store the API key')
    parser.add_argument("-t", "--target", help="Favicon target url", type=str)
    return parser.parse_args()


def initialize_api_key(api_key):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'API_KEY': api_key}

    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

    print("CriminalIP API key initialized and stored.")

def get_api_key():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    if 'DEFAULT' in config and 'API_KEY' in config['DEFAULT']:
        return config['DEFAULT']['API_KEY']

    return None


# this function will calculate favicon hash value 
def calculate_hash(url):
    response = requests.get(url)

    favicon = codecs.encode(response.content,"base64")
    hash = mmh3.hash(favicon)
    hex_val=hex(hash)
    if hex_val.startswith('-'):
        return "-"+hex_val[3:]
    else:
        return hex_val[2:]

# this function will extract IPs based on favicon hash
def retrieve_ip_fh(faviconhash,offset=0):
    url = "https://api.criminalip.io/v1/banner/search"
    headers = {
        "x-api-key": api_key
    }

    params = {
        "query": f"favicon:{faviconhash}",
        "offset": offset
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]["result"]
    ip_addresses = sorted(set(item["ip_address"] for item in data))

    for ip_address in ip_addresses:
        print(ip_address)


# this function will retrieve IPs based on tld
def retrieve_ip(url,offset=0):
    domain=get_tld(url,as_object=True).fld

    url = "https://api.criminalip.io/v1/banner/search"
    headers = {
        "x-api-key": api_key
    }

    params = {
        "query": f"ssl_subject_common_name:{domain}",
        "offset": offset
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]["result"]
    ip_addresses = sorted(set(item["ip_address"] for item in data))

    for ip_address in ip_addresses:
        print(ip_address)




if __name__ == '__main__':
    banner()

    args = parse_arguments()


    # initialize your api key
    if args.init:
        initialize_api_key(args.init)

    try:
        if args.target:
            if get_api_key() is None or not get_api_key().strip():
                print("please initialise your API key")
            else:
                api_key=get_api_key()
            
                # retrieving IPs using favicon hash trick
                retrieve_ip_fh(calculate_hash(args.target))
                # retrieve IPs using the domain name
                retrieve_ip(args.target)
    except KeyError:
        print("Error: Wrong api key or insufficient credit")
