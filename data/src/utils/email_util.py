def is_valid_email(email):
        return  email.count("@") == 1 and email.endswith(("gmail.com","outlook.com","yahoo.com"))