create table T_KNTI_DTL	(
	 SYN_CD				char(6) NOT NULL
	,KNTI_DT			date NOT NULL
	,PJ_NO				varchar(8) NOT NULL
	,WRK_ST_TIME		datetime
	,WRK_ED_TIME		datetime
	,ACT_HRS			DECIMAL(3, 1)
	,RST_HRS			DECIMAL(3, 1)
	,MDNGHT_WRK_HRS		DECIMAL(3, 1)
	,NN_RGLR_WRK_HRS	DECIMAL(3, 1)
	,PRIMARY KEY(SYN_CD, KNTI_DT, PJ_NO)
)
