"""
Tests unitaires pour la configuration Great Expectations
"""

import os
import yaml
import pytest
import json

class TestGreatExpectations:
    """
    Test cases pour Great Expectations
    """
    
    @pytest.fixture
    def ge_dir(self):
        """
        Fixture pour le chemin de Great Expectations
        """
        return os.path.join(os.path.dirname(__file__), "../great_expectations")
    
    def test_ge_config_exists(self, ge_dir):
        """
        Test si la configuration de Great Expectations existe
        """
        config_path = os.path.join(ge_dir, "great_expectations.yml")
        assert os.path.exists(config_path)
        
        # Vérifier le contenu de la configuration
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            assert config.get('config_version') is not None
            assert 'datasources' in config
            assert 'stores' in config
    
    def test_expectations_exist(self, ge_dir):
        """
        Test si les expectations existent
        """
        expectations_dir = os.path.join(ge_dir, "expectations")
        assert os.path.exists(expectations_dir)
        
        # Vérifier si la suite d'expectations existe
        suite_path = os.path.join(expectations_dir, "raw_sales_suite.json")
        assert os.path.exists(suite_path)
        
        # Vérifier le contenu de la suite
        with open(suite_path, 'r') as f:
            suite = json.load(f)
            assert suite.get('expectation_suite_name') == 'raw_sales_suite'
            assert 'expectations' in suite
            
            # Vérifier si certaines expectations spécifiques sont présentes
            expectation_types = [exp.get('expectation_type') for exp in suite.get('expectations', [])]
            assert 'expect_table_row_count_to_be_between' in expectation_types
            assert 'expect_column_values_to_not_be_null' in expectation_types
            assert 'expect_compound_columns_to_be_unique' in expectation_types
    
    def test_checkpoint_exists(self, ge_dir):
        """
        Test si les checkpoints existent
        """
        checkpoints_dir = os.path.join(ge_dir, "checkpoints")
        assert os.path.exists(checkpoints_dir)
        
        # Vérifier si le checkpoint existe
        checkpoint_path = os.path.join(checkpoints_dir, "raw_sales_checkpoint.yml")
        assert os.path.exists(checkpoint_path)
        
        # Vérifier le contenu du checkpoint
        with open(checkpoint_path, 'r') as f:
            checkpoint = yaml.safe_load(f)
            assert checkpoint.get('name') == 'raw_sales_checkpoint'
            assert checkpoint.get('expectation_suite_name') == 'raw_sales_suite'
            assert 'batch_request' in checkpoint
            assert 'action_list' in checkpoint 