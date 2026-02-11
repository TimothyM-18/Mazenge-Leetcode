# Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

from typing import Dict, Union

DeepNestedDict = Dict[str, Union[str, 'DeepNestedDict']]

def flatten_dictionary(dictionary: DeepNestedDict) -> Dict[str, str]:

    if not dictionary:
        return {}

    result = {}
    def dfs(parent_key, value):

        for k, v in value.items():
            if k == "":
                new_key = parent_key
            else:
                if parent_key:
                    new_key = parent_key + "." + k
                else:
                    new_key = k
            if isinstance(v, dict):
                dfs(new_key, v)
            else:
                result[new_key] = v
    
    dfs("", dictionary)
    return result

dict_input = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

print(flatten_dictionary(dict_input))