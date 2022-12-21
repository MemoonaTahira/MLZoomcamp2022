import requests

user_id = 'abc_012'
# credit_user = {"reports": 0, "share": 0.001694,"expenditure": 0.12, "owner": "yes"}
credit_user = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

# Runs on all 4!
url = 'http://0.0.0.0:9696/predict'
# url = 'http://localhost:9696/predict'
# url = 'http://127.0.0.1:9696/predict'
# url = 'http://172.30.58.76:9696/predict'


# General format: requests.post(url, json= credit_user)
response = requests.post(url, json= credit_user).json()

# For autoscaling:
# while True:
#     sleep(0.1)
#     response = requests.post(url, json=client).json()
#     print(response)

print(response)

# if response['credit_card_prob'] == True:
#    print('sending promo email to to this customer to get a credit card %s' % user_id)
# else:
#    print('not sending promo email for credit card to %s' % user_id)

