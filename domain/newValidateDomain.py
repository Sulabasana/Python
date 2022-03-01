import whois

domain = input("Provide domain name: ")

# def check_reg(name):
#     try:
#         domain_info = whois.whois(name)
#         return True
#     except:
#         return False

# check_reg(domain)

domain_info = whois.whois(domain)

# #keys from dictionary
# for key in domain_info.keys():
#     print(key)

for key, value in domain_info.items():
    print(key,':', value)


