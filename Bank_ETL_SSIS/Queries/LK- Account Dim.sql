SELECT [Account Number SK]
      ,[Account Number BK]

  FROM [Union Bank DWH].[dbo].[Account Dim]
  WHERE [is_current]=1
