import re

text="Your password is 92837487"
new_text=re.sub(r'\d', '*', text)
print("Masked:", new_text)