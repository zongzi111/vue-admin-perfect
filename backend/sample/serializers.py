from sample.models import ProjectModel
from dvadmin.utils.serializers import CustomModelSerializer


class ProjectModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = ProjectModel
        fields = "__all__"


class ProjectModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = ProjectModel
        fields = '__all__'