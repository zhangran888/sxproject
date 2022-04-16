# 账号
class AcccountUtil():
    # 系统管理员账号、密码
    ACCOUNT = "ybj111"
    PASSWORD = "cDqq2Etr7Sv6Qjhz5QePhf2hqnbl+b25/ErY4x347fA35X3Dyt6Dsb00SkIdVN1Av+/G2swuB22l4HigVHPjaNrIfyD/cNHvITduWjbUNl8wYOphdg9l/eWJjrxJ/ngozG7Qd2rq3nJbGFfy9/ifQT+TTNahlMunkq1ewpdF7ZU="


# 接口管理
class ContUtil():
    # 通用ip+端口
    IP_PORT = 'http://172.18.1.40/'
    # 获取图形验证码
    VERIFYCODE_URL = IP_PORT + 'api/sso/user/verifyCode'
    # 获取ticket票据
    TICKET_URL = IP_PORT + 'api/sso/user/ticket'
    # 获取jwtToken进行登录
    JWTTOKEN_URL = IP_PORT + 'api/sso/user/login'
    # 退出登录
    LOGOUT_URL = IP_PORT + 'api/sso/user/logout'

    # 首页登录日志
    HOME_LOG = IP_PORT + 'api/openplatform/sysOperLog/selfLoglist'
    # 辖内机构数
    HOME_INSTITUTION_NUMBER = IP_PORT + 'api/openplatform/sysOrganization/organizationCount'
    # 本机构用户数
    HOME_LOACAL_INST_NUMBER = IP_PORT + 'api/openplatform/sysUser/countUser'
    # 当前用户基本信息
    HOME_USER_INFORMATION = IP_PORT + 'api/sso/user/getUserInfo'

    # 新增机构分类
    INSTITUTIONAL_ADD = IP_PORT + 'api/openplatform/sysOrganizationtType/addOrUpdate'
    # 修改机构分类
    INSTITUTIONAL_UPDATE = IP_PORT + 'api/openplatform/sysOrganizationtType/addOrUpdate'
    # 机构分类列表
    INSTITUTIONAL_LIST = IP_PORT + 'api/openplatform/sysOrganizationtType/list'
    # 删除机构分类
    INSTITUTIONAL_DELETE = IP_PORT + 'api/openplatform/sysOrganizationtType/deleteById'

    # 新增机构管理
    ORGANIZATIONAL_ADD = IP_PORT + 'api/openplatform/sysOrganization/addOrUpdate'
    # 修改机构管理
    ORGANIZATIONAL_UPDATE = IP_PORT + 'api/openplatform/sysOrganization/addOrUpdate'
    # 机构管理列表
    ORGANIZATIONAL_LIST = IP_PORT + 'api/openplatform/sysOrganization/list'

    # 新增零级机构
    ZERO_ADD = IP_PORT + 'api/openplatform/sysOrganization/addOrUpdateForRoot'
    # 修改零级机构
    ZERO_UPDATE = IP_PORT + 'api/openplatform/sysOrganization/addOrUpdateForRoot'
    # 零级机构配置列表
    ZERO_LIST = IP_PORT + 'api/openplatform/sysOrganization/pageForRoot'
    # 删除零级机构
    ZERO_DELETE = IP_PORT + 'api/openplatform/sysOrganization/deleteForRoot'

    # 新增机构产品权限
    AUTHORITY_ADD = IP_PORT + 'api/openplatform/sysOrganization/updatePlatform'
    # 修改机构产品权限
    AUTHORITY_UPDATE = IP_PORT + 'api/openplatform/sysOrganization/updatePlatform'
    # 机构产品权限列表
    AUTHORITY_LIST = IP_PORT + 'api/openplatform/sysOrganization/listForOrgPlatform'
    # 删除机构产品权限
    AUTHORITY_DELETE = IP_PORT + 'api/openplatform/sysOrganization/deletePlatform'

    # 新增角色
    ROLE_ADD = IP_PORT + 'api/openplatform/sysRole/addOrUpdate'
    # 修改角色
    ROLE_UPDATE = IP_PORT + 'api/openplatform/sysRole/addOrUpdate'
    # 角色管理列表
    ROLE_LIST = IP_PORT + 'api/openplatform/sysRole/list'
    # 删除角色
    ROLE_DELETE = IP_PORT + 'api/openplatform/sysRole/delete'

    # 新增用户
    ACCOUNT_ADD = IP_PORT + 'api/openplatform/sysUser/addOrUpdate'
    # 修改用户
    ACCOUNT_UPDATE = IP_PORT + 'api/openplatform/sysUser/addOrUpdate'
    # 重置密码
    ACCOUNT_RESET = IP_PORT + 'api/openplatform/sysUser/initPassword'
    # 停用用户
    ACCOUNT_DISABLE = IP_PORT + 'api/openplatform/sysUser/update/status'
    # 用户管理列表
    ACCOUNT_LIST = IP_PORT + 'api/openplatform/sysUser/list'

    # 新增菜单
    MENU_ADD = IP_PORT + 'api/openplatform/sysMenu/addOrUpdate'
    # 修改菜单
    MENU_UPDATE = IP_PORT + 'api/openplatform/sysMenu/addOrUpdate'
    # 菜单管理列表
    MENU_LIST = IP_PORT + 'api/openplatform/sysMenu/pageList'
    # 删除菜单
    MENU_DELETE = IP_PORT + 'api/openplatform/sysMenu/delete'
