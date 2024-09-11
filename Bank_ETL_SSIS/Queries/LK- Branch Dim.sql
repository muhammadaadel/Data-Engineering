SELECT [BranchId SK]
      ,[BranchId BK]

  FROM [Union Bank DWH].[dbo].[Branch Dim]
  WHERE [is_current]=1