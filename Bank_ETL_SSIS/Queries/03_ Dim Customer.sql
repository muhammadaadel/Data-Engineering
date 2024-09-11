SELECT c.[Customer_ID]
      ,c.[First Name]
      ,c.[Last Name]
      ,c.[Email]
      ,c.[State]
      ,c.[Age]
      ,c.[Gender]
      ,c.[BD]
	  ,c_ph.[Mobile Number]

  FROM [Union_Bank].[dbo].[Customer] c
  LEFT JOIN 
	   [Union_Bank].[dbo].[Customer_Phones] c_ph
	   ON
	   c.[Customer_ID] = c_ph.[Customer_ID]

