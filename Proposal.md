# __GROUP:__ AngryTiger
1.	Andhika Adiel Insani
2.	Muhammad Lutfil Hadi Bin Mohd Rothi
3.	Ahmad Khairulanam Bin Che Mat

# __TITLE:__ Medicine Management 

# OVERVIEW
This project is used mainly for storing medicine to maintain the details of medicine such as stock, price, date check-in and check-out and the details. This medicine management software is design for ease the work load of employers in the medical shop, pharmacy and hospital. The main features of this software is includes the inventory, stock control, accounting and client details. This software can used by a wide variety of outlets such as retailers and wholesaler to automate the process of manually maintaining the record related to subject of maintaining the stock and cash flows. This project is basically updating the manual chemist inventory system to automated inventory system, so that organization can mange their record in efficient and organized form.
# CLASS DIAGRAM
## CLASSES
1.  USER : Manage all the operation in the system
2.  SELLS : Manage the operation that related to sell
3.  MEDICINE : Manage the operation that related to medicine
4.  STOCK : Manage the operation that related to medicine stock
5.  BILING INFO : Manage the operation that related to bill
## ATTRIBUTES
1.  USER :
  * Username
  * userID
  * userPassword
2.  SELLS : 
  * sellID
  * sellDesc
  * sellName
  * sellDate
3.  MEDICINE  :
  * MediName
  * MediID
  * MediDateIn
  * MediExpiredDate
4.  STOCK : 
  * stockID
  * stockNum
  * stockType
  * stockDes
  * stockDatein
5.  BILING INFO :
  * billNumber
  * billName
  * billDate

## METHOD
1.  USER :
 * addUser()
 * editUser()
 * deleteUser()
 * searchUser()
2.  SELLS : 
 * addsell()
 * editsell()
 * deletesell()
 * searchsell()
3.  MEDICINE  :
 * addmedi()
 * editmedi()
 * deletemedi()
 * searchmedi()
4.  STOCK : 
 * addstock()
 * editstock()
 * deletestock()
 * searchstock()n
5.  BILING INFO :
 * addbillNumb()
 * editbillNumb()
 * deletebillNumb()
 * searchbillNumb()
## ATTRIBUTE
![attribute](https://drive.google.com/uc?export=view&id=1O-8RFe9mA8jzpxa-82pKVZRUSOK9Z0AC)

## DIAGRAM
![class diagram](https://drive.google.com/uc?export=view&id=1KlX1Qv8ARl_-0TsGYeBBBQqAu7HDDc7a)

## ERD DIAGRAM
![erd](https://drive.google.com/uc?export=view&id=1aVqEb1TM9lIaH2H3EbeC6PYaCmTJ9bzU)


