"""
Test DAG pour vérifier le fonctionnement d'Airflow et PostgreSQL.

Ce DAG effectue des opérations simples et vérifie la connexion à la base de données PostgreSQL.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

# Arguments par défaut pour le DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Fonction pour tester la connexion à PostgreSQL
def test_postgres_connection():
    """
    Vérifie la connexion à PostgreSQL en comptant le nombre de tables dans le schéma public.
    
    Returns:
        str: Message indiquant le nombre de tables trouvées
    """
    hook = PostgresHook(postgres_conn_id='postgres_default')
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';")
    records = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return f"Nombre de tables dans le schéma public: {records[0]}"

# Création du DAG
with DAG(
    'test_dag',
    default_args=default_args,
    description='DAG de test pour vérifier Airflow et PostgreSQL',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    # Tâche 1: Création d'une table de test
    create_test_table = PostgresOperator(
        task_id='create_test_table',
        postgres_conn_id='postgres_default',
        sql="""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            test_value TEXT
        );
        """
    )

    # Tâche 2: Insertion de données dans la table
    insert_test_data = PostgresOperator(
        task_id='insert_test_data',
        postgres_conn_id='postgres_default',
        sql="""
        INSERT INTO test_table (test_value)
        VALUES ('Test depuis Airflow - {{ ds }}');
        """
    )

    # Tâche 3: Vérification des données
    verify_data = PostgresOperator(
        task_id='verify_data',
        postgres_conn_id='postgres_default',
        sql="SELECT COUNT(*) FROM test_table;"
    )

    # Tâche 4: Test de la connexion avec un hook
    test_connection = PythonOperator(
        task_id='test_connection',
        python_callable=test_postgres_connection,
    )

    # Définition de l'ordre des tâches
    create_test_table >> insert_test_data >> verify_data >> test_connection 