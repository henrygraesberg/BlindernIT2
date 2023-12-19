from motorsykkel import Motorcycle

def test_mc():
    mc_result = Motorcycle("Aprilia", "BR5732", 234_450)
    mc_expected = {
        "brand": "Aprilia",
        "licence_nr": "BR5732",
        "distance_driven": 234_450
    }

    add_distance = 10

    mc_result.drive(add_distance)

    dist_driven_result = mc_result.get_distance_driven()
    dist_driven_expected = mc_expected["distance_driven"] + add_distance

    del add_distance

    assert dist_driven_result == dist_driven_expected, f'Expected {dist_driven_expected}, but got {dist_driven_result}'

def main():
    test_mc()

    mc1 = Motorcycle("BMW", "BR9852", 100_000)
    mc2 = Motorcycle("Aprilia", "BR5732", 234_450)
    mc3 = Motorcycle("Ducati", "HZ7862", 320_873)

    print(mc1, "\n", mc2, "\n", mc3)

if __name__ == "__main__":
    main()