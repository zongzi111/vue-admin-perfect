from sample.models import *
from sample.serializers import *
from dvadmin.utils.viewset import CustomModelViewSet


class ProjectModelViewSet(CustomModelViewSet):
    """
    项目管理
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer
    create_serializer_class = ProjectModelCreateUpdateSerializer
    update_serializer_class = ProjectModelCreateUpdateSerializer
    filter_fields = ['project']
    search_fields = ['project']


class SampleAnalysisModelViewSet(CustomModelViewSet):
    """
    样本分析管理
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = SampleAnalysisModel.objects.all()
    serializer_class = SampleAnalysisModelSerializer
    create_serializer_class = SampleAnalysisModelCreateUpdateSerializer
    update_serializer_class = SampleAnalysisModelCreateUpdateSerializer
    filter_fields = ['name']
    search_fields = ['name']


class ProductModelViewSet(CustomModelViewSet):
    """
    Panel货号管理
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    create_serializer_class = ProductModelCreateUpdateSerializer
    update_serializer_class = ProductModelCreateUpdateSerializer
    filter_fields = ['product']
    search_fields = ['product']


class SpeciesModelViewSet(CustomModelViewSet):
    """
    物种表管理
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = SpeciesModel.objects.all()
    serializer_class = SpeciesModelSerializer
    create_serializer_class = SpeciesModelCreateUpdateSerializer
    update_serializer_class = SpeciesModelCreateUpdateSerializer
    filter_fields = ['name']
    search_fields = ['name']