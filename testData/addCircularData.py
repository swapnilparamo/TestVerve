from datetime import datetime


def getAddCircularDataTc3():
    add_circular_data_tc3 = {"title": "add internal circular" + datetime.now().strftime("%Y-%m-%d"),
                             "announcement_type": "CIRCULAR",
                             "circular_no": "add internal circular" + datetime.now().strftime("%Y-%m-%d"),
                             "circular_issue_date": str(int(datetime.now().day) - 3),
                             "internal_circular_value": "Internal Circular",
                             "internal_sub_type_value": "IT",
                             "description": "add internal circular" + datetime.now().strftime("%Y-%m-%d"),
                             "shared_value": "RESTRICTED",
                             "department_value": ["AL", "BEM"],
                             "location_value": ["AMRITSAR", "BHOPAL"],
                             "date_restriction": "Yes",
                             "expiry_date_year_header": str(2026),
                             "expiry_date_month": "Jun",
                             "expiry_date": str(10),
                             "attach_file_value": "Yes",
                             }
    return add_circular_data_tc3


def getAddCircularDataTc4():
    add_circular_data_tc4 = {"title": "add internal circular" + datetime.now().strftime("%Y-%m-%d"),
                             "announcement_type": "CIRCULAR",
                             "circular_no": "add internal circular" + datetime.now().strftime("%Y-%m-%d"),
                             "circular_issue_date": str(int(datetime.now().day) - 3),
                             "internal_circular_value": "Internal Circular",
                             "external_circular_value": "External Circular",}
    return add_circular_data_tc4
