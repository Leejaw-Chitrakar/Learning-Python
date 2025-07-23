def generate_invite(name, location, time):
    return (f"""
    Dear {name},

    your are invited to our jail.
    Location {location} 
    Time {time}. 
""")


student_name = ["ram",
                "shyam",
                "hari"
                ]
location = "Kathmandu"
time = "10:00 AM"

for name in student_name:
    invitation = generate_invite(name, location, time)
    print(invitation)