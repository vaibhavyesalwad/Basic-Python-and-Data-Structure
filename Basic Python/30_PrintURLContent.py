"""Program to access and print a URL's content to the console"""
import http.client                                             # using http.client module
conn = http.client.HTTPConnection('bridgelabz.com')               # establish connection with URL
conn.request('GET', '/')                             # request for content
result = conn.getresponse()                            # fetch content
print(result.read().decode())              # printing fetched content
conn.close()

'''
print(result.response) # shows response code
print(result.reason) # description of response
'''