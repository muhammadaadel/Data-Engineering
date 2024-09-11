SELECT [ATM ID SK]
      ,[ATM ID BK]

  FROM [Union Bank DWH].[dbo].[ATM Dim]
  WHERE [is_current]=1
