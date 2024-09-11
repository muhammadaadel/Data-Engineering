SELECT [Transaction_Type_Id SK]
      ,[Transaction_Type_Id BK]

  FROM [Union Bank DWH].[dbo].[Transaction Type Dim]
  WHERE [is_current]=1
