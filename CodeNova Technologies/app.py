from auth import login_user, register_user
from incident_response import log_incident, view_incidents
from bia import add_bia_record, view_bia_records
from utils import log_event


# ================================
# MAIN MENU
# ================================
def main_menu():
    print("\n=== CodeNova Security System ===")
    print("[1] Login")
    print("[2] Register (User/Admin)")
    print("[0] Exit")
    return input("Choose an option: ")


# ================================
# MENU AFTER LOGIN
# ================================
def logged_in_menu(username, is_admin):
    print(f"\n=== Welcome, {username} ===")
    print("[1] Report Security Incident")
    print("[2] View Incident Logs")
    print("[3] Add BIA Record")
    print("[4] View BIA Records")
    if is_admin:
        print("[5] View Admin System Logs")
    print("[0] Logout")
    return input("Choose an option: ")


# ================================
# MAIN PROGRAM LOOP
# ================================
def main():
    while True:
        choice = main_menu()

        # -------------------------------
        # LOGIN
        # -------------------------------
        if choice == '1':
            username, role = login_user()   # login_user returns a tuple
            if not username:                # Login failed → skip rest
                continue

            is_admin = (role == "admin")

            # Logged-in loop
            while True:
                opt = logged_in_menu(username, is_admin)

                # REPORT INCIDENT
                if opt == '1':
                    log_incident(username)

                # VIEW INCIDENT LOGS
                elif opt == '2':
                    view_incidents()

                # ADD BIA RECORD
                elif opt == '3':
                    add_bia_record(username)

                # VIEW BIA RECORDS
                elif opt == '4':
                    view_bia_records()

                # ADMIN: VIEW SYSTEM LOGS
                elif opt == '5' and is_admin:
                    print("\n--- SYSTEM LOGS ---")
                    try:
                        with open("system.log", "r") as f:
                            print(f.read())
                    except FileNotFoundError:
                        print("No logs available yet.")

                # LOGOUT
                elif opt == '0':
                    print("Logged out.")
                    log_event(f"{username} logged out.")
                    break

                else:
                    print("Invalid option.")

        # -------------------------------
        # REGISTRATION
        # -------------------------------
        elif choice == '2':
            register_user()

        # -------------------------------
        # EXIT SYSTEM
        # -------------------------------
        elif choice == '0':
            print("Goodbye.")
            break

        else:
            print("Invalid option. Try again.")


# ================================
# ENTRY POINT
# ================================
if __name__ == "__main__":
    main()
