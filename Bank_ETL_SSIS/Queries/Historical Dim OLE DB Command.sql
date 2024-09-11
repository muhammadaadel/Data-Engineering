UPDATE [DB Name].[dbo].[Dim Name] 
	SET [end_date]=? ,
		[is_current]=0
WHERE
	[1st_BK]=? AND [2nd_BK]=? AND [nth_BK]=?
	AND [end_date] IS NULL
