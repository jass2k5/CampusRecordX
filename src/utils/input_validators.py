def is_valid_email(email):
        return  email.count("@") == 1 and email.endswith(("gmail.com","outlook.com","yahoo.com"))
def is_valid_text_input(name: str) ->bool:#checking_syntax 
        return name.replace(" ","").isalpha()
def is_valid_roll(roll):
        try:
                return int(roll)
        except ValueError:
                return None
def is_valid_phone(phone):
        # return len(phone) != 10 or not phone.isdigit() this is invalid because we are only returning true writing this as a future note
        return len(phone) == 10 and phone.isdigit() # ensures true if both are true unlike or even if one wrong then false
def is_valid_cgpa(cgpa):
        try:
                cgpa = float(cgpa)
                return cgpa >= 0.0 and cgpa <= 10.0 and round(cgpa,2) == cgpa
        except (ValueError or TypeError):
                return False
