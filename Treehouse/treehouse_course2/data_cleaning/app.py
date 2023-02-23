from data import data


# INSTRUCTIONS
# 1) Split the full name into two fields, first name and last name
# 2) Convert the admin field to a boolean value
# 3) Convert the id to an integer
# 4) Keep the rest of the info the same
# 5) Complete this in a function(s)
# 6) Save the data into a new data structure: a list of dictionaries


def clean_data(data):
    cleaned = []
    for user in data:
        print(user["name"])
        fixed = {}
        fixed["email"] = user["email"]
        split_name = user ["name"].split(" ")
        fixed["first_name"] = split_name[0]
        fixed["last_name"] = split_name[1]
        fixed["date_joined"] = user["date_joined"]
        if user ["admin"] == "True":
            fixed["admin"] = True
        else:
            fixed["admin"] = False
        fixed["id"] = int(user["id"])
        cleaned.append(fixed)
    return cleaned

print(clean_data(data)[0])