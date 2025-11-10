#JC dictionary notes 2nd


govinfo = {
    #Key: Value,
    "name": "Jaxon",
    "age": 15,
    "Job": "Unemployed",
    "Reletives": ["micah", "Juan", "luara", "jenny"]
}

print(govinfo["name"])
print(govinfo.keys())
for key in govinfo.keys():
    print(f"{key} is {govinfo[key]}")
govinfo["birthday"] = "Nov 2"

avatar = {
    "earth": {
        "toph": "Is a charater "
    },
    "water": {
        "Katara": "Is a charater ",
        "Sokka": "i dont know what to write"
    },
}


print(avatar["earth"]["toph"])