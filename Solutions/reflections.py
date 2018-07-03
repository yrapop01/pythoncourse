def remove_non_reflections(d):
    for key, value in list(d.items()):
        if key != value[::-1]:
            del d[key]

def procedural():
    d = {"ab": "ba", "a": "b"}
    remove_non_reflections(d)
    print(d)

def non_reflections(d):
    return {key: value for key, value in d.items()
            if key == value[::-1]}

def functional():
    d = {"ab": "ba", "a": "b"}
    d = non_reflections(d)
    print(d)

if __name__ == "__main__":
    procedural()
    functional()
