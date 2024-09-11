SELECT c.Customer_ID,
	   c.[First Name],
       c.[Last Name],
       c.Email,
       c.State,
       c.Age,
       c.Gender,
	   c.BD,
	   cp.[Mobile Number]


FROM Customer as c
LEFT JOIN Customer_Phones as cp
ON c.Customer_ID = cp.Customer_ID;