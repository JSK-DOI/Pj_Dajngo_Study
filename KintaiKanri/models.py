# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse_lazy


class MClndr(models.Model):
    clndr_dt = models.DateField(db_column='CLNDR_DT', primary_key=True)  # Field name made lowercase.
    pj_no = models.CharField(db_column='PJ_NO', max_length=8)  # Field name made lowercase.
    wrk_dt_kbn = models.CharField(db_column='WRK_DT_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_clndr'
        unique_together = (('clndr_dt', 'pj_no'),)


class MPjKnr(models.Model):
    pj_no = models.CharField(db_column='PJ_NO', primary_key=True, max_length=8)  # Field name made lowercase.
    pj_nm = models.CharField(db_column='PJ_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pj_st_time = models.TimeField(db_column='PJ_ST_TIME', blank=True, null=True)  # Field name made lowercase.
    rst_st_time = models.TimeField(db_column='RST_ST_TIME', blank=True, null=True)  # Field name made lowercase.
    rst_ed_time = models.TimeField(db_column='RST_ED_TIME', blank=True, null=True)  # Field name made lowercase.
    pj_ed_time = models.TimeField(db_column='PJ_ED_TIME', blank=True, null=True)  # Field name made lowercase.
    act_hrs = models.DecimalField(db_column='ACT_HRS', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_pj_knr'

    def get_absolute_url(self): 
        return reverse_lazy("PjKanriView") #CRUD時の戻り先指定


class MPjSzk(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', primary_key=True, max_length=6)  # Field name made lowercase.
    pj_kbn = models.CharField(db_column='PJ_KBN', max_length=2)  # Field name made lowercase.
    pj_no = models.CharField(db_column='PJ_NO', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_pj_szk'
        unique_together = (('syn_cd', 'pj_kbn'),)


class MUsr(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', primary_key=True, max_length=6)  # Field name made lowercase.
    syn_nm_s_kj = models.CharField(db_column='SYN_NM_S_KJ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    syn_nm_n_kj = models.CharField(db_column='SYN_NM_N_KJ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    syn_nm_s_kn = models.CharField(db_column='SYN_NM_S_KN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    syn_nm_n_kn = models.CharField(db_column='SYN_NM_N_KN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nysy_dt = models.DateField(db_column='NYSY_DT', blank=True, null=True)  # Field name made lowercase.
    pj_add_dt = models.DateField(db_column='PJ_ADD_DT', blank=True, null=True)  # Field name made lowercase.
    pj_del_dt = models.DateField(db_column='PJ_DEL_DT', blank=True, null=True)  # Field name made lowercase.
    e_mail_adr = models.CharField(db_column='E_MAIL_ADR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    syn_kngn = models.CharField(db_column='SYN_KNGN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lgn_pss = models.CharField(db_column='LGN_PSS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    syn_kbn = models.CharField(db_column='SYN_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_usr'
        
    def get_absolute_url(self): 
        return reverse_lazy("muserlist") # "戻る"のリダイレクト先


class TKnti(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', primary_key=True, max_length=6)  # Field name made lowercase.
    knti_dt = models.DateField(db_column='KNTI_DT')  # Field name made lowercase.
    ido_kbn = models.CharField(db_column='IDO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmrks = models.CharField(db_column='RMRKS', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_knti'
        unique_together = (('syn_cd', 'knti_dt'),)


class TKntiDtl(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', primary_key=True, max_length=6)  # Field name made lowercase.
    knti_dt = models.DateField(db_column='KNTI_DT')  # Field name made lowercase.
    pj_no = models.CharField(db_column='PJ_NO', max_length=8)  # Field name made lowercase.
    wrk_st_time = models.TimeField(db_column='WRK_ST_TIME', blank=True, null=True)  # Field name made lowercase.
    wrk_ed_time = models.TimeField(db_column='WRK_ED_TIME', blank=True, null=True)  # Field name made lowercase.
    act_hrs = models.DecimalField(db_column='ACT_HRS', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    rst_hrs = models.DecimalField(db_column='RST_HRS', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    mdnght_wrk_hrs = models.DecimalField(db_column='MDNGHT_WRK_HRS', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    nn_rglr_wrk_hrs = models.DecimalField(db_column='NN_RGLR_WRK_HRS', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_knti_dtl'
        unique_together = (('syn_cd', 'knti_dt', 'pj_no'),)
    
    def get_absolute_url(self):
        return reverse_lazy("index")
