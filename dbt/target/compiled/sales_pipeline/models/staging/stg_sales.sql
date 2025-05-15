

/*
  Modèle de staging pour les données de ventes
  Effectue les opérations suivantes:
  - Cast des types de données appropriés
  - Conversion des dates
  - Filtrage des valeurs nulles pour CustomerID et UnitPrice
  - Ajout d'une colonne d'identifiant unique
  - Calcul du montant total (Quantity * UnitPrice)
*/

WITH source AS (
    SELECT * FROM "airflow_db"."public"."raw_sales"
),

renamed AS (
    SELECT
        CAST("InvoiceNo" AS VARCHAR) AS invoice_no,
        CAST("StockCode" AS VARCHAR) AS stock_code,
        CAST("Description" AS VARCHAR) AS description,
        CAST("Quantity" AS INTEGER) AS quantity,
        CAST("InvoiceDate" AS TIMESTAMP) AS invoice_date,
        CAST("UnitPrice" AS DECIMAL(10, 2)) AS unit_price,
        CAST("CustomerID" AS VARCHAR) AS customer_id,
        CAST("Country" AS VARCHAR) AS country
    FROM source
),

transformed AS (
    SELECT
        invoice_no,
        stock_code,
        description,
        quantity,
        invoice_date,
        DATE(invoice_date) AS invoice_date_only,
        unit_price,
        customer_id,
        country,
        quantity * unit_price AS total_amount
    FROM renamed
    WHERE 
        unit_price > 0
        AND quantity > 0
),

indexed AS (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY invoice_no, stock_code, invoice_date) as row_idx,
        *
    FROM transformed
    WHERE customer_id IS NOT NULL
)

SELECT
    -- Création d'une clé unique en combinant invoice_no, stock_code et un index
    'SALE-' || invoice_no || '-' || stock_code || '-' || row_idx AS sale_id,
    invoice_no,
    stock_code,
    description,
    quantity,
    invoice_date,
    invoice_date_only,
    unit_price,
    customer_id,
    country,
    total_amount
FROM indexed