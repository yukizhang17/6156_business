import flask
from flask import *
from application_services.business_service import *
from application_services.address_service import *
from application_services.product_service import *
import json

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template("index.html")

# newsId = shortuuid.uuid(url)


@app.route('/business', methods=['GET', 'POST'])
def business():
    if flask.request.method == 'POST':
        # User form['user'] for data insertion -> None
        insert_business(request.form)
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
        return render_template("business_id.html", businessID=businessID, jsonfile=json.dumps(get_business_by_id(businessID)))
        # get_user_info(userID) - userID get from url -> JSON
        #return json.dumps(get_user_by_id(userID))

    elif flask.request.method == 'POST':
        if "delete" in flask.request.form:
            # delete_user_info(userID) - userID get from url
            delete_business(businessID)
            return "User is already deleted."
        # print(request.form)
        # update_user_info(userID) - userID get from url - request.form['user'] input form
        update_business(businessID, request.form)
        return "You are all set."
        # extract items from data about user's info name, email, etc.



@app.route('/business/<businessID>/address', methods=['GET', 'POST'])
def business_id_address(businessID):
    if flask.request.method == 'POST':
        try:
            create_address_by_bid(businessID, request.form)
            return "Address added successfully for business!"
        except Exception as e1:
            return "Failed to add address for business!"
        # Insert a new address
        # associate aid with uid -> get from selecting or email
        # Insert new record to user_address

    elif flask.request.method == 'GET':
        # return json.dumps(get_address_by_uid(userID))
        return render_template("business_id_address.html", businessID=businessID, jsonfile=json.dumps(get_address_by_bid(businessID)))


        # join user with user_address and return
    # elif flask.request.method == 'PUT':
        # 1. get aid
        # 2. delete <uid, aid> in user_address
        # 3. create a new address with request.form['address']
        # 4. insert to address table
        # 5. insert <uid, new aid> to user_address table

@app.route('/address', methods=['GET', 'POST'])
def address():
    if flask.request.method == 'POST':
        insert_address(request.form)
        return "You are all set"
        # check duplicate
        # insert a new address

    elif flask.request.method == 'GET':
        # print(get_all_address())
        return json.dumps(get_all_address())


@app.route('/address/<addressID>', methods=['GET', 'POST', 'DELETE'])
def address_id(addressID):
    if flask.request.method == 'GET':
        return render_template("address_id.html", addressID=addressID, jsonfile=json.dumps(get_address_by_aid(addressID)))

    elif flask.request.method == 'POST':
        if "delete" in flask.request.form:
            # delete_user_info(userID) - userID get from url
            delete_address(addressID)
            return "Address is already deleted."
        update_address(addressID, request.form)
        return "Address has been updated."




if __name__ == '__main__':
    app.run()
