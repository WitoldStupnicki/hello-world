import re
input_str = 'Kacy je pizze 666'
print(re.findall(r'\w+.\w+.\w+.\d{3}', input_str))