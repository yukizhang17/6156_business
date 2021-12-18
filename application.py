import flask
from flask import *
from application_services.business_service import *
from application_services.address_service import *
from application_services.product_service import *
import json

app = Flask(__name__)
application = app


@app.route('/')
def index_page():
    # return render_template("index.html")
    return "This is business homepage"

# newsId = shortuuid.uuid(url)

@app.route('/business', methods=['GET', 'POST'])
def business():
    if flask.request.method == 'POST':
        # User form['user'] for data insertion -> None
        insert_business(request.json)
        return "You are all set"
        # create a new user record
            # 1. check if it exists
            #   select * where email = email
            # 2. if no insert_user()
            #uuid.uuid4() = 32 bits str
        
    elif flask.request.method == 'GET':
        # get_all_user_info() -> JSON()
        return json.dumps(get_all_business())


@app.route('/business/<businessID>', methods=['GET', 'POST', 'DELETE'])
def business_id(businessID):
    print(businessID)
    if flask.request.method == 'GET':
        return json.dumps(get_business_by_id(businessID))
        # return render_template("business_id.html", businessID=businessID, jsonfile=json.dumps(get_business_by_id(businessID)))
        # get_user_info(userID) - userID get from url -> JSON
        #return json.dumps(get_user_by_id(userID))

    elif flask.request.method == 'POST':
        if "delete" in flask.request.json:
            # delete_user_info(userID) - userID get from url
            delete_business(businessID)
            return "User is already deleted."
        # print(request.json)
        # update_user_info(userID) - userID get from url - request.json['user'] input form
        update_business(businessID, request.json)
        return "You are all set."
        # extract items from data about user's info name, email, etc.



@app.route('/business/<businessID>/address', methods=['GET', 'POST'])
def business_id_address(businessID):
    if flask.request.method == 'POST':
        try:
            create_address_by_bid(businessID, request.json)
            return "Address added successfully for business!"
        except Exception as e1:
            return "Failed to add address for business!"
        # Insert a new address
        # associate aid with uid -> get from selecting or email
        # Insert new record to user_address

    elif flask.request.method == 'GET':
        return json.dumps(get_address_by_bid(businessID))
        # return render_template("business_id_address.html", businessID=businessID, jsonfile=json.dumps(get_address_by_bid(businessID)))


        # join user with user_address and return
    # elif flask.request.method == 'PUT':
        # 1. get aid
        # 2. delete <uid, aid> in user_address
        # 3. create a new address with request.json['address']
        # 4. insert to address table
        # 5. insert <uid, new aid> to user_address table

@app.route('/address', methods=['GET', 'POST'])
def address():
    if flask.request.method == 'POST':
        insert_address(request.json)
        return "You are all set"
        # check duplicate
        # insert a new address

    elif flask.request.method == 'GET':
        # print(get_all_address())
        return json.dumps(get_all_address())


@app.route('/address/<addressID>', methods=['GET', 'POST', 'DELETE'])
def address_id(addressID):
    if flask.request.method == 'GET':
        return json.dumps(get_address_by_aid(addressID))
        # return render_template("address_id.html", addressID=addressID, jsonfile=json.dumps(get_address_by_aid(addressID)))

    elif flask.request.method == 'POST':
        if "delete" in flask.request.json:
            # delete_user_info(userID) - userID get from url
            delete_address(addressID)
            return "Address is already deleted."
        update_address(addressID, request.json)
        return "Address has been updated."

@app.route('/product', methods=['GET', 'POST'])
def product():
    keywords = flask.request.args.get('name')
    if flask.request.method == 'POST':
        insert_product(request.json)
        return "YOU are all set"
    elif flask.request.method == 'GET' and keywords == None:
        return json.dumps(get_all_product())
    else:
        products = search_product_by_name(keywords)
        return json.dumps(products)

@app.route('/product/<productID>', methods=['GET', 'POST', 'DELETE'])
def product_id(productID):
    if flask.request.method == 'GET':
        return json.dumps(get_product_by_pid(productID))

    elif flask.request.method == 'POST':
        if "delete" in flask.request.json:
            # delete_user_info(userID) - userID get from url
            delete_product(productID)
            return "Product is already deleted."
        update_product(productID, request.json)
        return "Product has been updated."

@app.route('/business/<businessID>/product', methods=['GET', 'POST'])
def business_id_product(businessID):
    if flask.request.method == 'POST':
        try:
            create_product_by_bid(businessID, request.json)
            return "product added successfully for business!"
        except Exception as e1:
            return "Failed to add product for business!"
        # Insert a new address
        # associate aid with uid -> get from selecting or email
        # Insert new record to user_address

    elif flask.request.method == 'GET':
        form = flask.request.json
        offset = None
        limit = None

        for element in form:
            if element == "limit":
                limit = form[element]
            elif element == "offset":
                offset = form[element]
        return json.dumps(get_product_by_bid(businessID, limit, offset), default=str), 200

@app.route('/product/<productID>/business', methods=['GET'])
def product_id_business(productID):
    if flask.request.method == 'GET':
        form = flask.request.json
        offset = None
        limit = None

        for element in form:
            if element == "limit":
                limit = form[element]
            elif element == "offset":
                offset = form[element]
        return json.dumps(get_business_by_pid(productID, limit, offset), default=str), 200

# @app.route('/business/<businessID>/address', methods=['GET', 'POST'])
# def business_id_address(businessID):
#     if flask.request.method == 'POST':
#         try:
#             create_address_by_bid(businessID, request.json)
#             return "Address added successfully for business!"
#         except Exception as e1:
#             return "Failed to add address for business!"
#         # Insert a new address
#         # associate aid with uid -> get from selecting or email
#         # Insert new record to user_address
#
#     elif flask.request.method == 'GET':
#         form = flask.request.json
#         offset = None
#         limit = None
#
#         for element in form:
#             if element == "limit":
#                 limit = form[element]
#             elif element == "offset":
#                 offset = form[element]
#         return json.dumps(get_address_by_bid(businessID), default=str), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


