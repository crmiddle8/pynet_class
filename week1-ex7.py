#!/usr/bin/env python


#Write a Python program that reads both the YAML file and the JSON file created in exercise6 and
#pretty prints the data structure that is returned.
import yaml
import json

from pprint import pprint

def output_format(my_dict, my_str):
    '''
    Make the output format easier to read
    '''
    print '\n\n'
    print '#' * 3
    print '#' * 3 + my_str
    print '#' * 3
    pprint(my_dict)

def main():
    '''
    Read YAML and JSON files. Pretty print to standard out
    '''
    yaml_file = 'my_test.yml'
    json_file = 'my_test.json'

    with open(yaml_file) as f:
        yaml_dict = yaml.load(f)

    with open(json_file) as f:
        json_dict = json.load(f)

    output_format(yaml_dict, ' YAML')
    output_format(json_dict, ' JSON')
    print '\n'

if __name__ == "__main__":
    main()
