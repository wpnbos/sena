from pathlib import Path
from random import shuffle
from collections import Counter
import sys

exercise_dir = Path(__file__).parent

exercises = list(exercise_dir.glob("*.csv"))
print("Please choose exercise:")
for i, exercise in enumerate(exercises):
    print(i + 1, "-", exercise.stem)
exercise_choice = int(input("Exercise number: ").strip()) - 1

exercise = {
    line.split(',')[0]: line.split(',')[1]
    for line in exercises[exercise_choice].read_text().splitlines() if line
}
inv_exercise = {
    v: k for k, v in exercise.items()
}

queue = list(exercise.keys())
shuffle(queue)

mistakes = []
while True:
    made_mistake = False
    if not queue:
        print(f"Finished exercise! Mistakes made: {len(mistakes)}.")
        mistake_counts = Counter(mistakes)
        if mistakes:
            print(f"You struggled with these characters: {dict(mistake_counts)}")
            export_mistakes = input("Create new exercise for these mistakes? y/n: ").strip()
            if export_mistakes.lower() == "y":
                filename = input("Enter filename (no extension): ")
                exercise_dir.joinpath(f"{filename}.csv").write_text(
                    "\n".join([f"{h},{exercise[h]}" for h in set(mistakes)])
                )
        sys.exit(0)
    query = queue[-1]
    answer = input(f'{query}: ').strip()
    while answer != exercise[query]:
        made_mistake = True
        mistakes.append(query)
        print(f"WRONG!!! try again. True answer for '{answer}' is {inv_exercise.get(answer)}")
        answer = input(f'{query}: ').strip()
    if not made_mistake:
        queue.pop()
    else:
        shuffle(queue)
