# In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. You will implement functions to add, update, delete, and view user settings.
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

def add_setting(settings, setting_pair):
    key, value = setting_pair
    key_lower = key.lower()
    value_lower = value.lower()
    if key_lower in settings:
        return f"Setting '{key_lower}' already exists! Cannot add a new setting with this name."
    else:
        settings[key_lower] = value_lower
        return f"Setting '{key_lower}' added with value '{value_lower}' successfully!"

def update_setting(settings, setting_pair):
    key, value = setting_pair
    key_lower = key.lower()
    value_lower = value.lower()
    if key_lower not in settings:
        return f"Setting '{key_lower}' does not exist! Cannot update a non-existing setting."
    settings[key_lower] = value_lower
    return f"Setting '{key_lower}' updated to '{value_lower}' successfully!"

def delete_setting(settings, key):
    key_lower = key.lower()
    if key_lower not in settings:
        return "Setting not found!"
    del settings[key_lower]
    return f"Setting '{key_lower}' deleted successfully!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    return output

test_settings = {
    'theme': 'dark',
    'language': 'English',
    'notifications': True
}

print(view_settings(test_settings))