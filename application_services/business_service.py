import uuid
from application_services.base_application_resource import BaseApplicationResource
from application_services.address_service import *
from application_services.product_service import *

db_name = "businesses"
table_name = "business"
address_table_name = "address"
business_address_table_name = "business_address"
product_table_name = "product"
business_product_table_name = "business_product"

def get_all_business():
    return BaseApplicationResource.get_by_template(db_name, table_name, None)

def get_business_by_id(business_id):
    template = {"bid": business_id}
    return BaseApplicationResource.get_by_template(db_name, table_name, template)

def insert_business(create_data):
    # ﬁprint(create_data['email'])
    email = create_data["email"]
    res = BaseApplicationResource.get_by_template(db_name, table_name, {"email": email})
    if res is not None:
        bid = uuid.uuid4().hex
        template = {"bid": bid}
        for item in create_data:
            template[item] = create_data[item]
        BaseApplicationResource.create(db_name, table_name, template)

def update_business(business_id, update_data):
    data = {}
    for item in update_data:
        if update_data[item] != "":
            data[item] = update_data[item]
    # print(data)
    template = {"bid": business_id}
    BaseApplicationResource.update(db_name, table_name, data, template)

def delete_business(business_id):
    template = {"bid": business_id}
    BaseApplicationResource.delete(db_name, table_name, template)

def get_address_by_bid(business_id):
    template = {"bid": business_id}
    addr_list = BaseApplicationResource.get_by_template(db_name, business_address_table_name, template)
    aids = []
    for addr in addr_list:
        aids.append(addr['baid'])
    print("baids: ", aids)
    if len(aids) > 0:
        addresses = BaseApplicationResource.find_in_condition(db_name, address_table_name, None, "baid", aids)
    else:
        addresses = {}
    return addresses

def create_address_by_bid(business_id, create_data):
    # check if address exists?
    baid = insert_address(create_data)
    template = {"bid": business_id, "baid": baid}
    BaseApplicationResource.create(db_name, business_address_table_name, template)

def get_product_by_bid(business_id, limit, offset):
    template = {"bid": business_id}
    prod_list = BaseApplicationResource.get_by_template(db_name, business_product_table_name, template, limit, offset)
    pids = []
    for prod in prod_list:
        pids.append(prod['pid'])
    print("pids: ", pids)
    if len(pids) > 0:
        products = BaseApplicationResource.find_in_condition(db_name, product_table_name, None, "pid", pids)
    else:
        products = {}
    return products

def create_product_by_bid(business_id, create_data):
    # check if address exists?
    pid = insert_product(create_data)
    template = {"bid": business_id, "pid": pid}
    BaseApplicationResource.create(db_name, business_product_table_name, template)
