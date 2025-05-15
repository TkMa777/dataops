select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select CustomerID
from (select * from "airflow_db"."public"."raw_sales" where "CustomerID" is not null) dbt_subquery
where CustomerID is null



      
    ) dbt_internal_test