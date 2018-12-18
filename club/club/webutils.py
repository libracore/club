# -*- coding: utf-8 -*-
# Copyright (c) 2018, libracore (https://www.libracore.com) and contributors
# For license information, please see license.txt
import frappe

@frappe.whitelist(allow_guest=True)
def get_next_date(event_type="Spieltag"):
    sql_query = """SELECT
                  `subject`, `starts_on`, `ends_on`
                FROM `tabEvent`
                WHERE
                  `event_type` = "{event_type}"
                  AND `starts_on` >= CURDATE()
                ORDER BY `starts_on` ASC
                LIMIT 1;""".format(event_type=event_type)
    next_date = frappe.db.sql(sql_query, as_dict=True)
    return next_date
