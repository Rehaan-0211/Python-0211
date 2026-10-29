# Accept the gender of the user and input a greeting message following their input.

gender = str(input("Please specify your gender(specify in small letters only+if you have other gender type other):- "))

if gender == "male":
    print ("Good evening sir you are a male")
elif gender == "female":
    print ("Good evening mam you are a female")
elif gender == "other":
    print ("Good evening")
else :
    print("Invalid input please try again")