import whois
from validateDomain import is_registered
domain = input("Provide domain name: ")
domain_name = domain
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    # print if is registered
    print('Domain ' + domain_name + " is registered")
    # print the registrar
    print("Domain registrar:", whois_info.registrar)
    # print the WHOIS server
    print("WHOIS server:", whois_info.whois_server)
    # get the creation time
    print("Domain creation date:", whois_info.creation_date)
    # get expiration date
    print("Expiration date:", whois_info.expiration_date)
    # print all other info
    print(whois_info)