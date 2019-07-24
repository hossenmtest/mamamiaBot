import requests
get_response = requests.get(url='https://api.telegram.org/bot853024173:AAFhW3lWxL1hfECScSHK6LO8Il-MK6vlQ58/getUpdates')
post_data = {'username':'joeb', 'password':'foobar'}
# POST some form-encoded data:
post_response = requests.post(url='http://httpbin.org/post', data=post_data)
