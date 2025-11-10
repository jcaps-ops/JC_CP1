#JC dictionary notes 2nd


govinfo = {
    "name": "Jaxon",
    "age": 15,
    "Job": "Unemployed",
    "Reletives": ["micah", "Juan", "luara", "jenny"]
}

print(govinfo["name"])
print(govinfo.keys())
for key in govinfo.keys():
    print(f"{key} is {govinfo[key]}")