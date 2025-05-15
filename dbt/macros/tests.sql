{% macro test_positive_values(model, column_name) %}

-- Teste si les valeurs d'une colonne sont toutes positives
WITH validation AS (
    SELECT
        {{ column_name }} AS value
    FROM {{ model }}
),

validation_errors AS (
    SELECT
        value
    FROM validation
    WHERE value <= 0 OR value IS NULL
)

SELECT * FROM validation_errors

{% endmacro %}


{% macro test_date_in_past(model, column_name) %}

-- Teste si les dates sont dans le passé (pas dans le futur)
WITH validation AS (
    SELECT
        {{ column_name }} AS date_value
    FROM {{ model }}
),

validation_errors AS (
    SELECT
        date_value
    FROM validation
    WHERE date_value > CURRENT_DATE
)

SELECT * FROM validation_errors

{% endmacro %}


{% macro test_percentage_complete(model, column_name, threshold=95) %}

-- Teste si le pourcentage de valeurs non nulles est supérieur au seuil
WITH column_values AS (
    SELECT
        {{ column_name }} AS value
    FROM {{ model }}
),

counts AS (
    SELECT
        COUNT(*) AS total_count,
        COUNT(value) AS non_null_count
    FROM column_values
),

percentage AS (
    SELECT
        (non_null_count * 100.0 / total_count) AS percent_complete
    FROM counts
),

validation_errors AS (
    SELECT 
        percent_complete
    FROM percentage
    WHERE percent_complete < {{ threshold }}
)

SELECT * FROM validation_errors

{% endmacro %} 