# Pipeline DataOps - Planification

## Architecture du projet

Le projet s'articule autour d'une architecture DataOps complète utilisant:
- **Apache Airflow** pour l'orchestration et la planification des tâches
- **dbt (data build tool)** pour la transformation des données
- **Great Expectations** pour la validation de la qualité des données
- **PostgreSQL** comme base de données relationnelle

## Structure des dossiers

```
dataops/
├── dags/                    # DAGs Airflow
│   └── sales_pipeline.py    # DAG principal du pipeline de ventes
├── data/                    # Données source
│   └── sales.csv            # Données de ventes (à ajouter)
├── dbt/                     # Configuration dbt
│   ├── models/              # Modèles dbt
│   │   ├── staging/         # Couche staging
│   │   │   └── stg_sales.sql
│   │   └── marts/           # Couche mart (analytique)
│   │       └── fct_daily_revenue.sql
│   ├── seeds/               # Données de référence
│   ├── macros/              # Fonctions SQL réutilisables
│   ├── tests/               # Tests personnalisés
│   ├── dbt_project.yml      # Configuration du projet dbt
│   └── profiles/            # Profils de connexion
├── great_expectations/      # Configuration Great Expectations
│   ├── expectations/        # Définitions des attentes qualité
│   ├── checkpoints/         # Points de contrôle
│   └── great_expectations.yml # Configuration principale
├── logs/                    # Logs d'exécution
├── plugins/                 # Plugins Airflow
├── docker-compose.yml       # Configuration des services
└── README.md                # Documentation
```

## Objectifs et contraintes

### Objectifs fonctionnels
1. Ingestion automatique quotidienne du fichier sales.csv
2. Transformation des données en modèles exploitables
3. Validation de la qualité des données
4. Agrégation des revenus quotidiens pour analyse

### Contraintes techniques
1. Performance: Le pipeline doit s'exécuter en moins de 15 minutes
2. Qualité: Tests de qualité des données à chaque étape
3. Modularité: Architecture permettant l'ajout facile de nouvelles sources/transformations
4. Maintenance: Documentation claire et tests automatisés

## Planification des tâches

1. **Configuration initiale**
   - Mise en place de l'environnement Docker
   - Configuration de PostgreSQL, Airflow et dbt

2. **Pipeline d'ingestion**
   - Développement du DAG d'ingestion quotidienne
   - Configuration des connecteurs PostgreSQL

3. **Modèles de transformation dbt**
   - Création du modèle staging (stg_sales)
   - Création du modèle analytique (fct_daily_revenue)

4. **Validation des données**
   - Configuration de Great Expectations
   - Implémentation des contrôles qualité

5. **Tests et déploiement**
   - Tests unitaires et d'intégration
   - Documentation finale

## Technologies et versions

- Python 3.9+
- Apache Airflow 2.5.0
- dbt-postgres 1.5.2
- Great Expectations 0.15+
- PostgreSQL 13 