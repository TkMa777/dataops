

-- Teste si les valeurs d'une colonne sont toutes positives
WITH validation AS (
    SELECT
        quantity AS value
    FROM "airflow_db"."public_staging"."stg_sales"
),

validation_errors AS (
    SELECT
        value
    FROM validation
    WHERE value <= 0 OR value IS NULL
)

SELECT * FROM validation_errors

