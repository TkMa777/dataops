"""
Tests unitaires pour le DAG de pipeline de ventes
"""

import os
import sys
import pytest
from airflow.models import DagBag

# Ajouter le chemin du dossier dags au path Python
sys.path.append(os.path.join(os.path.dirname(__file__), "../dags"))

class TestSalesPipelineDAG:
    """
    Test cases pour le DAG sales_pipeline
    """
    
    @pytest.fixture
    def dagbag(self):
        """
        Fixture pour initialiser DagBag
        """
        return DagBag(dag_folder=os.path.join(os.path.dirname(__file__), "../dags"), include_examples=False)
    
    def test_dag_loaded(self, dagbag):
        """
        Test si le DAG est correctement chargé
        """
        dag = dagbag.get_dag(dag_id="sales_pipeline")
        assert dagbag.import_errors == {}
        assert dag is not None
    
    def test_task_count(self, dagbag):
        """
        Test si le DAG a le bon nombre de tâches
        """
        dag = dagbag.get_dag(dag_id="sales_pipeline")
        assert len(dag.tasks) == 5
    
    def test_task_dependencies(self, dagbag):
        """
        Test si les dépendances entre tâches sont correctes
        """
        dag = dagbag.get_dag(dag_id="sales_pipeline")
        
        # Obtenir les tâches par ID
        check_file = dag.get_task("check_file_exists")
        load_data = dag.get_task("load_csv_to_postgres")
        validate_data = dag.get_task("validate_with_great_expectations")
        run_dbt = dag.get_task("run_dbt_transformations")
        test_dbt = dag.get_task("test_dbt_models")
        
        # Vérifier les dépendances
        downstream_tasks = {t.task_id: t for t in check_file.downstream_list}
        assert "load_csv_to_postgres" in downstream_tasks
        
        downstream_tasks = {t.task_id: t for t in load_data.downstream_list}
        assert "validate_with_great_expectations" in downstream_tasks
        
        downstream_tasks = {t.task_id: t for t in validate_data.downstream_list}
        assert "run_dbt_transformations" in downstream_tasks
        
        downstream_tasks = {t.task_id: t for t in run_dbt.downstream_list}
        assert "test_dbt_models" in downstream_tasks
    
    def test_dag_schedule(self, dagbag):
        """
        Test si le DAG a le bon planning d'exécution
        """
        dag = dagbag.get_dag(dag_id="sales_pipeline")
        assert dag.schedule_interval == "@daily" 