-- SQL Business Case Studies
-- Business KPI query examples.

SELECT * FROM sample_data LIMIT 20;

SELECT domain, metric, SUM(value) AS total_value
FROM sample_data
GROUP BY domain, metric
ORDER BY total_value DESC;

SELECT dimension, SUM(value) AS total_value,
       RANK() OVER (ORDER BY SUM(value) DESC) AS value_rank
FROM sample_data
GROUP BY dimension;
