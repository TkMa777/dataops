select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select invoice_date
from "airflow_db"."public_staging"."stg_sales"
where invoice_date is null



      
    ) dbt_internal_test