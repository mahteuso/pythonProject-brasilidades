import re


# simple template
template = "[0-9][a-z]{2}[0-9]"
text = "123 acb 1bc3 999 bca"
verify = re.search(template, text)
verify = verify.group()

print(verify)

# e-mail template
email_template = "\w{3,30}@[a-z]{3,10}.\w{2,3}.\w{2,3}"
e_mail = "asdk m_ateuso@hotmail.com.br 2143"
verify = re.search(email_template, e_mail)
verify = verify.group()
print(verify)

# telephone template
phone_template = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
phone_test = "15981521625"
verify = re.search(phone_template, phone_test)
verify = verify.group()
print(verify)





