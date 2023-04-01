from . import __version__ as app_version

app_name = "customer_complaints"
app_title = "Customer Complaints"
app_publisher = "Deepak Kumar"
app_description = "Customer Complaints of Items"
app_email = "deepakkumar.it20@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customer_complaints/css/customer_complaints.css"
# app_include_js = "/assets/customer_complaints/js/customer_complaints.js"

# include js, css files in header of web template
# web_include_css = "/assets/customer_complaints/css/customer_complaints.css"
# web_include_js = "/assets/customer_complaints/js/customer_complaints.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "customer_complaints/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "customer_complaints.utils.jinja_methods",
#	"filters": "customer_complaints.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "customer_complaints.install.before_install"
# after_install = "customer_complaints.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "customer_complaints.uninstall.before_uninstall"
# after_uninstall = "customer_complaints.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customer_complaints.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"customer_complaints.tasks.all"
#	],
#	"daily": [
#		"customer_complaints.tasks.daily"
#	],
#	"hourly": [
#		"customer_complaints.tasks.hourly"
#	],
#	"weekly": [
#		"customer_complaints.tasks.weekly"
#	],
#	"monthly": [
#		"customer_complaints.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "customer_complaints.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "customer_complaints.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "customer_complaints.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"customer_complaints.auth.validate"
# ]
