from typing import Dict, List


class ProductSalesMapper:
    def map(self, rows: List[Dict]) -> Dict:
        result = {}
        for row in rows:
            result[row.get('product_id')] = row.get('sales')

        return result