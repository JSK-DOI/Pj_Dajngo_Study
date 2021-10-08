create table T_KNTI	(
	 SYN_CD		char(6) NOT NULL
	,KNTI_DT	date NOT NULL
	,IDO_KBN	char(1)
	,RMRKS		varchar(100)
	,PRIMARY KEY(SYN_CD, KNTI_DT)	
)