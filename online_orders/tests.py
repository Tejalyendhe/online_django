# # from django.test import TestCase
# import requests,
# path('test_api/', views.test_api, name='test_api'),

# def test_api(request):

#     with open('test.jpg', mode='rb') as file: img = file.read()
#     with open('test-1.jpg', mode='rb') as file: img_1 = file.read()
#     with open('test-2.jpg', mode='rb') as file: img_2 = file.read()
#     with open('test-3.jpg', mode='rb') as file: img_3 = file.read()
#     data = {
#         'user':'sarvesh'
#         'product':[{
#         'unique_no':'11AA1197',
#         'product':'SAREE',
#         'product_type':'SAREE',
#         'price':100.0,
#         'quantity':100.0,
#         'primaryImage': base64.b64encode(img).decode("utf-8"),
#         'secondaryImage': '',
#         },
#         ]
        
#     }  
#     LOGIN_URL = 'http://localhost:5000/add_product/'
#             # LOGIN_URL = 'http://localhost:7000/add_dispatch_data'
#     resp = requests.post(LOGIN_URL, data= json.dumps(data))
#     return HttpResponse(f'''{resp.content}''')