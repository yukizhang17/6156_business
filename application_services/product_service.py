'''
Function to deal with address table by using SQL commands
'''

from application_services.base_application_resource import BaseApplicationResource
import json
import uuid

'''
Global field
'''
DB = "business"
PRODUCT_TABLE = "product"
BUSINESS_PRODUCT_TABLE = 'business_product'


def insert_product(data):
    '''
    Function to insert a new product entry to product table
    '''
    try:
        print(data)
        template = data
        product = BaseApplicationResource.get_by_template(DB, PRODUCT_TABLE, template)
        if product:
            return product[0]["aid"]
        else:
            pid = uuid.uuid4().hex
            template = {'pid': pid}
            template.update(data)
            res = BaseApplicationResource.create(DB, PRODUCT_TABLE, template)
            print(res)
            return pid
    except:
        print("ops, product insert failed")


def get_all_product():
    '''
    Function to query all product data entries from product table
    '''
    try:
        res = BaseApplicationResource.get_by_template(DB, PRODUCT_TABLE, None)
    except:
        print("Ops, query of all product failed")
    return res


def get_product_by_pid(pid):
    '''
    Function to query a sepcific address by its pid
    '''
    try:
        template = {"pid": pid}
        return BaseApplicationResource.get_by_template(DB, PRODUCT_TABLE, template)
    except:
        print("ops, the product not found")


def update_product(pid, data):
    '''
    Function to update an product
    '''
    try:
        template = {'pid': pid}
        update_data = {}
        for item in data:
            if data[item] != "":
                update_data[item] = data[item]
        return BaseApplicationResource.update(DB, PRODUCT_TABLE, update_data, template)
    except:
        print ("ops, update product failed")


def delete_product(pid):
    '''
    Function to delete an product record in product table by its pid
    '''
    try:
        template = {'pid':pid}
        print(delete_product_business(pid))
        return BaseApplicationResource.delete(DB, PRODUCT_TABLE, template)
    except:
        print("ops, delete rocord in product table failed")


def delete_product_business(pid):
    '''
    Helper function to delete records in product_business table when action of
    delete product or business happens.
    '''
    try:
        template = {'pid':pid}
        return BaseApplicationResource.delete(DB, BUSINESS_PRODUCT_TABLE, template)
    except:
        print("ops, cannot delete record in business_product table")







