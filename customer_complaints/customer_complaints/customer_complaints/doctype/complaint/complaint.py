# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Complaint(Document):
	

	def after_insert(self):
		item = [i for i in self.selected_item.split(',') if i]	
		for i in item:
			self.append('items', {'item': i})
		self.save()
