import raspy

def model():
    length = (raspy.key(1) == raspy.query(1)).value(1)
    breakpoint()
    flip = (raspy.key(length - raspy.indices - 1) == raspy.query(raspy.indices)).value(raspy.tokens)
    return flip

if __name__ == "__main__":
    print(model())
