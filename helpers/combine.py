"""
SandCMS - Content Management System (Product & Blogging) for Rapid website development
Website: www.sandcms.com
Author: S. Jangra & Mark A.R. Pequeras
"""

keys = {
        "orders" : ['id','fulfilled','customer_name', 'customer_email', 'amount_total', 'created', 'payment_status', 'customer_country', 'customer_postal', 'currency', 'items', 'session_id', 'notes','tracking','metadata', 'address', 'phone', 'shipping_cost','history','ordernumber','additional']
        }

def zipper(key: str,combinewith: list) -> dict:
    return dict(zip(keys[key],combinewith))

		
	
	

        

    