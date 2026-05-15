import os
from  openpyxl  import Workbook 
from config import (
    work_book_name
)





print("welcome to hostel mess")

#check for workbook in the system .
workbook_status=False
if not os.path.exists(work_book_name):
    confirm=input("if you want create a workbook yes,no : y/n ,press enter to create by default").lower() or "y"
    if confirm == "y":
        wb=Workbook()
        wb_name=str(input(f"enter work book name press enter for default name: {work_book_name}")) or (work_book_name)
        if wb_name==work_book_name:
             wb.save(wb_name)
        else:
            wb_name+=".xlsx"
            wb.save(wb_name)
            work_book_name=wb_name
        workbook_status=True
    
    else:
        print("need a work book for work")

else:
    workbook_status=True
    
if workbook_status:
    print("main menu")
       
    


