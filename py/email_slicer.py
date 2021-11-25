print("Email Slicer v1.0")
print("Copyrihght (c) 2020 miniprime1\n")
email = input("Enter Email Address: ").strip()

try: 
    user_name = email[:email.index("@")]
    domain_name = email[email.index("@")+1:]
except: 
    print("\nError: cannot slice email")

print(f"Username: {user_name} \nDomain Name: {domain_name}")