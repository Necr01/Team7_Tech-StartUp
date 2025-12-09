from auth import login_user, register_user
from incident_response import log_incident, view_incidents
from bia import add_bia_record, view_bia_records
from utils import log_event

def main_menu():
    print("\n=== CodeNova Security System ===")
    print("[1] Login")
    print("[2] Register (User/Admin)")
    print("[0] Exit")
    return input("Choose an option: ")

def logged_in_menu(is_admin, username):
    print(f"\n=== Welcome, {username} ===")
    print("[1] Report Security Incident")
    print("[2] View Incident Logs")
    print("[3] Add BIA Record")
    print("[4] View BIA Records")
    if is_admin:
        print("[5] View Admin System Logs")
    print("[0] Logout")
    return input("Choose an option: ")

def main():
    while True:
        choice = main_menu()

        if choice == '1':
            user = login_user()
            if not user:
                continue

            username = user["username"]
            is_admin = user["role"] == "admin"

            while True:
                opt = logged_in_menu(is_admin, username)

                if opt == '1':
                    log_incident(username)

                elif opt == '2':
                    view_incidents()

                elif opt == '3':
                    add_bia_record(username)

                elif opt == '4':
                    view_bia_records()

                elif opt == '5' and is_admin:
                    print("\n--- SYSTEM LOGS ---")
                    with open("system.log", "r") as f:
                        print(f.read())

                elif opt == '0':
                    print("Logged out.")
                    log_event(f"{username} logged out.")
                    break

        elif choice == '2':
            register_user()

        elif choice == '0':
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
