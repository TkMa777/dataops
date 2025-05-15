
    
    



select CustomerID
from (select * from "airflow_db"."public"."raw_sales" where "CustomerID" is not null) dbt_subquery
where CustomerID is null


