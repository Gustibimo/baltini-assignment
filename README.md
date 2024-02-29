## Baltini Assignment

### Answer #1:
- Please have a look into `src` folder, run the application with:

```
$ pip install -r requirements.txt
$ python src/main.py
```

There are two files that responsible to do 2 different tasks:

1. `get_duplicates.py` to find duplicate data, not really efficient because I rely on SQL query. Improvement tips: use Pandas to process the data, or pySpark
2. `merge_duplicates.py` to merge the duplicate products into one single unique
product.

### Answer #2:

- query to retrieve merge suggestion data:

```sql
SELECT pd.title AS "Group Title", COUNT(*) AS Count, MIN(pd.created_at) AS Created_at
FROM product_duplicates AS pd
INNER JOIN product_duplicate_lists AS pdl ON pd.id = pdl.product_duplicate_id
GROUP BY pd.title
HAVING COUNT(*) > 1
ORDER BY "Group Title";
```

- added index to enhanced query speed:
```
CREATE INDEX pd_title_idx ON product_duplicates (title);
```



