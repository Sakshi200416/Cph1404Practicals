def get_name_from_email(email):
    """Extract name from email."""
    name_part = email.split('@')[0]
    parts = name_part.replace('.', ' ').split()
    return " ".join(parts).title()

email_to_name = {}

email = input("Email: ")
while email != "":
    name = get_name_from_email(email)
    confirm = input(f"Is your name {name}? (Y/n) ").lower()
    if confirm != "y" and confirm != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
