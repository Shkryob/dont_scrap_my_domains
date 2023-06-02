# Don't Scrap My Domains!

An util that gets info about domains from public resources
and extracts personal info (phone, emails, addresses)
with help of ChatGPT and oldscool Python libs

## Usage

Get ChatGPT key from https://platform.openai.com/account/api-keys

Set ChatGPT API key:

```commandline
 export OPENAI_API_KEY='<YOUR_CHAT_GPT_API_KEY>'
```

Download a domain targets list from https://hackerone.com/opportunities/all as a CSV file.

Install dependencies:

```commandline
pip install -r requirements.txt
```

Run Don't Scrap My Domains tool:

```commandline
python main.py <YOUR_CSV_FROM_HACKERONE>
```

Checkout extracted data in the report folder.
