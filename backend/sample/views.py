from sample.models import ProjectModel
from sample.serializers import ProjectModelSerializer, ProjectModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class ProjectModelViewSet(CustomModelViewSet):
    """
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