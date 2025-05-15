

/*
  Modèle d'agrégation des revenus quotidiens.
  Regroupe les montants totaux par jour et pays.
  Ce modèle est utile pour les analyses de tendances de ventes.
*/

WITH sales AS (
    SELECT * FROM "airflow_db"."public_staging"."stg_sales"
),

daily_totals AS (
    SELECT
        invoice_date_only AS date,
        country,
        COUNT(DISTINCT invoice_no) AS total_invoices,
        COUNT(DISTINCT customer_id) AS total_customers,
        SUM(quantity) AS total_quantity,
        SUM(total_amount) AS total_revenue
    FROM sales
    GROUP BY 
        invoice_date_only,
        country
),

-- Ajout de métadonnées pour l'analyse temporelle
enriched AS (
    SELECT
        date,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month,
        EXTRACT(DAY FROM date) AS day,
        EXTRACT(DOW FROM date) AS day_of_week,
        country,
        total_invoices,
        total_customers,
        total_quantity,
        total_revenue,
        total_revenue / NULLIF(total_quantity, 0) AS avg_price_per_item,
        total_revenue / NULLIF(total_invoices, 0) AS avg_revenue_per_invoice,
        total_revenue / NULLIF(total_customers, 0) AS avg_revenue_per_customer
    FROM daily_totals
)

SELECT * FROM enriched
ORDER BY date, country