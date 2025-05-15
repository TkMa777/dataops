select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      





with validation_errors as (

    select
        invoice_no, stock_code
    from "airflow_db"."public_staging"."stg_sales"
    group by invoice_no, stock_code
    having count(*) > 1

)

select *
from validation_errors



      
    ) dbt_internal_test