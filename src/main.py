from multiprocessing import Pool

from task.get_duplicate import fetch_products_duplicate, group_products
from task.merge_duplicate import generate_merge_suggestions

if __name__ == '__main__':
    generate_merge_suggestions()
