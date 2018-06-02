from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView

from views import SelectEmp,NewRegistration,NewDept,ShowEmployees,ApplyLeave,EmpHomeView,NewLeaveType,MyProfileView,ShowDept,ShowDeptAllLeaves
from views import ShowEmployeesByDept,ShowDeptLeaveRequests,EmployeeEdit,LoginView,DeptHeadHomeView,AssignEmpHead,ShowAllLeaveRequests,LeaveApprove,LeaveReject,MyLeaveStatus,CancelLeave,AdminHomeView,EmployeeDelete,DeleteDept


admin.autodiscover()

urlpatterns = patterns('',

	# url(r'^home/', HomeView.as_view(), name='home'),
	# url(r'^employeeregister/', NewEmployeeRegistration.as_view(), name='new_register'),
	url(r'^newemployeeregister/', NewRegistration.as_view(), name='new_register'),
	url(r'^emp-details/list/$', ShowEmployees.as_view(), name='employee_show'),

	url(r'^newdepartment/', NewDept.as_view(), name='new_dept'),


	url(r'^new_emphead/',AssignEmpHead.as_view(),name='assign_head'),
	url(r'^dept_head/',SelectEmp.as_view(),name='dept_head'),
	url(r'^dept_leave-requests/list/$', ShowDeptLeaveRequests.as_view(), name='dept_leave_request_show'),
	url(r'^dept_all_leaves/',ShowDeptAllLeaves.as_view(),name='dept_all_leaves'),
	url(r'^dept_all_employees/',ShowEmployeesByDept.as_view(),name='dept_all_employees'),




	url(r'^newleavetype/', NewLeaveType.as_view(), name='new_leave_type'),
	url(r'^showdepartment/', ShowDept.as_view(), name='show_dept'),

	url(r'^leave_request/list/$', ShowAllLeaveRequests.as_view(), name='leave_request_show'),
	# url(r'^new_leave_request/list/$', ShowNewLeaveRequests.as_view(), name='new_leave_requests'),

	url(r'^leave_approval/([a-zA-Z0-9_-]+)/$',LeaveApprove.as_view(),name='approve_leave'),
    url(r'^leave_reject/([a-zA-Z0-9_-]+)/$',LeaveReject.as_view(),name='reject_leave'),
    # url(r'^leave_delete/([a-zA-Z0-9_-]+)/$',LeaveDelete.as_view(),name='delete_leave'),
    url(r'^employee_delete/([a-zA-Z0-9_-]+)/$',EmployeeDelete.as_view(),name='delete_emp'),
    url(r'^dept_delete/([a-zA-Z0-9_-]+)/$',DeleteDept.as_view(),name='delete_department'),

    url(r'^emp_edit/([a-zA-Z0-9_-]+)/$',EmployeeEdit.as_view(),name='edit_emp'),

    url(r'^cancel_leave/([a-zA-Z0-9_-]+)/$',CancelLeave.as_view(),name='cancel_leave'),


	url(r'^admin/home/', AdminHomeView.as_view(), name='admin_home'),
	url(r'^head/home/', DeptHeadHomeView.as_view(), name='head_home'),
	url(r'^employee/home/', EmpHomeView.as_view(), name='emp_home'),



	
	url(r'^leave_request/$', ApplyLeave.as_view(), name='apply_leave'),
	

	url(r'^myprofile/$', MyProfileView.as_view(),name='my_profile'),

	url(r'^myleave_status/$',MyLeaveStatus.as_view() ,name='emp_leave_status'),

	url(r'^login/$', 'django.contrib.auth.views.login' ,name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/leave/login/'},name='logged_out'),



)

