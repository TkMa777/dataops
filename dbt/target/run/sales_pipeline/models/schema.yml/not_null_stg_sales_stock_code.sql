select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select stock_code
from "airflow_db"."public_staging"."stg_sales"
where stock_code is null



      
    ) dbt_internal_test