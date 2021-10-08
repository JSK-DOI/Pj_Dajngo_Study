create table M_CLNDR	(
	 CLNDR_DT		date  NOT NULL
	,PJ_NO			varchar(8) NOT NULL
	,WRK_DT_KBN		char(2)
	,PRIMARY KEY(CLNDR_DT, PJ_NO)
)
;
