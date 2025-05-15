
  create view "airflow_db"."public"."example_model__dbt_tmp"
    
    
  as (
    /*
  Modèle d'exemple pour démontrer l'utilisation de dbt
*/

SELECT 
  1 as id,
  'exemple' as nom,
  current_timestamp as date_creation
  );