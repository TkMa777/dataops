select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select date
from "airflow_db"."public_marts"."fct_daily_revenue"
where date is null



      
    ) dbt_internal_test