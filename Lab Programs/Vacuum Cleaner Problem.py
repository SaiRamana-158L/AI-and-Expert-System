def vacuum(initial_state):
    pos, left, right = initial_state
    print("Initial:", initial_state)

    while left == "dirty" or right == "dirty":
        if pos == "left":
            if left == "dirty":
                print("Left dirty → CLEAN")
                left = "clean"
            else:
                print("Move to RIGHT")
                pos = "right"

        elif pos == "right":
            if right == "dirty":
                print("Right dirty → CLEAN")
                right = "clean"
            else:
                print("Move to LEFT")
                pos = "left"

    print("Final:", (pos,left,right))

vacuum(("left","dirty","dirty"))
