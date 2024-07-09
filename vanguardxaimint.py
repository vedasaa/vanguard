# import random
"""
    vedpratama x SGBTEAM
    vedasaa
"""
import requests
import json
import os
import time
import re
import html
import socket
import struct
# import tweepy

def mints(wallet, tokenid):
    url = 'https://vanguard-queue-backend.xai.games/mints'

    headers_dict = {
        'Accept': '*/*',
        'Sec-Ch-Ua': '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.179 Mobile Safari/537.36',
        'Sec-Ch-Ua-platform': 'Android',
        'Origin': 'https://vanguard.xai.games',
        'Referer': 'https://vanguard.xai.games/',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Priority': 'u=1, i'
    }
    
    response = requests.post(url, headers=headers_dict, json={"walletAddress":wallet,"tokenId":tokenid})
    return response

def checkqueue(wallet):
    url = 'https://vanguard-queue-backend.xai.games/is-queued?walletAddress="'+ wallet +'"'
    headers_dict = {
        'Accept': '*/*',
        'Sec-Ch-Ua': '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.179 Mobile Safari/537.36',
        'Sec-Ch-Ua-platform': 'Android',
        'Origin': 'https://vanguard.xai.games',
        'Referer': 'https://vanguard.xai.games/',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Priority': 'u=1, i'
    }
    response = requests.get(url, headers=headers_dict)
    return response

wallet = input("Masukan Wallet: ")
tokenid = 0
while True:
    while tokenid !=41:
        resultmints = mints(wallet, tokenid)
        print(resultmints.status_code)
        os.system('clear')
        while resultmints.status_code != 200:
            resultmints = mints(wallet, tokenid)
        print(str(resultmints.status_code) + resultmints.reason)
        resultcheckqueue = checkqueue(wallet)
        while resultcheckqueue.status_code != 200:
            resultcheckqueue = checkqueue(wallet)
        print(resultcheckqueue.text)
        tokenid+=1
        time.sleep(3)
    tokenid = 0
    print("Token ID Query Check: " + str(tokenid))
    time.sleep(86400)
