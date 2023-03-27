from sample.models import ProjectModel
from sample.models import SampleAnalysisModel
from sample.models import *
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


class ProductModelSerializer(CustomModelSerializer):
    """
    Panel货号序列化器
    """

    class Meta:
        model = ProductModel
        fields = "__all__"


class ProductModelCreateUpdateSerializer(CustomModelSerializer):
    """
    Panel货号创建/更新时的列化器
    """

    class Meta:
        model = ProductModel
        fields = '__all__'


class SpeciesModelSerializer(CustomModelSerializer):
    """
    物种表序列化器
    """

    class Meta:
        model = SpeciesModel
        fields = "__all__"


class SpeciesModelCreateUpdateSerializer(CustomModelSerializer):
    """
    物种表创建/更新时的列化器
    """

    class Meta:
        model = SpeciesModel
        fields = '__all__'


class SampleModelSerializer(CustomModelSerializer):
    """
    样本序列化器
    """

    class Meta:
        model = SampleModel
        fields = "__all__"


class SampleModelCreateUpdateSerializer(CustomModelSerializer):
    """
    样本创建/更新时的列化器
    """

    class Meta:
        model = SampleModel
        fields = '__all__'