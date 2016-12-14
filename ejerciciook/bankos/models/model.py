from datetime import datetime, timedelta
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import SUPERUSER_ID



class bankos(osv.osv):
	_name= 'bankos'
	_inherit='res.partner.bank'
	
bankos()
	
