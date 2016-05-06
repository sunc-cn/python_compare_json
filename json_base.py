#!/usr/bin/python2.6
#encoding=utf-8




import json

def TypeIsEqual(lhs,rhs):
    if type(lhs) != type(rhs):
        return False
    return True

def ValueIsEqual(lhs,rhs):
    if not TypeIsEqual(lhs,rhs):
        return (False,"type dismatch")
    if lhs != rhs:
        return (False,"value not equal")
    return (True,"equal")

def SliceIsEqual(lhs,rhs):
    if not TypeIsEqual(lhs,rhs):
        return (False,"type dismatch")
    lhs_sorted = sorted(lhs)
    rhs_sorted = sorted(rhs)
    if lhs_sorted != rhs_sorted:
        return (False,"value not equal")
    return (True,"equal")

def DictIsEqual(lhs,rhs):
    if not TypeIsEqual(lhs,rhs):
        return (False,"type dismatch")
    lhs_sorted = sorted(lhs)
    rhs_sorted = sorted(rhs)
    if lhs_sorted != rhs_sorted:
        return (False,"value not equal")
    return (True,"equal")


def ParseJson(json_str):
    try:
        return json.loads(json_str)
    except Exception as e:
        print("ParseJson has Exception:",str(e))
        return {}

def CompareDict(expect_json_dict,actual_json_dict,result_dict):
    for key,value in expect_json_dict.items():
        if not actual_json_dict.has_key(key):
            result_dict[key] = "miss key"
            continue
        actual_value = actual_json_dict[key]
        if type(value) != type(actual_value):
            result_dict[key] = "value type dismatch"
            continue
        if isinstance(value, dict):
            #(ret,result_dict[key]) = DictIsEqual(value,actual_value)
            temp_dict = {}
            CompareDict(value,actual_value,temp_dict)
            result_dict[key] = temp_dict
        elif isinstance(value,list):
            (ret,result_dict[key]) = SliceIsEqual(value,actual_value)
            #return result_dict
        else:
            (ret,result_dict[key]) = ValueIsEqual(value,actual_value)
            #return result_dict

    
def CompareJson(expect_json_str,actual_json_str):
    expect_json_dict = ParseJson(expect_json_str)
    actual_json_dict = ParseJson(actual_json_str)
    if len(actual_json_dict) > len(expect_json_dict):
        print("actual_json_str keys more than expect_json_str")
    
    result_dict = {}
    for key,value in expect_json_dict.items():
        if not actual_json_dict.has_key(key):
            result_dict[key] = "miss key"
            continue
        actual_value = actual_json_dict[key]
        if type(value) != type(actual_value):
            result_dict[key] = "value type dismatch"
            continue
        if isinstance(value, dict):
            #(ret,result_dict[key]) = DictIsEqual(value,actual_value)
            temp_dict = {}
            CompareDict(value,actual_value,temp_dict)
            result_dict[key] = temp_dict
        elif isinstance(value,list):
            (ret,result_dict[key]) = SliceIsEqual(value,actual_value)
        else:
            (ret,result_dict[key]) = ValueIsEqual(value,actual_value)

    return result_dict


expect_json = """{"int_key":1,"double_key":1.2,"str_key":"xx_yy"}"""
actual_json1 = """{"int_key":1,"double_key":1.2,"str_key":"xx_yy"}"""
actual_json2 = """{"int_key":1,"double_key":"1.2","str_key":"xx_yy"}"""
actual_json3 = """{"int_key":1,"double_ey":1.2,"str_key":"xx_yy"}"""
actual_json4 = """{"employees": [{ "firstName":"John" , "lastName":"Doe" },{ "firstName":"Anna" , "lastName":"Smith" }]}"""
actual_json5 = """{"int_key":1,"str_key":"xx_yy","double_key":"1.2"}"""

expect_json1 = """{"xx": 2, "second": {"uu": "uu", "third": {"double_key": 1.2}}}"""
actual_json6 = """{"xx": 2, "second": {"uu": "uu", "third": {"double_key": 1.2}}}"""
actual_json7 = """{"xx": 3, "second": {"uu": 1.3, "third": {"double_key": 1.5}}}"""
actual_json8 = """{"xx1": 3, "second": {"uu": 1.3, "third": {"double_key1": 1.5}}}"""

slice1 = [1,3,4]
slice2 = [3,4,1]

if __name__ == "__main__":
    print(CompareJson(expect_json,actual_json1))
    print(CompareJson(expect_json,actual_json2))
    print(CompareJson(expect_json,actual_json3))
    print(CompareJson(expect_json1,actual_json6))
    print(CompareJson(expect_json1,actual_json7))
    print(CompareJson(expect_json1,actual_json8))
