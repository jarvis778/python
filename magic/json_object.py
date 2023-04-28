# json to py object
import json

f = '{ "name":"bhonesh" , "age":23 }'

y = json.loads(f)

print(y["age"])

# py object to json

#
# import json
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)
