import pandas as pd
import xml.etree.ElementTree as et

class Xml_to_ExcelSheet:

    @staticmethod
    def xmldata_to_excel_sheet():
        tree = et.parse("E:\\NOP BO Automation\\dummy_code\\Test_Cust.xml")
        root = tree.getroot()
        myrows = []
        for items in root.iter():
            if items.tag == "Email":
                cust_email = items.text
            elif items.tag == "CompanyName":
                cust_company = items.text
            elif items.tag == "FirstName":
                cust_firstname = items.text
            elif items.tag == "LastName":
                cust_lastname = items.text
                myrows.append({"Email":cust_email, "Company Name":cust_company, "First Name":cust_firstname, "Last Name":cust_lastname})

        out_df = pd.DataFrame(myrows)
        out_df.to_excel("E:\\NOP BO Automation\\test_data\CustDetails.xlsx" , index=False)

















