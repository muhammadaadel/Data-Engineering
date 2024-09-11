SELECT tr.[TransactionId]
      ,tr.[TransactionTypeId]
      ,tr.[Amount]
      ,tr.[TransactionDate]
      ,tr.[Account Number]
      ,tr.[ATM ID]
	  ,c.[CardNumber]
  FROM [Union_Bank].[dbo].[transactions_ATM_Account] tr
  INNER JOIN 
	   [Union_Bank].[dbo].[Account] acc
	   ON
	   tr.[Account Number] = acc.[Account Number]
  INNER JOIN 
	   [Union_Bank].[dbo].[Card] c
	   ON
	   acc.[Account Number] = c.Account_Number
