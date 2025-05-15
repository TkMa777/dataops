# DataOps avec Airflow et PostgreSQL

## Description
Ce projet configure un environnement de DataOps basé sur Apache Airflow et PostgreSQL. Il est conçu pour orchestrer et automatiser les workflows de données.

## Prérequis
- Docker
- Docker Compose

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
- `dags/` : Répertoire contenant les DAGs Airflow
- `logs/` : Répertoire pour les fichiers de logs
- `plugins/` : Répertoire pour les plugins personnalisés d'Airflow
- `docker-compose.yml` : Configuration des services Docker

## DAG de test
Un DAG de test (`test_dag.py`) est inclus pour vérifier :
- Le bon fonctionnement d'Airflow
- La connexion à PostgreSQL
- Les opérations CRUD de base

Pour exécuter le DAG de test :
1. Accéder à l'interface web d'Airflow
2. Activer le DAG "test_dag"
3. Déclencher manuellement une exécution ou attendre l'exécution planifiée

## Dépannage
- Si les conteneurs ne démarrent pas correctement, vérifier les logs :
  ```bash
  docker-compose logs
  ```
- Pour redémarrer tous les services :
  ```bash
  docker-compose down
  docker-compose up -d
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