frappe.ready(function() {
	// bind events here

	//default status
	frappe.web_form.set_value('status','New')
	
	if (frappe.web_form.doc.name) {
		frappe.web_form.set_df_property('items', 'hidden', 0)
	}
	// if customer change clear the sales invoice and Item checkbox html
	// also filter the sales invoice
	frappe.web_form.on('customer', (field, value) => {
		// clear items field
		frappe.web_form.set_value('selected_item','')
		// clear sales invoice
		frappe.web_form.set_value('sales_invoice','')

		customer = value
		frappe.call({
			method: "customer_complaints.utils.filter_sales_invoice",
			args: {
				customer: customer
			},
			callback: function(r) {
				let options = []
				for (var i = 0; i < r.message.length; i++) {
					options.push({
						'label': r.message[i][0],
						'value': r.message[i][0]
						});
					let sales_invoice = frappe.web_form.get_field("sales_invoice");
					sales_invoice._data = options;
					sales_invoice.refresh();
				}
			}
		})
	});

	// when sales invoice selected show item checkbox
	frappe.web_form.on('sales_invoice', (field, value) => {
		customer = frappe.web_form.get_value('customer')
		sales_invoice = value

		filter_items(customer, sales_invoice)
	});
	
	function filter_items(customer, sales_invoice) {
		frappe.call({
			method: "customer_complaints.utils.filter_items",
			args: {
				customer: customer,
				sales_invoice: sales_invoice
			},
			callback: function(r) {
	
				let table = `<table id="mytable"> <tr>
					<th>Item</th>
					<th>Checkbox</th>
				</tr>`
				for (var i = 0; i < r.message.length; i++) {
					table += `
					<tr>
					  <td>${r.message[i][0]}</td>
					  <td><input class= "checkitem" type="checkbox" name= "${r.message[i][0]}" value="${r.message[i][0]}"></td>
					</tr>`
				}
				table += `</table>`

				$('#html_item').html(table)

				// 
				$(".checkitem").click(function(){
				  if ($(this).is(":checked"))
				  {
					let prev = frappe.web_form.get_value('selected_item')
					if (prev) {
						let v = prev +','+ $(this).val()
						frappe.web_form.set_value('selected_item',v) 
					} else {
						frappe.web_form.set_value('selected_item',$(this).val())
					}
				  } else {
					let val = frappe.web_form.get_value('selected_item')
					frappe.web_form.set_value('selected_item',val.replace($(this).val(),''))
				  }
				});
			}
		});
	}
});