-- Actualizar los sueldos de los empleados que ganen $5000 o menos, de acuerdo al reajuste anual del continente al que pertenecen. 

SELECT continents.name, continents.anual_adjustment, employees.salary, employees.first_name, employees.last_name 
FROM employees 
JOIN countries ON countries.id = employees.country_id 
JOIN continents ON continents.id = countries.continent_id WHERE salary <= 5000

UPDATE employees
JOIN countries ON employees.country_id = countries.id
JOIN continents ON countries.continent_id = continents.id
SET 
    employees.salary = employees.salary * ((continents.anual_adjustment/100)+1)
WHERE
    employees.salary <= 5000