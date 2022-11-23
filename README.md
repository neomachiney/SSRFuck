# SSRFuck
## Description
- :warning: Before diving into my tools, read this: [NUKED](https://github.com/machineydv/machineydv/blob/master/NUKED.md)

Inspiried by `jsfuck` and `brainfuck`, two words which have no relation with my tool. Test for SSRF against a list of URLs

## Features
1. Threaded testing of SSRF against a list of URLs (hakrawler,gau).

## Usage
```
usage: SSRFucker [-h] [-w WORDLIST] [-d DOMAIN] [-s SERVER] [-t THREADS] [-b]

Simple tool for SSRF

optional arguments:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Absolute path to wordlist
  -d DOMAIN, --domain DOMAIN
                        Domain name
  -s SERVER, --server SERVER
                        Server name
  -t THREADS, --threads THREADS
                        Number of threads
  -b, --banner          Print banner and exit

Check your server logs
```

## Example
General SSRF 
* ```SSRFuck -w path/to/file.txt -oD `pwd` -t 1 -d domainname.txt -s SERVERNAME```  
where servername = your bxssrf+ngrok, burpcollaborator etc

## Caveats
1. None i guess.
