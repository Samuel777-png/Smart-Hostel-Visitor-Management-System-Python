print("SMART HOSTEL VISITOR MANAGEMENT SYSTEM")

visitor_name = input("Enter Visitor Name: ")
student_name = input("Enter Student Name: ")
purpose = input("Enter Purpose of Visit: ")
visit_time = input("Enter Visit Time: ")

if purpose.lower() == "academic" or purpose.lower() == "official":
    access_status = "APPROVED"
else:
    access_status = "DENIED"

print("\n--- VISIT DETAILS ---")
print("Visitor Name:", visitor_name)
print("Student Visited:", student_name)
print("Purpose:", purpose)
print("Visit Time:", visit_time)
print("Access Status:", access_status)
