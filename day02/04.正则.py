import re

# 1.定义规则
pattern=re.compile(r'^abc')
# pattern=re.compile(r'<script class="J_ContextData" type="text/template">(.*?)</script>')

# 2.匹配
result=pattern.findall('abcdefg')

print(result)
# List = [-2,1,3,-6]
# print(sorted(List, key=abs))
