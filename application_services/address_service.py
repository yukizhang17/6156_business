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
ADDRESS_TABLE = "address"
BUSINESS_ADDRESS_TABLE = 'business_address'



def insert_address(data):
    '''
    Function to insert a new address entry to adress table
    '''
    try:
        print('data is', data)
        template = data
        address = BaseApplicationResource.get_by_template(DB, ADDRESS_TABLE, template)
        print(address)
        if address:
            return address[0]["baid"]
        else:
            baid = uuid.uuid4().hex
            template = {'baid': baid}
            template.update(data)
            res = BaseApplicationResource.create(DB, ADDRESS_TABLE, template)
            print(res)
            return baid
    except:
        print("ops, address insert failed")


def get_all_address():
    '''
    Function to query all address data entries form address table
    '''
    try:
        res = BaseApplicationResource.get_by_template(DB, ADDRESS_TABLE, None)
    except:
        print("Ops, query of all adresses failed")
    return res


def get_address_by_aid(aid):
    '''
    Function to query a sepcific address by its aid
    '''
    try:
        template = {"baid": baid}
        return BaseApplicationResource.get_by_template(DB, ADDRESS_TABLE, template)
    except:
        print("ops, the address not found")


def update_address(baid, data):
    '''
    Function to update an address
    '''
    try:
        template = {'baid': baid}
        update_data = {}
        for item in data:
            if data[item] != "":
                update_data[item] = data[item]
        return BaseApplicationResource.update(DB, ADDRESS_TABLE, update_data, template)
    except:
        print ("ops, update addres failed")


def delete_address(baid):
    '''
    Function to delete an address record in address table by its aid
    '''
    try:
        template = {'baid':baid}
        print(delete_address_business(baid))
        return BaseApplicationResource.delete(DB, ADDRESS_TABLE, template)
    except:
        print("ops, delete rocord in address table failed")


def delete_address_business(baid):
    '''
    Helper function to delete records in business_address table when action of
    delete business or address happens.
    '''
    try:
        template = {'baid':baid}
        return BaseApplicationResource.delete(DB, BUSINESS_ADDRESS_TABLE, template)
    except:
        print("ops, cannot delete record in business_address table")







