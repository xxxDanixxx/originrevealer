# OriginRevealer

originrevealer is a Tool for extracting possible Origin IPs given a favicon url

## Installation And Setup

1. Clone the project :
```
git clone https://github.com/xxxDanixxx/originrevealer
```

2. Prepare and activate the virtual environment :
```
$ python3 -m venv myenv
$ source myenv/bin/activate
```

3. Install requirements :
```
(myenv) $ pip install -r requirements.txt
```

## Usage

```

usage: originrevealer.py [-h] [--init API_KEY] [-t TARGET]

Tool for extracting possible Origin IPs given a favicon url

optional arguments:
  -h, --help            show this help message and exit
  --init API_KEY        Initialize and store the API key
  -t TARGET, --target TARGET
                        Favicon target url
```

### API KEY
To make use of the tool, you will need to acquire an API key from CriminalIP. Once you have obtained the key, you can authenticate and access the CriminalIP API seamlessly.

```
python3 originrevealer.py --init a123b123

CriminalIP API key initialized and stored.
```
### Get Origin IPs :
```
$ python3 originrevealer.py -t https://www.facebook.com/favicon.ico

157.240.212.35
....
```



### Notes

- Exercise caution when using the tool, as it may retrieve assets that do not belong to the target or false positive .

- To ensure proper functionality of the tool, it relies on CriminalIP. If you encounter any errors during execution, it may indicate that you have exceeded the query limit associated with your API key. visit the [CriminalIP](https://www.criminalip.io/en/pricing) website for more informations
