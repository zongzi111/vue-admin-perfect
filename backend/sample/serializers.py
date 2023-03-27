from sample.models import ProjectModel
from sample.models import SampleAnalysisModel
from dvadmin.utils.serializers import CustomModelSerializer


class ProjectModelSerializer(CustomModelSerializer):
    """
    项目管理序列化器
    """

    class Meta:
        model = ProjectModel
        fields = "__all__"


class ProjectModelCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理创建/更新时的列化器
    """

    class Meta:
        model = ProjectModel
        fields = '__all__'


class SampleAnalysisModelSerializer(CustomModelSerializer):
    """
    样本分析序列化器
    """

    class Meta:
        model = SampleAnalysisModel
        fields = "__all__"


class SampleAnalysisModelCreateUpdateSerializer(CustomModelSerializer):
    """
    样本分析创建/更新时的列化器
    """

    class Meta:
        model = SampleAnalysisModel
        fields = '__all__'