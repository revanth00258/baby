import datetime

appointments = []
appointment_limit = 2

def schedule_vaccination(child_name):
    global appointments
    
    today = datetime.date.today()
    appointment_date = today + datetime.timedelta(days=2)

    while sum(1 for appointment in appointments if appointment['appointment_date'] == appointment_date) >= appointment_limit:
        appointment_date += datetime.timedelta(days=1)

    appointments.append({
        "child_name": child_name,
        "vaccine": "vaccine",
        "appointment_date": appointment_date,
        "status": "Scheduled"
    })
    print(f"Vaccination for {child_name} scheduled on {appointment_date}.")

def view_appointments():
    if not appointments:
        print("No appointments scheduled.")
        return
    
    search_choice = input("View all appointments or search by child's name? (all/name): ").strip().lower()
    
    if search_choice == "all":
        for idx, appointment in enumerate(appointments):
            print(f"\n{idx + 1}. {appointment['child_name']} - {appointment['vaccine']} on {appointment['appointment_date']} (Status: {appointment['status']})\n")
    
    elif search_choice == "name":
        child_name = input("Enter the child's name to search: ").strip()
        found_appointments = [appointment for appointment in appointments if appointment['child_name'].lower() == child_name.lower()]
        
        if found_appointments:
            for idx, appointment in enumerate(found_appointments):
                print(f"\n{idx + 1}. {appointment['child_name']} - {appointment['vaccine']} on {appointment['appointment_date']} (Status: {appointment['status']})\n")
        else:
            print(f"No appointments found for {child_name}.")
    else:
        print("Invalid choice. Please enter 'all' or 'search'.")

def update_appointment(index, new_date):
    if 0 <= index < len(appointments):
        appointments[index]['appointment_date'] = new_date
        appointments[index]['status'] = "Rescheduled"
        print(f"Appointment rescheduled to {new_date}.")
    else:
        print("Invalid appointment number.")


while True:
    print("Child Vaccination Management System")
    print("1. Schedule Vaccination")
    print("2. View Appointments")
    print("3. Reschedule Appointment")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        child_name = input("Enter child's name: ")
        schedule_vaccination(child_name)
    elif choice == "2":
        view_appointments()
    elif choice == "3":
        view_appointments()
        index = int(input("Enter appointment number to reschedule: ")) - 1
        new_date = input("Enter new appointment date (YYYY-MM-DD): ")
        update_appointment(index, new_date)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
