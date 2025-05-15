
    
    

select
    id as unique_field,
    count(*) as n_records

from "airflow_db"."public"."example_model"
where id is not null
group by id
having count(*) > 1


