'''
Author: ruofei
Date: 2021-03-01 16:15:58
LastEditTime: 2021-03-01 18:40:18
LastEditors: Please set LastEditors
Description: Using flask server as a mugglepay callback server example
FilePath: /mugglepay-python-sdk/example_callback_server.py
'''

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/mugglepay_callback_api', methods=['POST'])
def muggle_call_back():
    callback_info = request.json
    print('order_id: MugglePay order ID\n{}\n==========='.format(callback_info['order_id']))
    print('merchant_order_id: Order ID of the merchant. Should be used to identify order or invoice.\n\
        {}==========='.format(callback_info['merchant_order_id']))
    print('status: MugglePay payment status.\n\
        {}==========='.format(callback_info['status']))
    print('price_amount: The price set by the merchant; Example: 9.99\n\
        {}\n==========='.format(callback_info['price_amount']))
    print('price_currency: Currency in which the merchant\'s goods/services are priced; Example: USD\n\
        {}\n==========='.format(callback_info['price_currency']))
    print('created_at: Invoice creation time; Example: \'2019-04-24T17:23:54.311Z\'\n\
        {}\n==========='.format(callback_info['created_at']))
    print('created_at_t: Your token provided by CreateOrder to validate Payment Callback\n\
        {}\n==========='.format(callback_info['created_at_t']))
    # token field is generated by merchant. you can compare your own token with this token field to make sure you get callback from real mugglepay service. 
    # The token validation try to avoid fake callback request from others.
    print('token: Your token provided by CreateOrder api to validate Payment Callback.\n\
        {}\n==========='.format(callback_info['token']))
    print('meta: Option: provide third party information. e.g. Alipay or WechatPay. An example of Alipay is provided as example.\n\
        {}\n==========='.format(callback_info['meta']))
    return callback_info

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)