# Current world population (2026 estimate)
current_population = 8.3e9  # 8.3 billion

# Current growth rate (2026 estimate)
growth_rate = 0.0083  # 0.83%

# Calculate population growth for the next 100 years
population = current_population
year = 2026

print("Year\tPopulation\tIncrease")

for i in range(1, 101):
    increase = population * growth_rate
    population += increase
    year += 1
    print(f"{year}\t{population:.2e}\t{increase:.2e}")

    if population >= current_population * 2 and 'double_year' not in locals():
        double_year = year
    if population >= current_population * 4 and 'quadruple_year' not in locals():
        quadruple_year = year

print(f"Population will double by {double_year}")
print(f"Population will quadruple by {quadruple_year}")