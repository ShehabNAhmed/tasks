{

    'name': 'Task ',
    'version': '1.0.0',
    'author': 'mohamed',
    'sequence': -150,
    'website': 'www.proengmht.com',
    'category': 'Test to hirring',
    'summary': '',
    'description': """Test to hirring""",
    'demo': [],
    'depends': ['sale','base','purchase'],
    'data': [
        "security/ir.model.access.csv",
        # "views/task.xml",
        "views/project_inherit.xml",
             ],
    # 'installable': True,"views/purchase_request.xml"
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',

}
