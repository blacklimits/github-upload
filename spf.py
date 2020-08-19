#!/usr/bin/env python3
import pydig
import sys
import re


# host=sys.argv[1] #input hostname
# qtype=sys.argv[2] #input DNS query type
# s=sys.argv[3] #input dkim selector
qtype='txt' 
host='bugdasht.ir'

spf1=pydig.query(host, qtype)
RE=re.findall(r'(v=spf1)(.+?)"', str(spf1), flags=0)
if RE==[]:
    print("\nNo SPF record found for ", host)
else:
    for y in RE:
        print("SPF record for ", host,":", y)
print()




    
# # print(spf1)
#     for y in RE:
#         print("SPF",y)