SELECT [CardNumber Sk]
      ,[CardNumber Bk]

  FROM [Union Bank DWH].[dbo].[Card Dim]
  WHERE [is_current]=1
