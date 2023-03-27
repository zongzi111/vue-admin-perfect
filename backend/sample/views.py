from sample.models import ProjectModel, SampleAnalysisModel
from sample.serializers import ProjectModelSerializer, ProjectModelCreateUpdateSerializer
from sample.serializers import SampleAnalysisModelSerializer, SampleAnalysisModelCreateUpdateSerializer
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