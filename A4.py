Bikes = {
    "names" : ["kawasaki","hero","yamaha","bajaj","suzuki"],
    "model" : ["ninja","xpluse","r15","dominar","vstrom"],
    "color" : ["black","white","blue","green","yellow"]
    }


print(Bikes)

print(Bikes.keys())

print(Bikes.values())

Bikes["location"] = ["blr","chennai","kerala","udaipur","rawat"]

print(Bikes)

Bikes["location"][4] = "kerala"

print(Bikes)

del Bikes["color"]

print(Bikes)

print(len(Bikes))

print(Bikes.clear())
