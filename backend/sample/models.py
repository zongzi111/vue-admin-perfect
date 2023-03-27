from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel


class ProjectModel(CoreModel):
    '''
    项目表
    '''
    name = models.CharField(max_length=255, verbose_name='项目名称')
    project = models.CharField(max_length=255, verbose_name='项目号')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "projects"
        verbose_name = '项目表'
        verbose_name_plural = verbose_name
        ordering = ('-id',)


class SampleAnalysisModel(CoreModel):
    '''
    样本分析表
    '''
    name = models.CharField(max_length=255, verbose_name='样本分析')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "sample-analysis"
        verbose_name = '样本分析表'
        verbose_name_plural = verbose_name
        ordering = ('-id',)


class BatchModel(CoreModel):
    '''
    分析批次表
    '''
    batch = models.CharField(max_length=255, verbose_name='分析批号')
    sampleanalysis = models.ForeignKey(SampleAnalysisModel, on_delete=models.PROTECT, verbose_name='样本分析表')

    def __str__(self):
        return self.batch

    class Meta:
        db_table = "batches"
        verbose_name = '分析批次表'
        verbose_name_plural = verbose_name
        ordering = ('-id',)


class ProductModel(CoreModel):
    '''
    Panel货号表
    '''
    product = models.CharField(max_length=255, verbose_name='货号')

    def __str__(self):
        return self.product

    class Meta:
        db_table = "products"
        verbose_name = 'Panel货号表'
        verbose_name_plural = verbose_name
        ordering = ('-id',)


class SpeciesModel(CoreModel):
    '''
    物种表
    '''
    name = models.CharField(max_length=255, verbose_name='物种名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "species"
        verbose_name = '物种表'
        verbose_name_plural = verbose_name
        ordering = ('-id',)


class SampleModel(CoreModel):
    '''
    样本表
    '''
    no = models.CharField(max_length=255, verbose_name='样本编号', unique=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.PROTECT ,verbose_name='项目号')
    paired_sample = models.ForeignKey("SampleModel", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="配对样本")
    batch = models.ForeignKey(BatchModel, on_delete=models.PROTECT ,verbose_name='分析批次')
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT ,verbose_name='Panel货号')
    SAMPLE_TYPE = (
        (0, "TIS"),
        (1, "FFPE"),
        (2, "PLA"),
        (3, "WBC"),
        (4, "唾液"),
        (5, "拭子"),
        (6, "尿液"),
        (7, "标准品"),
    )
    sample_type = models.IntegerField(choices=SAMPLE_TYPE, default=0, null=True, blank=True, verbose_name="样本类型", help_text="样本类型")
    species = models.ForeignKey(SpeciesModel, on_delete=models.PROTECT ,verbose_name='物种')
    SEQ_SOURCE = (
        (0,"自测"),
        (1,"外部测序"),
    )
    seq_source = models.IntegerField(choices=SEQ_SOURCE, default=0, null=True, blank=True, verbose_name="测序来源", help_text="测序来源")
    run_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='Run编号')
    external_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='订单编号')

    
    @property
    def seq_id(self):
        if self.seq_source == 0:
            return self.run_id
        else:
            return self.external_id
        
    def __str__(self):
        return self.no

    class Meta:
        db_table = "sample"
        verbose_name = '样本表'
        verbose_name_plural = verbose_name
        ordering = ('-id',)