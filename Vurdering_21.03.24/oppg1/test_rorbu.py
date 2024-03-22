import rorbu, gjest

rorbua = rorbu.Rorbu()
gjesteliste = []

for i in range(100):
    gjesteliste.append(gjest.Gjest())

for guest in gjesteliste:
    rorbua.legg_til_gjest(guest)

rorbua.fortell_vits(200)

print(rorbua.hvor_morsomt_har_vi_det())

rorbua.fortell_vits(1000)

print(rorbua.hvor_morsomt_har_vi_det())