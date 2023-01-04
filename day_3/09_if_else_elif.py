required_age_at_school = 5
hammad_age = input("How old is Hammad? ")
hammad_age = int(hammad_age)        # Change class from string to int so there is not type error

# question: Can hammad go to school?
if hammad_age == required_age_at_school:
    print("Hammad can join the school")
elif hammad_age > required_age_at_school:
    print("Hammad can join the school")
elif hammad_age < required_age_at_school:
    print("You should take care of Hammad, He si still a baby")
else:
    print("Hammad can not join the school")




