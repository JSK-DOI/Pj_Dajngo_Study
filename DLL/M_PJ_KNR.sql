create table M_PJ_KNR   (
	 PJ_NO   		varchar(8) NOT NULL
	,PJ_NM  		varchar(100)
	,PJ_ST_TIME 	time
	,RST_ST_TIME    time
	,RST_ED_TIME    time
	,PJ_ED_TIME 	time
	,ACT_HRS    	decimal(3, 1)
	,PRIMARY KEY(PJ_NO)
)
;
