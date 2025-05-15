# Pipeline DataOps : Ventes et Analyse

## Description
Ce projet implémente un pipeline DataOps complet pour l'ingestion, la transformation, la validation et l'analyse des données de ventes. Il utilise Apache Airflow pour l'orchestration, dbt pour la transformation des données, Great Expectations pour la validation de la qualité, et PostgreSQL comme base de données.

## Architecture
![Architecture DataOps](https://example.com/dataops-architecture.png)

L'architecture du pipeline comprend :
- **Ingestion** : Chargement quotidien automatique des données CSV
- **Validation** : Contrôle de qualité avec Great Expectations
- **Transformation** : Modèles dbt pour la standardisation et l'agrégation
- **Tests** : Tests unitaires et d'intégration
- **CI/CD** : Pipeline GitHub Actions pour le déploiement continu

## Prérequis
- Docker
- Docker Compose
- Git

## Installation et démarrage

1. Cloner le dépôt :
   ```bash
   git clone <repository-url>
   cd dataops
   ```

2. Lancer les services avec Docker Compose :
   ```bash
   docker-compose up -d
   ```

3. Vérifier que tous les conteneurs sont en cours d'exécution :
   ```bash
   docker ps
   ```

4. Accéder à l'interface web d'Airflow :
   - URL : http://localhost:8082
   - Identifiant : admin
   - Mot de passe : admin

## Structure du projet
```
dataops/
├── dags/                    # DAGs Airflow
│   └── sales_pipeline.py    # DAG principal
├── data/                    # Données source
│   └── sales.csv            # Données de ventes
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
│   └── great_expectations.yml  # Configuration principale
├── tests/                   # Tests unitaires et d'intégration
├── docker-compose.yml       # Configuration des services
└── README.md                # Documentation
```

## Utilisation du pipeline

### Démarrage du pipeline
Le pipeline est configuré pour s'exécuter automatiquement tous les jours. Pour déclencher une exécution manuelle :

1. Accéder à l'interface web d'Airflow (http://localhost:8082)
2. Activer le DAG "sales_pipeline"
3. Cliquer sur le bouton "Trigger DAG"

### Visualisation des résultats
Les données transformées sont disponibles dans la base de données PostgreSQL, dans les tables :
- `staging.stg_sales` - Données de ventes nettoyées
- `marts.fct_daily_revenue` - Agrégation des revenus quotidiens

### Exécution des tests
```bash
# Exécuter les tests unitaires
pytest -xvs

# Vérifier la qualité du code
black --check dags/
```

## Fonctionnalités principales

### 1. Pipeline d'ingestion
Le DAG Airflow `sales_pipeline.py` gère :
- L'ingestion quotidienne des données de ventes à partir d'un fichier CSV
- Le chargement des données dans PostgreSQL
- La validation de la qualité des données

### 2. Transformation avec dbt
Les modèles dbt transforment les données brutes en insights métier :
- `stg_sales` : Nettoyage et standardisation des données de ventes
- `fct_daily_revenue` : Agrégation des revenus par jour et par pays

### 3. Validation de la qualité avec Great Expectations
Great Expectations applique des contrôles de qualité rigoureux :
- Validation de l'intégrité des données (valeurs nulles, doublons)
- Vérification des types de données et des plages de valeurs
- Tests d'unicité pour les combinaisons de clés

### 4. CI/CD avec GitHub Actions
Le workflow GitHub Actions automatise :
- La validation des DAGs Airflow
- La compilation des modèles dbt
- Les tests unitaires et d'intégration
- Le packaging et le déploiement

## Dépannage
- Si les conteneurs ne démarrent pas correctement, vérifier les logs :
  ```bash
  docker-compose logs
  ```
- Pour les problèmes avec Airflow, consulter les logs dans l'interface web ou :
  ```bash
  docker-compose logs airflow-webserver
  ```
- Pour dbt, exécuter les commandes en mode debug :
  ```bash
  docker exec -it epsi_dataops-dbt-1 bash
  cd /usr/app
  dbt debug --profiles-dir profiles
  ```

## Arrêt des services
Pour arrêter tous les services :
```bash
docker-compose down
```

Pour arrêter les services et supprimer les volumes (supprime toutes les données) :
```bash
docker-compose down -v
```

## Contribution
1. Forker le projet
2. Créer une branche (`git checkout -b feature/nom-fonctionnalite`)
3. Commiter les changements (`git commit -m 'Ajout de la fonctionnalité X'`)
4. Pousser vers la branche (`git push origin feature/nom-fonctionnalite`)
5. Ouvrir une Pull Request

## Licence
Distribué sous licence MIT. Voir `LICENSE` pour plus d'informations.