#!/usr/bin/env python


#create a list (one of the elements of the list should be a dictionary with at
#least 2 keys)
#Write it to a file using both JSON and YAML...

import json
import yaml

def main():
    yaml_file = 'my_test.yml'
    json_file = 'my_test.json'

    my_dict = {
    'ip_add': '10.1.1.1',
    'vendor': 'cisco',
    'platform': 'cisco_ios',
    'model': '1921'
    }


    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_dict, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(my_dict, f)


if __name__ == "__main__":
    main()
