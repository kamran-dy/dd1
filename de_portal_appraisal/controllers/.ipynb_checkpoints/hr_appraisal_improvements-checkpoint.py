from . import config
from . import update
from collections import defaultdict
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.exceptions import UserError
from collections import OrderedDict
from operator import itemgetter
from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem
from odoo.osv.expression import OR
import ast
appraisal_improvements_list = []

def appraisal_improvements_page_content(flag = 0):
    global appraisal_improvements_list 
    managers = request.env['res.users'].search([('id','=',http.request.env.context.get('uid'))])
    employees = request.env['hr.employee'].search([('parent_id.user_id','=',http.request.env.context.get('uid'))])
    company_info = request.env['res.users'].search([('id','=',http.request.env.context.get('uid'))])
    return {
        'managers': managers,
        'employees' : employees,
        'appraisal_improvements_list': appraisal_improvements_list,
        'success_flag' : flag,
        'company_info': company_info,
    }

def paging(data, flag1 = 0, flag2 = 0):        
    if flag1 == 1:
        return config.list12
    elif flag2 == 1:
        config.list12.clear()
    else:
        k = []
        for rec in data:
            for ids in rec:
                config.list12.append(ids.id)  
                
                
class CreateImprovements(http.Controller):
    
    @http.route('/appraisal/improvement/create/',type="http", website=True, auth='user')
    def appraisal_improvement_template(self, **kw):
        global appraisal_improvements_list
        appraisal_improvements_list = []
        return request.render("de_portal_appraisal.create_appraisal_improvement",appraisal_improvements_page_content()) 
    
    
    @http.route('/appraisal/improvement/line/save',type="http", website=True, auth='user')
    def appraisal_improvements_template(self, **kw):
        global appraisal_improvements_list
        appraisal_val = {
            'performance_improvement_area': kw.get('performance_improvement_area'),
            'action_plan':  kw.get('action_plan'),
            'rating': kw.get('rating'),
        }
        appraisal_improvements_list.append(appraisal_val)
        return request.render("de_portal_appraisal.create_appraisal_improvement",appraisal_improvements_page_content())
    
    @http.route('/appraisal/improvement/save', type="http", auth="public", website=True)
    def create_appraisal_improvement(self, **kw):
        obj_line = []
        global appraisal_improvements_list
        for emp_improve in appraisal_improvements_list:
            obj_line.append((0,0,{
                'performance_improvement_area':  emp_improve['performance_improvement_area'],
                'action_plan':  emp_improve['action_plan'],
                'rating': emp_improve['rating'],
                }))
        improvement_val = {
            'follow_up_period': kw.get('follow_up_period'),
            'employee_id': int(kw.get('employee_id')),
            'follow_up_period': kw.get('follow_up_period'),
            'comments': kw.get('comments'),
            'appraisal_improve_line': obj_line,
        }
        record = request.env['hr.appraisal.improvements'].sudo().create(improvement_val)
        record.action_confirmed()
        appraisal_improvements_list = []
        return request.render("de_portal_appraisal.appraisal_submited", {})
    
    
    
                   
        
        
class CustomerPortal(CustomerPortal):
    
      
    
    def _improvement_get_page_view_values(self,improvement, edit_improvement,edit_emp_improvement, edit_hod_improvement, edit_hr_improvement, next_id = 0,pre_id= 0, improvement_user_flag = 0, access_token = None, **kwargs):
        company_info = request.env['res.users'].search([('id','=',http.request.env.context.get('uid'))])
        
        values = {
            'page_name' : 'improvement',
            'improvement' : improvement,
            'improvement_user_flag': improvement_user_flag,
            'next_id' : next_id,
            'edit_improvement': edit_improvement,
            'edit_emp_improvement': edit_emp_improvement,
            'edit_hod_improvement': edit_hod_improvement,
            'edit_hr_improvement': edit_hr_improvement,
            'company_info': company_info,
            'pre_id' : pre_id,
        }
        return self._get_page_view_values(improvement, access_token, values, 'my_improvement_history', False, **kwargs)

    
    @http.route(['/appraisal/improvements', '/appraisal/improvement/page/<int:page>'], type='http', auth="user", website=True)
    def portal_appraisal_improvements(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, search=None,
                         search_in='content', groupby=None, **kw):
        values = self._prepare_portal_layout_values()
        searchbar_sortings = {
            'id': {'label': _('Default'), 'order': 'id asc'},
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name desc' },
            'update': {'label': _('Last Update'), 'order': 'write_date desc'},
        }
        
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
            'draft': {'label': _('Draft'), 'domain': [('state', '=', 'draft')]},
            'waiting': {'label': _('Confirmed'), 'domain': [('state', '=', 'confirmed')]},  
            'confirmed': {'label': _('Waiting For Employee Review'), 'domain': [('state', '=', 'employee_waiting')]},
            'employee_review': {'label': _('Employee Review'), 'domain': [('state', '=', 'employee_review')]},
            'follow_up': {'label': _('Follow Up'), 'domain': [('state', '=', 'follow_up')]},
            'done': {'label': _('Done'), 'domain': [('state', '=', 'done')]},
        }
           
        searchbar_inputs = {
            'id': {'input': 'id', 'label': _('Search in No#')},
            'name': {'input': 'name', 'label': _('Search in Name')},
            'employee_id.name': {'input': 'employee_id.name', 'label': _('Search in Employee')}, 
            'all': {'input': 'all', 'label': _('Search in All')},
        }
        
        searchbar_groupby = {
            'none': {'input': 'none', 'label': _('None')},
        }

        appraisal_groups = request.env['hr.appraisal.improvements'].search([])

        # default sort by value
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        # default filter by value
        if not filterby:
            filterby = 'all'
        domain = searchbar_filters.get(filterby, searchbar_filters.get('all'))['domain']
#         domain = []
        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]       

        # search
        if search and search_in:
            search_domain = []
            if search_in in ('name', 'all'):
                search_domain = OR([search_domain, [('name', 'ilike', search)]])
            if search_in in ('id', 'all'):
                search_domain = OR([search_domain, [('id', 'ilike', search)]])
            if search_in in ('employee_id.name', 'all'):
                search_domain = OR([search_domain, [('employee_id.name', 'ilike', search)]])
            if search_in in ('state', 'all'):
                search_domain = OR([search_domain, [('state', 'ilike', search)]])
            domain += search_domain
        domain += ['|',('employee_id.user_id', '=', http.request.env.context.get('uid')),('employee_id.parent_id.user_id', '=', http.request.env.context.get('uid'))]
        improvements_count = request.env['hr.appraisal.improvements'].search_count(domain)

        pager = portal_pager(
            url="/appraisal/improvements",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby, 'filterby': filterby,
                      'search_in': search_in, 'search': search},
            total=improvements_count,
            page=page,
            step=self._items_per_page
        )

        _improvements = request.env['hr.appraisal.improvements'].search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_improvement_history'] = _improvements.ids[:100]

        grouped_improvements = [_improvements]
                
        paging(0,0,1)

        paging(grouped_improvements)
        company_info = request.env['res.users'].search([('id','=',http.request.env.context.get('uid'))])
        values.update({
            'date': date_begin,
            'date_end': date_end,
            'grouped_improvements': grouped_improvements,
            'page_name': 'improvement',
            'default_url': '/appraisal/improvements',
            'pager': pager,
            'company_info': company_info,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'search': search,
            'sortby': sortby,
            'groupby': groupby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
        })
        return request.render("de_portal_appraisal.portal_appraisal_imrovements", values)

   
    @http.route(['/appraisal/improvement/<int:improvement_id>'], type='http', auth="user", website=True)
    def portal_appraisal_improvement(self, improvement_id, access_token=None, **kw):
        values = []
        active_user = http.request.env.context.get('uid')
        improvement_user = []
        id = improvement_id
        try:
            improvement_sudo = self._document_check_access('hr.appraisal.improvements', improvement_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')        

        improvement_user_flag = 0
                
        improvement_id_list = paging(0,1,0)
        next_id = 0
        pre_id = 0
        next_next_id = 0
        improvement_id_list.sort()
        length_list = len(improvement_id_list)
        length_list = length_list - 1
        if length_list != 0:
            if improvement_id in improvement_id_list:
                improvement_id_loc = improvement_id_list.index(improvement_id)
                if improvement_id_loc == 0:
                    next_id = 1
                    pre_id = 0
                elif improvement_id_loc == length_list:
                    next_id = 0
                    pre_id = 1
                else:
                    next_id = 1
                    pre_id = 1
        else:
            next_id = 0
            pre_id = 0
            
        edit_improvement = False
        edit_emp_improvement = False
        edit_hod_improvement = False
        edit_hr_improvement = False
        values = self._improvement_get_page_view_values(improvement_sudo,edit_improvement,edit_emp_improvement, edit_hod_improvement, edit_hr_improvement,next_id, pre_id, improvement_user_flag,access_token, **kw) 
        return request.render("de_portal_appraisal.portal_appraisal_improvement", values)
    
    
    # Appraisal Edit improvement
    
    @http.route(['/appraisal/edit/improvement/<int:improvement_id>'], type='http', auth="user", website=True)
    def edit_portal_appraisal_improvement(self, improvement_id, access_token=None, **kw):
        values = []
        active_user = http.request.env.context.get('uid')
        improvement_user = []
        id = improvement_id
        try:
            improvement_sudo = self._document_check_access('hr.appraisal.improvements', improvement_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')        

        improvement_user_flag = 0
                
        improvement_id_list = paging(0,1,0)
        next_id = 0
        pre_id = 0
        next_next_id = 0
        improvement_id_list.sort()
        length_list = len(improvement_id_list)
        length_list = length_list - 1
        if length_list != 0:
            if improvement_id in improvement_id_list:
                improvement_id_loc = improvement_id_list.index(improvement_id)
                if improvement_id_loc == 0:
                    next_id = 1
                    pre_id = 0
                elif improvement_id_loc == length_list:
                    next_id = 0
                    pre_id = 1
                else:
                    next_id = 1
                    pre_id = 1
        else:
            next_id = 0
            pre_id = 0
            
        edit_improvement = False
        edit_emp_improvement = False
        edit_hod_improvement = False
        edit_hr_improvement = False    
        
        values = self._improvement_get_page_view_values(improvement_sudo, edit_improvement,edit_emp_improvement, edit_hod_improvement, edit_hr_improvement,next_id, pre_id, improvement_user_flag,access_token, **kw) 
        return request.render("de_portal_appraisal.portal_appraisal_improvement", values)

    

    @http.route(['/improvement/next/<int:improvement_id>'], type='http', auth="user", website=True)
    def portal_improvement_next(self, improvement_id, access_token=None, **kw):
        
        improvement_id_list = paging(0,1,0)
        next_next_id = 0
        improvement_id_list.sort()
        
        length_list = len(improvement_id_list)
        if length_list == 0:
            return request.redirect('/my')
        length_list = length_list - 1
        
        if improvement_id in improvement_id_list:
            improvement_id_loc = improvement_id_list.index(improvement_id)
            next_next_id = improvement_id_list[improvement_id_loc + 1] 
            next_next_id_loc = improvement_id_list.index(next_next_id)
            if next_next_id_loc == length_list:
                next_id = 0
                pre_id = 1
            else:
                next_id = 1
                pre_id = 1      
        else:
            buffer_larger = 0
            buffer_smaller = 0
            buffer = 0
            for ids in improvement_id_list:
                if ids < improvement_id:
                    buffer_smaller = ids
                if ids > improvement_id:
                    buffer_smaller = ids
                if buffer_larger and buffer_smaller:
                    break
            if buffer_larger:
                next_next_id = buffer_smaller
            elif buffer_smaller:
                next_next_id = buffer_larger
                
            next_next_id_loc = improvement_id_list.index(next_next_id)
            length_list = len(improvement_id_list)
            length_list = length_list + 1
            if next_next_id_loc == length_list:
                next_id = 0
                pre_id = 1
            elif next_next_id_loc == 0:
                next_id = 1
                pre_id = 0
            else:
                next_id = 1
                pre_id = 1
         
        values = []
        active_user = http.request.env.context.get('uid')
        improvement_user = []
        id = improvement_id
        try:
            improvement_sudo = self._document_check_access('hr.appraisal.improvements', next_next_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        
        improvement_user_flag = 0

        edit_improvement = False
        edit_emp_improvement = False
        edit_hod_improvement = False
        edit_hr_improvement = False
        values = self._improvement_get_page_view_values(improvement_sudo, edit_improvement,edit_emp_improvement, edit_hod_improvement, edit_hr_improvement,next_id, pre_id, access_token, **kw) 
        return request.render("de_portal_appraisal.portal_appraisal_improvement", values)

  
    @http.route(['/improvement/pre/<int:improvement_id>'], type='http', auth="user", website=True)
    def portal_improvement_previous(self, improvement_id, access_token=None, **kw):
        
        improvement_id_list = paging(0,1,0)
        pre_pre_id = 0
        improvement_id_list.sort()
        length_list = len(improvement_id_list)
    
        if length_list == 0:
            return request.redirect('/my')
        
        length_list = length_list - 1
        if improvement_id in improvement_id_list:
            improvement_id_loc = improvement_id_list.index(improvement_id)
            pre_pre_id = improvement_id_list[improvement_id_loc - 1] 
            pre_pre_id_loc = improvement_id_list.index(improvement_id)

            if improvement_id_loc == 1:
                next_id = 1
                pre_id = 0
            else:
                next_id = 1
                pre_id = 1      
        else:
            buffer_larger = 0
            buffer_smaller = 0
            buffer = 0
            for ids in improvement_id_list:
                if ids < improvement_id:
                    buffer_smaller = ids
                if ids > improvement_id:
                    buffer_smaller = ids
                if buffer_larger and buffer_smaller:
                    break
            if buffer_smaller:
                pre_pre_id = buffer_smaller
            elif buffer_larger:
                pre_pre_id = buffer_larger
                
            pre_pre_id_loc = improvement_id_list.index(pre_pre_id)
            length_list = len(improvement_id_list)
            length_list = length_list -1
            if pre_pre_id_loc == 0:
                next_id = 1
                pre_id = 0
            elif pre_pre_id_loc == length_list:
                next_id = 0
                pre_id = 1
            else:
                next_id = 1
                pre_id = 1
   
        values = []
        active_user = http.request.env.context.get('uid')
        improvement_user = []
        id = pre_pre_id
        try:
            improvement_sudo = self._document_check_access('hr.appraisal.improvements', pre_pre_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        
        improvement_user_flag = 0
        edit_improvement = False
        edit_emp_improvement = False
        edit_hod_improvement = False
        edit_hr_improvement = False
        values = self._improvement_get_page_view_values(improvement_sudo,edit_improvement,edit_emp_improvement, edit_hod_improvement, edit_hr_improvement, next_id,pre_id, access_token, **kw) 
        return request.render("de_portal_appraisal.portal_appraisal_improvement", values)
    
##############################