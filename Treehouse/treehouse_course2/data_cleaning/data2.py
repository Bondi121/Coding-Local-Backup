


data = [
    {
        "email": "we@afi.co",
        "name": "Warren Bates",
        "date_joined": "4/20/2048",
        "admin": "False",
        "id": "36"
    },
    {
        "email": "koz@ma.cf",
        "name": "Edgar Howell",
        "date_joined": "2/2/2022",
        "admin": "False",
        "id": "40"
    },
    {
        "email": "li@kifal.vi",
        "name": "Benjamin Newman",
        "date_joined": "6/12/2090",
        "admin": "False",
        "id": "17"
    },
    {
        "email": "unauli@suiju.gw",
        "name": "Ray Greer",
        "date_joined": "9/15/2022",
        "admin": "False",
        "id": "71"
    },
    {
        "email": "vi@cipu.io",
        "name": "Ina Goodman",
        "date_joined": "1/19/2052",
        "admin": "False",
        "id": "8"
    },
    {
        "email": "bannoj@jik.hm",
        "name": "Irene Larson",
        "date_joined": "10/16/2053",
        "admin": "False",
        "id": "73"
    },
    {
        "email": "kaf@wun.nr",
        "name": "Florence Olson",
        "date_joined": "8/27/2031",
        "admin": "False",
        "id": "89"
    },
    {
        "email": "imuahezu@ga.fo",
        "name": "Madge Edwards",
        "date_joined": "9/10/2117",
        "admin": "False",
        "id": "35"
    },
    {
        "email": "tagap@ulti.fm",
        "name": "Lola Griffin",
        "date_joined": "4/20/2023",
        "admin": "False",
        "id": "27"
    },
    {
        "email": "ku@oku.mg",
        "name": "Bryan Tate",
        "date_joined": "6/1/2036",
        "admin": "False",
        "id": "98"
    },
]


# 1) Split the full name into two fields, first name and last name




    
    # print (type(id))


# 4) Keep the rest of the info the same

# 5) Complete this in a function(s)


def converting_list(data):
    
    for item in data:
        name = item["name"]
        first_and_last_name = name.split(" ")
        first_name = first_and_last_name[0]
        last_name = first_and_last_name[1]
        item["first_name"] = first_name
        item["last_name"] = last_name
        # print(item["name"])
      #  del item["name"]

    for item in data:
        admin = item["admin"]
        if admin == "False":
            item["admin"] = False
        else:
            item["admin"] = True

    for item in data:
        id = int(item["id"])
        item["id"] = id

    return data

converting_list(data)


# 6) Save the data into a new data structure: a list of dictionaries

