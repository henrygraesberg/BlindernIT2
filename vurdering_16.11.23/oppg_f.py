def sjekk_reise(reise: "list[list]"):
    for i in range(len(reise) - 1):
        if reise[i][1] != reise[i + 1][0]:
            return False
    
    return True

print(sjekk_reise([["Russland", "Tyskland"], ["Tyskland", "Sverige"]]))
print(sjekk_reise([["Russland", "Tyskland"], ["Tyskland", "Sverige"], ["Norge", ["Tyskland"]]]))