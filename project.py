# -*- encoding: utf-8 -*-

from openerp.osv import fields, osv, orm

class project_issue(osv.osv):
    _name = 'project.issue'
    _inherit = 'project.issue'
    _columns = {
        # 'category_id':fields.many2one('project.issue.category','Categoria'),
        'issue_category':fields.selection(
            (('1','Velocidad'),('2','Incidencia'),('3','Desarrollo'),
             ('4','Capacitacion'),('5','Proceso'),('6','Control de acceso'),
             ),'Categoria'),
        'company_id':fields.many2one('res.company','Sucursal', required=True),
        'priority':fields.selection(
            (('1','Urgente'),
             ('2','Media'),('3','Baja'),
             ),'Prioridad', help="URGENTE: Detiene operación o causa retrabajos MEDIA: todas BAJA: mejoras, cambios en diseño, formato, campos adicionales, etc."),
        'deadline':fields.date('Fecha compromiso'),
        'notes':fields.text('Incidencia'),
        'solution':fields.text('Solucion'),
        'company_id': fields.selection(
            (('CEDIS','CEDIS'),('TYP_HMO','Hermosillo'),('TYP_OBG','Obregon'),
             ('TYP_CLN','Culiacan'),('TYP_GDL','Guadalajara'),('TYP_LPZ','La Paz'),
             ('TYP_LMS','Los Mochis'),('TYP_MXL','Mexicali'),('TYP_NGZ','Nogales'),
             ('TYP_TJ','Tijuana')),'Envio a Tienda:'),
    }

# class project_issue_category(osv.osv):
#     _name = 'project.issue.category'
#     _description = 'Category of Issues'
#     _columns = {
#         'issue_category': fields.char('categoria', size=60),
#         'category_id':fields.one2many('project_issue','category_id','Categoria')
#     }

# class company_assignment(osv.osv):
#     _name = 'res.company'
#     _inherit = 'res.company'
#     _columns = {
#         'company_id': fields.one2many('project.issue','company_id','Sucursal'),

#     }
    
