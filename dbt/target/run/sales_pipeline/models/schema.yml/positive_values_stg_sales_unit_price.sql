select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      

-- Teste si les valeurs d'une colonne sont toutes positives
WITH validation AS (
    SELECT
        unit_price AS value
    FROM "airflow_db"."public_staging"."stg_sales"
),

validation_errors AS (
    SELECT
        value
    FROM validation
    WHERE value <= 0 OR value IS NULL
)

SELECT * FROM validation_errors


      
    ) dbt_internal_test