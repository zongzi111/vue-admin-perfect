import { request } from "@/api/service";
import { BUTTON_STATUS_NUMBER } from "@/config/button";
import { urlPrefix as bookPrefix } from "./api";


export const crudOptions = vm => {
    return {
        pageOptions: {
            compact: true
        },
        options: {
            tableType: "vxe-table",
            rowKey: true, // 必须设置，true or false
            rowId: "id",
            height: "100%", // 表格高度100%, 使用toolbar必须设置
            highlightCurrentRow: false
        },
        
        rowHandle: {
            width: 140,
            view: {
                thin: true,
                text: "",
                disabled() {
                    return !vm.hasPermissions("Retrieve");
                }
            },
            edit: {
                thin: true,
                text: "",
                disabled() {
                    return !vm.hasPermissions("Update");
                }
            },
            remove: {
                thin: true,
                text: "",
                disabled() {
                    return !vm.hasPermissions("Delete");
                }
            }
        },
        // indexRow: {
        //     // 或者直接传true,不显示title，不居中
        //     title: "序号",
        //     align: "center",
        //     width: 100
        // },
        viewOptions: {
            componentType: "form"
        },
        formOptions: {
            defaultSpan: 24, // 默认的表单 span
            width: "35%"
        },
        columns: [{
                title: "ID",
                key: "id",
                show: false,
                disabled: true,
                width: 90,
                form: {
                    disabled: true
                }
            },
            {
                title: "样本编号",
                key: "no",
                sortable: true,
                treeNode: true,

                type: "input",
                form: {
                    rules: [
                        // 表单校验规则
                        { required: true, message: "样本号必填" },
                        {
                            pattern: /^(Lib)(SH|NB)(\d{2}CDx\d{3})(D|M|S)(\d{3})(A|B|C)(T|F|P|W|L|B|U|S)$/,
                            message: "样本号有误"
                          },
                    ],
                    component: {
                        props: {
                            clearable: true
                        },
                        placeholder: "请输入项目"
                    },
                    itemProps: {
                        class: { yxtInput: true }
                    }
                }
            },
            {
                title: "项目号",
                key: "project",
                search: {
                    disabled: false,
                    search: {
                      url: '/api/project/',
                      queryKey: 'name',
                      targetKey: 'project',
                      label: 'name',
                    },
                  },
                sortable: true,
                type: "select",
                dict: {
                    cache: true,
                    isTree: false,
                    url: '/api/project/',
                    value: 'id',
                    label: 'project'
                  },
                form: {
                    rules: [
                        // 表单校验规则
                        { required: true, message: "项目号必填" }
                    ],
                    component: {
                        props: {
                            clearable: true,
                            filterable: true,
                        },
                        placeholder: "请输入项目号"
                    },
                    itemProps: {
                        class: { yxtInput: true }
                    }
                },
            },
            {
                title: "配对样本",
                key: "paired_sample",
                sortable: true,
                type: "select",
                dict: {
                    cache: true,
                    isTree: false,
                    url: '/api/sample/',
                    value: 'id',
                    label: 'no'
                  },
                form: {
                    component: {
                        props: {
                            clearable: true,
                            filterable: true,
                        },
                        placeholder: "请输入配对样本"
                    },
                    itemProps: {
                        class: { yxtInput: true }
                    }
                },
            },
            {
                title: "Panel货号",
                key: "product",
                sortable: true,
                type: "select",
                dict: {
                    cache: true,
                    isTree: false,
                    url: '/api/product/',
                    value: 'id',
                    label: 'product'
                  },
                form: {
                    component: {
                        props: {
                            clearable: true,
                            filterable: true,
                        },
                        placeholder: "Panel货号"
                    },
                    itemProps: {
                        class: { yxtInput: true }
                    }
                },
            },
            {
                title: '样本类型',
                key: 'sample_type',
                type: 'select',
                width: 70,
                dict: {
                  data: vm.dictionary('SAMPLE_TYPE')
                },
                form: {
                  value: 1,
                  component: {
                    span: 12
                  }
                },
                component: { props: { color: 'auto' } } // 自动染色
              },
              {
                title: "物种",
                key: "species",
                sortable: true,
                type: "select",
                dict: {
                    cache: true,
                    isTree: false,
                    url: '/api/species/',
                    value: 'id',
                    label: 'name'
                  },
                form: {
                    component: {
                        props: {
                            clearable: true,
                            filterable: true,
                        },
                        placeholder: "物种"
                    },
                    itemProps: {
                        class: { yxtInput: true }
                    }
                },
            },
            {
                title: '测序来源',
                key: 'seq_source',
                type: 'select',
                width: 70,
                dict: {
                  data: vm.dictionary('SEQ_SOURCE')
                },
                form: {
                  value: 1,
                  component: {
                    span: 12
                  }
                },
                component: { props: { color: 'auto' } } // 自动染色
              },
              {
                title: '测序编号',
                key: 'seq_id',
                minWidth: 110,
                type: 'input',
                form: {
                  itemProps: {
                    class: { yxtInput: true }
                  },
                  component: {
                    placeholder: '测序编号'
                  }
                }
              },
              {
                title: 'run编号',
                key: 'run_id',
                minWidth: 110,
                type: 'input',
                form: {
                  itemProps: {
                    class: { yxtInput: true }
                  },
                  component: {
                    placeholder: 'run编号'
                  }
                }
              },
        ].concat(vm.commonEndColumns())
    };
};
