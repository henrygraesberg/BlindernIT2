def passasjerkontroll(navnlist: "list[str]", navn: str):
    for n in navnlist:
        print(n)
        if n == navn:
            return True
    return False

nlist = ["Øyvind", "Bashar", "Sham", "Henry"]
print(passasjerkontroll(nlist, "Henry"))
print(passasjerkontroll(nlist, "Thea"))