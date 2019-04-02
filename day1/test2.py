
salary = [1000, 2000, 3000, 4000, 5000]

taxed_salary = [s * 0.967 for s in salary]

print(taxed_salary)

d = dict(zip(salary, taxed_salary))

print(d)

print()
for s in d:
    print("salary(" + str(s) + "): " + str(d.get(s)))
