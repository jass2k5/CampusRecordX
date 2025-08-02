# utils/input_helpers.py
def get_user_input(prompt):
    user_input = input(prompt).strip()
    
    if user_input.lower() in ['q', 'e']:
        print("Exiting input... 🏃‍♂️")
        return None
    
    return user_input
