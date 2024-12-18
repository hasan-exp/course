{
    'name' : "Hospital System",
    "summary" : "Testing Odoo Tehnical",
    "author" : "Expert Co",
    "discription" : "test odoo with hospital case study",
    "depends" : ["base", "hr", "account", "website"],
    "data" : [
        "security/hospital_groups.xml",
        "security/ir.model.access.csv",
        "views/hospital_view.xml",
        "wizard/wiz_view.xml",
        "report/hospital_report_template.xml",
        "report/report_action.xml",
        "data/hospital_data.xml",
        "views/portal.xml",
    ],
    "application" : True
}