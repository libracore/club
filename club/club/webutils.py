# -*- coding: utf-8 -*-
# Copyright (c) 2018, libracore (https://www.libracore.com) and contributors
# For license information, please see license.txt

@frappe.whitelist(allow_guest=True)
def get_next_date():
    sql_query = """SELECT
                  `starts_on`
                FROM `tabEvent`
                WHERE
                  `event_type` = "Spieltag"
                  AND `starts_on` > CURDATE()
                ORDER BY `starts_on` ASC
                LIMIT 1;"""
    next_date = frappe.db.sql(sql_query, as_dict=True)
    return next_date
