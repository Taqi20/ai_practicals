def monkey_banana():
    monkey_pos = 'A'
    box_pos = 'B'
    banana_pos = 'C'
    monkey_status = 'on_floor'

    actions = []

    if monkey_pos != box_pos:
        actions.append(f"Go({box_pos})")
        monkey_pos = box_pos

    actions.append(f"Push(Box, {banana_pos})")
    box_pos = banana_pos
    monkey_pos = banana_pos  

    if monkey_status == 'on_floor':
        actions.append("Climb(Box)")
        monkey_status = 'on_box'

    if monkey_status == 'on_box' and monkey_pos == banana_pos and box_pos == banana_pos:
        actions.append("Grasp")
        monkey_status = 'has_banana'

    if monkey_status == 'has_banana':
        actions.append("Goal Reached: Monkey has the banana!")

    return actions

steps = monkey_banana()

print("Plan to get the banana:")
for step in steps:
    print(step)
