"""
Made by Mark Richard
"""
visitors_dic = {
    "monday": [10, 15, 20],
    "tuesday": [12, 18],
    "wednesday": [8, 14, 16],
    "thursday": [20],
    "friday": [30, 25],
    "saturday": [40, 35, 30],
    "sunday": [18, 22]
}

results = {}

week_total = 0
week_count = 0

for day, visitors in visitors_dic.items():
    total = sum(visitors)
    average = total / len(visitors)

    results[day] = {
        "total": total,
        "average": average
    }

    week_total += total
    week_count += len(visitors)

week_average = week_total / week_count

print("Daily Results:")
for day, data in results.items():
    print(f"{day.capitalize()}:")
    print(f"  Total Visitors: {data['total']}")
    print(f"  Average Visitors: {data['average']:.2f}")

print("\nWeekly Results")
print("Total Visitors:", week_total)
print("Average Visitors:", round(week_average, 2))
