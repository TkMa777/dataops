"""
Tests unitaires pour les modèles dbt
"""

import os
import yaml
import pytest
import glob

class TestDbtModels:
    """
    Test cases pour les modèles dbt
    """
    
    @pytest.fixture
    def dbt_project_path(self):
        """
        Fixture pour le chemin du projet dbt
        """
        return os.path.join(os.path.dirname(__file__), "../dbt")
    
    @pytest.fixture
    def dbt_project_config(self, dbt_project_path):
        """
        Fixture pour la configuration du projet dbt
        """
        config_path = os.path.join(dbt_project_path, "dbt_project.yml")
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def test_dbt_project_exists(self, dbt_project_path):
        """
        Test si le projet dbt existe
        """
        assert os.path.exists(dbt_project_path)
        assert os.path.exists(os.path.join(dbt_project_path, "dbt_project.yml"))
    
    def test_dbt_project_config(self, dbt_project_config):
        """
        Test si la configuration du projet dbt est valide
        """
        assert dbt_project_config.get('name') == 'sales_pipeline'
        assert dbt_project_config.get('profile') == 'sales_pipeline'
    
    def test_stg_sales_model_exists(self, dbt_project_path):
        """
        Test si le modèle stg_sales existe
        """
        model_path = os.path.join(dbt_project_path, "models/staging/stg_sales.sql")
        assert os.path.exists(model_path)
        
        # Vérifier le contenu du modèle
        with open(model_path, 'r') as f:
            content = f.read().lower()
            assert 'select' in content
            assert 'from' in content
            assert 'invoice_no' in content
            assert 'customer_id' in content
    
    def test_fct_daily_revenue_model_exists(self, dbt_project_path):
        """
        Test si le modèle fct_daily_revenue existe
        """
        model_path = os.path.join(dbt_project_path, "models/marts/fct_daily_revenue.sql")
        assert os.path.exists(model_path)
        
        # Vérifier le contenu du modèle
        with open(model_path, 'r') as f:
            content = f.read().lower()
            assert 'select' in content
            assert 'from' in content
            assert 'revenue' in content
            assert 'group by' in content
    
    def test_schema_yml_exists(self, dbt_project_path):
        """
        Test si le fichier schema.yml existe
        """
        schema_path = os.path.join(dbt_project_path, "models/schema.yml")
        assert os.path.exists(schema_path)
        
        # Vérifier le contenu du schéma
        with open(schema_path, 'r') as f:
            schema = yaml.safe_load(f)
            assert 'version' in schema
            assert 'models' in schema
            
            # Vérifier si les modèles sont définis dans le schéma
            model_names = [model.get('name') for model in schema.get('models', [])]
            assert 'stg_sales' in model_names
            assert 'fct_daily_revenue' in model_names 