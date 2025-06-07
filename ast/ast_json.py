import ast
import json
"""
针对一些格式不是很规范的json数据
直接用json.loads会报错
这里可以使用ast模块的literal_eval方法
"""
a = "{u'person':u'Julian',u'token':u'abc123'}"
print(a)
# json.loads(a) # json.decoder.JSONDecodeError: Expecting property name
b = ast.literal_eval(a)
print(b)
