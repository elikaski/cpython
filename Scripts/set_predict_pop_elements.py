elements = [42, 123, True, "digital", "whisper", object()]
s = set(elements)
pop_indexes = [hash(element) % 32 for element in elements]

pops = {pop_indexes[i] : elements[i] for i in range(len(elements))}
for index in sorted(pops):
    prediction = pops[index]
    actual = s.pop()
    print("prediction:", prediction)
    print("actual:", actual)
    print()
    assert prediction == actual


