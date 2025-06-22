def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        default_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").strip()
        else:
            name = default_name

        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")
def extract_name_from_email(email):
    prefix = email.split('@')[0]
    name_parts = prefix.replace('.', ' ').split()
    return ' '.join(part.title() for part in name_parts)
main()
