import frappe


# filter sales invoice item 
@frappe.whitelist()
def filter_items(customer, sales_invoice):
    query = f'SELECT SII.item_code FROM `tabSales Invoice Item` SII INNER JOIN `tabSales Invoice` SI ON SII.parent=SI.name WHERE SI.customer="{customer}" AND SII.parent = "{sales_invoice}"'
    data = frappe.db.sql(query, as_list=True)
    return data

# filter sales invoice
@frappe.whitelist()
def filter_sales_invoice(customer):
    query = f'SELECT name FROM `tabSales Invoice` WHERE customer="{customer}"'
    data = frappe.db.sql(query, as_list=True)
    return data
