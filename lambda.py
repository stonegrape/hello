# dict
people = [
    {"name": "李白", "poetry": "a君不见黄河之水天上来，奔流到海不复回"},
    {"name": "杜甫", "poetry": "c安得广厦千万间，大庇天下寒士俱欢颜"},
    {"name": "李清照", "poetry": "b横看成岭侧成峰，远近高低各不同"}
]

'''
def f(person):
    return person["name"]
'''

# takes person as input and returns their name
# python actually sort by their name
people.sort(key=lambda person: person["name"])
print(people)
