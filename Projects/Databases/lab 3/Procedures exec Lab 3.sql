use [Auto Parking Management]
go
Create PROCEDURE getDatabaseToVersion
	@versionTo int
AS
BEGIN
	DECLARE @versionFrom int

	SET @versionFrom = (select V.currentVersion
							from DB_version V)

	DECLARE @query varchar(2000)

	IF @versionTo <= 7 AND @versionTo >=0
		IF @versionTo > @versionFrom
		BEGIN
			 WHILE @versionTo>@versionFrom
				BEGIN
					set @versionFrom = @versionFrom + 1
					set @query = 'do' + CAST(@versionFrom AS VARCHAR(5))
					exec @query
				END
		END
		ELSE  
		BEGIN 
			WHILE @versionTo<@versionFrom
				BEGIN
					IF @versionFrom!=0
					BEGIN
						set @query = 'undo' + CAST(@versionFrom AS VARCHAR(5))
						exec @query
					END
					set @versionFrom = @versionFrom - 1
				END
		END
		update DB_version 
		set currentVersion = @versionTo
END
go

exec getDatabaseToVersion  4;