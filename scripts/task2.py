import argparse
import json

import jsonpath_rw


JSON_TEMPLATE = {
    "connections": {},
    "access": []
}


def get_value(query, data):
    query = query.split('/')
    first_res = data.get(query[0])
    error_message = "No such field in json. Check --get argument"

    if first_res:
        for i in query[1:]:
            try:
                next_value = first_res[i]
                first_res = next_value
            except KeyError:
                return error_message

        return first_res

    return error_message


def set_value(val, query, data):
    query_arr = query.split('/')
    query = '.'.join([f"\'{i}\'" for i in query_arr[:-1]])
    
    json_path = jsonpath_rw.parse(query)  

    value = [match.value for match in json_path.find(data)][0]

    value[query_arr[-1]] = val

    with open('schema.json', 'w+') as file:
    	json.dump(data, file, indent=4)


def main():
    json_file = open('schema.json', 'a+')
    json_file.seek(0)
    text = json_file.read()

    if not text:
        json.dump(JSON_TEMPLATE, json_file, indent=4)
        json_file.flush()

    json_file.seek(0)
    data = json.load(json_file)

    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--get', nargs='?', type=str)
    parser.add_argument('--set', nargs='?', type=str)
    parser.add_argument('--value', nargs='?', type=str)

    args = parser.parse_args()
    data = main()

    if args.get:
        print(get_value(args.get, data))
    if args.set and args.value:
        set_value(args.value, args.set, data)
