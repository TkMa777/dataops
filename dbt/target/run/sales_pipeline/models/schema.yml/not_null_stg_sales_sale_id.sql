select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select sale_id
from "airflow_db"."public_staging"."stg_sales"
where sale_id is null



      
    ) dbt_internal_test