SELECT Company_Data.Name, 
Company_Financials.ROCE,
Company_Financials.ROE, 
Company_Financials.Debt_Equity FROM Company_Data
INNER JOIN Company_Financials ON Company_Data.Name = Company_Financials.Name
WHERE Company_Financials.ROCE>30 and Company_Financials.Debt_Equity<1

SELECT Company_Data.Name, 
Company_Financials.ROCE,
Company_Financials.ROE, 
Valuations_Ratios.PE,
Valuations_Ratios.EV_EBITDA FROM Company_Data
INNER JOIN Company_Financials ON Company_Data.Name = Company_Financials.Name
INNER JOIN Valuations_Ratios ON Company_Data.Name = Valuations_Ratios.Name
WHERE Valuations_Ratios.PE<35

SELECT * from Valuations_Ratios

EXEC SP_RENAME 'Company_Financials','COS_FIN'
EXEC SP_RENAME 'Company_Data','COS_DATA'
EXEC SP_RENAME 'Valuations_Ratios','VALUE_RATIO'

EXEC sp_rename 'COS_DATA.Sales_growth', 'Sales_growth_3Y', 'COLUMN';
EXEC SP_RENAME 'COS_DATA.Profit_growth', 'Profit_growth_3Y', 'COLUMN';

SELECT COS_DATA.Name,
COS_DATA.Sales_growth_3Y, 
COS_DATA.Profit_growth_3Y,
COS_DATA.Net_profit_margin,
VALUE_RATIO.PB FROM COS_DATA
INNER JOIN VALUE_RATIO ON COS_DATA.Name = VALUE_RATIO.Name
WHERE COS_DATA.NAME LIKE '%Bank%' AND VALUE_RATIO.PB < 3

CREATE OR ALTER PROCEDURE AS_PER_PE
@PE INT
AS
BEGIN
	SELECT COS_DATA.Name, 
	COS_DATA.Sales_growth_3Y, 
	COS_DATA.Profit_growth_3Y, 
	VALUE_RATIO.PE, 
	VALUE_RATIO.EV_EBITDA FROM COS_DATA
	INNER JOIN VALUE_RATIO ON COS_DATA.Name = VALUE_RATIO.Name
	WHERE VALUE_RATIO.PE < @PE
END
EXEC AS_PER_PE @PE = 30

CREATE OR ALTER PROCEDURE BK_VAL_PB
@PB INT, @S_GROWTH DECIMAL(10,2), @P_GROWTH DECIMAL(10,2) 
AS
BEGIN
	SELECT COS_DATA.Name, 
	COS_DATA.Sales_growth_3Y, 
	COS_DATA.Profit_growth_3Y, 
	VALUE_RATIO.PB 
	FROM COS_DATA
	INNER JOIN VALUE_RATIO ON COS_DATA.Name = VALUE_RATIO.Name
	WHERE COS_DATA.Name LIKE '%Bank%' AND VALUE_RATIO.PB < @PB AND COS_DATA.Sales_growth_3Y > @S_GROWTH AND COS_DATA.Profit_growth_3Y > @P_GROWTH
END
EXEC BK_VAL_PB @PB = 3, @S_GROWTH = 15, @P_GROWTH = 10

CREATE OR ALTER PROCEDURE STCK_VAL_GRTH
@EVEBITDA DECIMAL(10,2),
@ROCE DECIMAL(10,2)
AS
BEGIN
	SELECT COS_FIN.Name,
	COS_FIN.ROCE,
	VALUE_RATIO.EV_EBITDA,
	COS_DATA.Sales_growth_3Y,
	COS_DATA.Profit_growth_3Y FROM COS_FIN
	INNER JOIN COS_DATA ON COS_FIN.Name = COS_DATA.Name
	INNER JOIN VALUE_RATIO ON COS_FIN.Name =VALUE_RATIO.Name
	WHERE VALUE_RATIO.EV_EBITDA >= @EVEBITDA AND COS_FIN.ROCE >= @ROCE
END
EXEC STCK_VAL_GRTH 25, 30