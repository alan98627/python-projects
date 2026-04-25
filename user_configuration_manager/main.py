def add_setting(settings, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists!"
    else:
        settings[key] = value
        return f"Setting '{key}' added successfully!"


def update_setting(settings, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated successfully!"
    else:
        return f"Setting '{key}' does not exist!"


def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current Settings:\n"
    for key, value in settings.items():
        result += f"{key}: {value}\n"
    return result


def main():
    settings = {}

    while True:
        print("\n=== User Configuration Manager ===")
        print("1. Add Setting")
        print("2. Update Setting")
        print("3. Delete Setting")
        print("4. View Settings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            print(add_setting(settings, (key, value)))

        elif choice == "2":
            key = input("Enter key: ")
            value = input("Enter new value: ")
            print(update_setting(settings, (key, value)))

        elif choice == "3":
            key = input("Enter key to delete: ")
            print(delete_setting(settings, key))

        elif choice == "4":
            print(view_settings(settings))

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()