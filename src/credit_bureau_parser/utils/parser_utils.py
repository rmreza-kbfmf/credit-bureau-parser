import inspect
import os
import csv

from io import StringIO


def string_to_tuple(s):
    #ALF - Handling the values where there's a comma
    s = s.strip().rstrip(',')
    reader = csv.reader(StringIO(s), quotechar="'", skipinitialspace=True)
    row = next(reader)
    result = tuple(
        None if v.strip().upper() == "NULL" or v.strip() == '' else v.strip()
        for v in row
    )
    return result

def format_row_with_timestamp(row, created_at):
    try:
        row_str = ",".join(format_value(v) for v in row)
        row_str += f",{created_at}"
        return row_str
    except Exception as e:
        print(f"❌ Error formatting row: {row}")
        print(f"⚠️ Exception: {e}")
        return None  # Skip on error

def concat_string(string_value, string_concat):
    tmp = None
    try:
        if len(string_value) <= 2:
            string_value_new = string_value
        else:
            middle = string_value[1:-1]
            middle = middle.replace("\n", " ").replace("\r", " ")  # remove newlines
            middle = " ".join(middle.split())  # collapse multiple spaces
            middle = middle.replace("'", "''")  # escape single quotes for SQL
            string_value_new = string_value[0] + middle + string_value[-1]
        tmp = string_concat + string_value_new + ","
    except Exception as e:
        print(f'ERROR: in concat - {e}')

    return tmp

def format_value(v):
    if v is None:
        return ""
    if isinstance(v, str):
        # Handle numeric strings with decimal ".00"
        if v.replace(".", "", 1).isdigit():
            if v.endswith(".00"):
                return str(int(float(v)))  # "10000.00" → 10000
            if v.endswith(".0"):
                return str(int(float(v)))  # "10000.0" → 10000
            elif v.startswith("0") and not v.startswith("0.") and v != "0":
                return f'"{v}"'  # Keep leading zero strings like phone numbers
            else:
                return v  # Already a valid numeric string
        return f'"{v}"'
    return str(v)

def get_value(value, field, field_int):


    #RMR - Handle None value to put as NULL
    tmp = "NULL"
    try:
        if value is None or (isinstance(value, str) and len(value) == 0):
            tmp = "NULL"
        elif (isinstance(value, dict)):
            tmp = "NULL"
        elif field in field_int:
            tmp = format_value(value)
        else:
            tmp = f"'{value}'"


    except Exception as e:
        # print('-------')
        # print(field)
        # print(f'error in get value : {e}')
        pass
    return tmp

def get_amount(value, field):
    tmp = ''
    try:
        value = value['LocalValue']
        if value == "0.00":
            tmp = "0"
        else:
            tmp = value[0:-3]
    except KeyError:
        pass
    return tmp

def get_field_value(value, field, sql_field, sql_values, field_int):
    tmp_value = get_value(value, field, field_int)
    sql_field = concat_string(field, sql_field)
    sql_values = concat_string(tmp_value, sql_values)
    return sql_field, sql_values

def set_field_value(filename):
    FileName = os.path.basename(filename)
    field = "FileName,"
    values = "'" + FileName + "',"
    return field, values


def is_object(tag, object):
    """
    Retrieves the value associated with a given tag from a dictionary unless the value is itself a dictionary.

    Parameters:
    tag (str): The key to look up in the dictionary.
    object (dict): The dictionary from which to retrieve the value.

    Returns:
    str: The value associated with the tag if it is not a dictionary, otherwise an empty string.
    
    Note:
    - If `object[tag]` is not a dictionary, it returns its value.
    - If `object[tag]` is a dictionary, it returns an empty string.
    - Assumes `tag` exists in `object`; otherwise, it will raise a `KeyError`.
    """   
    # tmp  = object[tag] if not isinstance(object[tag], dict) else ""

    if isinstance(object, dict) and not isinstance(object.get(tag, ""), dict):
        tmp = object.get(tag,"") 
    elif isinstance(object, list):
        tmp = object[0].get(tag,"") 
    else: 
        tmp = get_value(object, tag, field_int=None)   
    return tmp

def get_sql_text(table_name, sql_columns, sql_values,
                 XML_FOLDER="xml", PEFINDO_ID=""):
   try:
      sql_columns = concat_string("created,FolderSource", sql_columns)
      sql_values = concat_string("GETDATE(),'" + XML_FOLDER + "'", sql_values)
      sql = "Insert into " + table_name + " (PefindoID," + sql_columns[:-1] + ") values ('" + PEFINDO_ID + "'," + sql_values[:-1] + ");"
      # # DB.execute(sql)

   except:
      pass

def remove_namespace(d):
    if isinstance(d, dict):
        return {
            k.split(":")[-1]: remove_namespace(v)
            for k, v in d.items()
        }
    elif isinstance(d, list):
        return [remove_namespace(i) for i in d]
    else:
        return d

def replace_nil_true(d):
    if isinstance(d, dict):
        # Detect {'nil': 'true'} pattern (case-insensitive)
        if set(d.keys()) == {'nil'} and str(d['nil']).lower() == 'true':
            res = None
            return res

        return {k: replace_nil_true(v) for k, v in d.items()}

    elif isinstance(d, list):
        return [replace_nil_true(item) for item in d]

    else:
        return d
    
def wrap_dicts_as_lists(obj):
    if isinstance(obj, dict):
        new_obj = {}
        for k, v in obj.items():
            if isinstance(v, dict):
                # Recursively process the inner dict, then wrap in list
                new_obj[k] = [wrap_dicts_as_lists(v)]
            elif isinstance(v, list):
                # Recursively process the list
                new_obj[k] = [wrap_dicts_as_lists(i) for i in v]
            else:
                new_obj[k] = v  # Leave non-dict/list types as-is
        return new_obj
    elif isinstance(obj, list):
        return [wrap_dicts_as_lists(i) for i in obj]
    else:
        return obj  # Return other types (str, int, float) as-is

def normalize_to_list(value):
    if value is None:
        value = []
    if not isinstance(value, list):
        value = [value]
    return value

def get_nested_dict(data, keys, default_value=None):
    """
    Safely get a value from a nested structure (dicts or lists of dicts)
    using a list of keys. Handles dicts wrapped in lists as well.
    """
    func_name = inspect.currentframe().f_code.co_name
    
    try:
        for key in keys:
            has_value = False
            if isinstance(data, list) and len(data) == 1:
                # Always take the first item in the list if it's a list of dicts
                data = data[0] if data else default_value
                default_value = data

            if isinstance(data, dict):
                data = data.get(key, default_value)            

        return data
    except (KeyError, IndexError, TypeError) as e:
        print(f"ERROR get nested dict: {e}")
        return default_value

def get_sql_field_values_list(sql_field, sql_values, sql_field_list=[], sql_values_list = []):

    sql_field = string_to_tuple(sql_field)
    sql_values = string_to_tuple(sql_values)

    sql_field_list.append(sql_field)
    sql_values_list.append(sql_values)

    sql_field_list = list(set(sql_field_list))

    return sql_field_list, sql_values_list
