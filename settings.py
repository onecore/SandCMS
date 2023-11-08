"""
SandCMS - Content Management System (Product & Blogging) for Rapid website development
Website: www.sandcms.com
Author: S. Jangra & Mark A.R. Pequeras
"""

# Templating & System variables
ks_badge_insert = "bg-secondary"  # Blog-list view / fn blog_list_badge_category
ks_admin_button = "bg-primary"   # Admin button / fn admin_button

# Dashboard route (URL)
route_dashboard = "/dashboard"

# File / Products
render_product_single = "product.html"
render_product_list = "product-list.html"

# File / Blogs
render_blog_single = "blog.html"
render_blog_list = "blog-list.html"

# Route (URL) Products
route_product = "/product"
route_product_list = "/product-list"

# Route (URL) Blogs
route_blog = "/blog"
route_blog_list = "/blog-list"


# Misc Settings / Variables below
cms_debug = False  
cms_version = "1.4"

# Email template paths for (Abandoned, Placed, Fulfilled) templates in .HTML form (Do not add Leading slash)
# email_templates = "templates/email"
# email_templates_write = ["fulfilled","placed"] # Do not change as its act as iterable and needs some other modification


# Orders
order_error_countries = ['CA','US']
order_payment_method = ['card']  # check stripe for list of avail. method
order_novariant_selected = "Available variants"  # override default value (when no variant selected) / Also needs an update on JS side


# Uploads
uploads_allowedext = set(['png', 'jpg', 'jpeg', 'gif', 'svg', 'ico'])  # Allowed File Extentions in uploader

# Database Path and File
dbase_path = "dbase/sand"


# Products
product_similar_load = 7 # try to pull similar in this count (if similar runs out it will pull random product)