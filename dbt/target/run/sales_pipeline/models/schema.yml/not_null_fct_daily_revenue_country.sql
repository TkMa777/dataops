select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select country
from "airflow_db"."public_marts"."fct_daily_revenue"
where country is null



      
    ) dbt_internal_test