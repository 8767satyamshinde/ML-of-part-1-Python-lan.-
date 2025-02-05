marks = {
    "Satyam": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Satyam"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rutuja": 99, "Radha": 100})
print(marks)

print(marks.get("Satyam")) # Prints None
print(marks["Satyam"]) # Returns an error