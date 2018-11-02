from django.conf import settings
from django.urls import (
    include,
    re_path,
)
import django.views.static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


import allauth.urls as allauth_urls
import rest_framework.urls as rest_framework_urls

import submission.urls as submission_urls
import manager.urls as manager_urls
import review.urls as review_urls
import api.urls as api_urls
import author.urls as author_urls
import editor.urls as editor_urls
import onetasker.urls as onetasker_urls
import swiftsubmit.urls as swiftsubmit_urls
import editorialreview.urls as editorialreview_urls
import django_summernote.urls as django_summernote_urls

from .views import (
    accept_proposal,
    activate,
    add_proposal_reviewers,
    assign_proposal,
    change_review_due_date,
    contact,
    contract_manager,
    dashboard,
    decline_proposal,
    delete_file,
    email_general,
    email_primary_contact,
    email_users,
    email_users_proposal,
    get_all,
    get_all_users,
    get_authors,
    get_editors,
    get_messages,
    get_onetaskers,
    get_proposal_users,
    index,
    login,
    login_orcid,
    logout,
    new_message,
    oai,
    overview,
    overview_inprogress,
    page,
    permission_denied,
    proposal,
    ProposalReviewCompletionEmail,
    proposal_add_editors,
    proposal_assign_edit,
    proposal_assign_user,
    proposal_assign_view,
    proposal_history,
    proposal_overview,
    proposal_review_declined,
    proposal_review_submitted,
    register,
    remove_proposal_review,
    reopen_proposal_review,
    RequestedReviewerDecisionEmail,
    request_proposal_revisions,
    reset_password,
    serve_all_files,
    serve_all_review_files,
    serve_all_review_files_one_click,
    serve_email_file,
    serve_file,
    serve_file_one_click,
    serve_marc21_file,
    serve_proposal_file_id,
    serve_versioned_file,
    start_proposal_review,
    switch_account,
    switch_account_user,
    task_complete,
    task_new,
    unauth_reset,
    unauth_reset_code,
    unauth_reset_password,
    update_file,
    update_profile,
    upload_additional,
    upload_manuscript,
    upload_misc_file,
    user_proposal,
    user_submission,
    versions_file,
    view_completed_proposal_review,
    view_file,
    view_log,
    view_profile,
    view_profile_readonly,
    view_proposal,
    view_proposal_log,
    view_proposal_review,
    view_proposal_review_decision,
    view_review_history,
    withdraw_proposal_review,
)

urlpatterns = [
    re_path(  # Core Site.
        r'^admin/',
        admin.site.urls
    ),
    re_path(
        r'^submission/',
        include(submission_urls)
    ),
    re_path(
        r'^manager/',
        include(manager_urls)
    ),
    re_path(
        r'^review/',
        include(review_urls)
    ),
    re_path(
        r'^api/',
        include(api_urls)
    ),
    re_path(
        r'^author/',
        include(author_urls)
    ),
    re_path(
        r'^editor/',
        include(editor_urls)
    ),
    re_path(
        r'^tasks/',
        include(onetasker_urls)
    ),
    re_path(
        r'^swiftsubmit/',
        include(swiftsubmit_urls)
    ),
    re_path(
        r'^editorialreview/',
        include(editorialreview_urls)
    ),
    re_path(  # 3rd Party Apps.
        r'^summernote/',
        include(django_summernote_urls)
    ),
    re_path(
        r'^accounts/',
        include(allauth_urls)
    ),
    re_path(
        r'^api-auth/',
        include(rest_framework_urls, namespace='rest_framework')
    ),
    re_path(  # Public pages.
        r'^$',
        index,
        name='index'
    ),
    re_path(
        r'^contact/$',
        contact,
        name='contact',
    ),
    re_path(
        r'^page/(?P<page_name>[-\w]+)/$',
        page,
        name='page',
    ),

    # Login/Register
    re_path(
        r'^login/$',
        login,
        name='login',
    ),
    re_path(
        r'^login/orcid/$',
        login_orcid,
        name='orcid-login',
    ),
    re_path(
        r'^logout/$',
        logout,
        name='logout',
    ),
    re_path(
         r'^switch/account/$',
         switch_account,
         name='switch-account',
    ),

    re_path(
        r'^switch/account/(?P<account_id>\d+)/$',
        switch_account_user,
        name='switch-account-user',
    ),
    re_path(
        r'^register/$',
        register,
        name='register',
    ),
    re_path(
        r'^login/activate/(?P<code>[-\w./]+)/$',
        activate,
        name='activate',
    ),
    re_path(  # Unauthenticated password reset.
        r'^login/reset/$',
        unauth_reset,
        name='unauth_reset',
    ),
    re_path(
        r'^login/reset/code/(?P<uuid>[\w-]+)/$',
        unauth_reset_code,
        name='unauth_reset_code',
    ),
    re_path(
        r'^login/reset/password/(?P<uuid>[\w-]+)/$',
        unauth_reset_password,
        name='unauth_reset_password',
    ),
    re_path(  # User profile.
        r'^user/profile/$',
        view_profile,
        name='view_profile',
    ),
    re_path(
        r'^user/view/(?P<user_id>\d+)/$',
        view_profile_readonly,
        name='view_profile_readonly',
    ),
    re_path(
        r'^user/review-history/(?P<user_id>\d+)/$',
        view_review_history,
        name='view_review_history',
    ),
    re_path(
        r'^user/profile/update/$',
        update_profile,
        name='update_profile',
    ),
    re_path(
        r'^user/profile/resetpassword/$',
        reset_password,
        name='reset_password',
    ),
    re_path(
        r'^user/task/new/$',
        task_new,
        name='task_new',
    ),
    re_path(
        r'^user/task/(?P<task_id>[-\w./]+)/complete/$',
        task_complete,
        name='task_complete',
    ),

    re_path(  # Message AJAX.
        r'^book/(?P<submission_id>\d+)/message/new/$',
        new_message,
        name='new_message',
    ),
    re_path(
        r'^book/(?P<submission_id>\d+)/messages/$',
        get_messages,
        name='get_messages',
    ),
    re_path(  # User submission.
        r'^user/submission/(?P<submission_id>\d+)/$',
        user_submission,
        name='user_submission',
    ),
    re_path(
        r'^user/proposal/(?P<proposal_id>\d+)/$',
        user_proposal,
        name='user_proposal',
    ),
    re_path(
        r'overview/$',
        overview,
        name='overview',
    ),
    re_path(
        r'overview/inprogress/$',
        overview_inprogress,
        name='overview_inprogress'
    ),
    re_path(
        r'overview/proposals/$',
        proposal_overview,
        name='proposal_overview',
    ),

    re_path(  # Email.
        r'^email/(?P<group>[-\w]+)/submission/(?P<submission_id>\d+)/$',
        email_users,
        name='email_users',
    ),
    re_path(
        r'^email/(?P<group>[-\w]+)/submission/(?P<submission_id>\d+)/'
        r'user/(?P<user_id>\d+)/$',
        email_users,
        name='email_user',
    ),
    re_path(
        r'^email/proposal/(?P<proposal_id>\d+)/user/(?P<user_id>\d+)/$',
        email_users_proposal,
        name='email_user_proposal',
    ),
    re_path(
        r'^email/primary-contact/$',
        email_primary_contact,
        name='email_primary_contact',
    ),

    re_path(
        r'^email/get/user/proposal/(?P<proposal_id>\d+)/$',
        get_proposal_users,
        name='get_proposal_users',
    ),
    re_path(
        r'^email/get/authors/submission/(?P<submission_id>\d+)/$',
        get_authors,
        name='get_authors',
    ),
    re_path(
        r'^email/get/editors/submission/(?P<submission_id>\d+)/$',
        get_editors,
        name='get_editors',
    ),
    re_path(
        r'^email/get/users/$',
        get_all_users,
        name='get_all_users',
    ),
    re_path(
        r'^email/get/onetaskers/submission/(?P<submission_id>\d+)/$',
        get_onetaskers,
        name='get_onetaskers',
    ),
    re_path(
        r'^email/get/all/submission/(?P<submission_id>\d+)/$',
        get_all,
        name='get_all',
    ),
    re_path(
        r'^email/general/$',
        email_general,
        name='email_general',
    ),
    re_path(
        r'^email/general/user/(?P<user_id>\d+)/$',
        email_general,
        name='email_general_user_id',
    ),
    re_path(  # Files.
        r'^files/submission/(?P<submission_id>\d+)/get/'
        r'marc21/(?P<type>[-\w]+)/$',
        serve_marc21_file,
        name='serve_marc21_file',
    ),
    re_path(
        r'^files/proposal/(?P<proposal_id>\d+)/file'
        r'/(?P<file_id>\d+)/download/$',
        serve_proposal_file_id,
        name='serve_proposal_file_id',
    ),

    re_path(
        r'^files/user/submission/(?P<submission_id>\d+)/file'
        r'/(?P<file_id>\d+)/download/review/(?P<review_id>\d+)'
        r'/access_key/(?P<access_key>[-\w+]+)/$',
        serve_file_one_click,
        name='serve_file_one_click'
    ),
    re_path(
        r'^files/user/submission/(?P<submission_id>\d+)/file'
        r'/(?P<file_id>\d+)/download/$',
        serve_file,
        name='serve_file',
    ),
    re_path(
        r'^files/user/submission/(?P<submission_id>\d+)/files/download/$',
        serve_all_files,
        name='serve_all_files',
    ),
    re_path(
        r'^files/user/email/file'
        r'/(?P<file_id>\d+)/download/$',
        serve_email_file,
        name='serve_email_file',
    ),
    re_path(
        r'^files/user/submission/(?P<submission_id>\d+)/review-files/'
        r'(?P<review_type>[-\w]+)/download/review/(?P<review_id>\d+)/'
        r'access_key/(?P<access_key>[-\w+]+)/$',
        serve_all_review_files_one_click,
        name='serve_all_review_files_one_click',
    ),
    re_path(
        r'^files/user/submission/(?P<submission_id>\d+)/review-files/'
        r'(?P<review_type>[-\w]+)/download/$',
        serve_all_review_files,
        name='serve_all_review_files',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/file/upload/additional/$',
        upload_additional,
        name='upload_additional',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/file/upload/manuscript/$',
        upload_manuscript,
        name='upload_manuscript',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/file/upload/manuscript/'
        r'(?P<editorial_review>[-\w]+)$',
        upload_manuscript,
        name='upload_manuscript_ed_review_redirect',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/file/(?P<revision_id>\d+)'
        r'/download_versioned_file/$',
        serve_versioned_file,
        name='serve_versioned_file',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/file/(?P<file_id>\d+)/'
        r'delete/returner/(?P<returner>[-\w]+)/$',
        delete_file,
        name='delete_file',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/file/'
        r'(?P<file_id>\d+)/view/$',
        view_file,
        name='view_file',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/file/(?P<file_id>\d+)/'
        r'update/returner/(?P<returner>[-\w]+)/$',
        update_file,
        name='update_file',
    ),
    re_path(
        r'^files/submission/(?P<submission_id>\d+)/'
        r'file/(?P<file_id>\d+)/versions/$',
        versions_file,
        name='versions_file',
    ),
    re_path(  # Log.
        r'^log/submission/(?P<submission_id>\d+)/',
        view_log,
        name='view_log',
    ),
    re_path(
        r'^log/proposal/(?P<proposal_id>\d+)/',
        view_proposal_log,
        name='view_proposal_log',
    ),
    re_path(  # Redirect to correct dashboard.
        r'^dashboard/$',
        dashboard,
        name='user_dashboard',
    ),
    re_path(
        r'^misc_files/(?P<submission_id>\d+)/upload/$',
        upload_misc_file,
        name='upload_misc_file',
    ),
    re_path(  # Proposals.
        r'^proposals/$',
        proposal,
        name='proposals',
    ),
    re_path(
        r'^proposals/filter/(?P<user_id>\d+)/$',
        proposal,
        name='proposals_filtered',
    ),
    re_path(
        r'^proposals/unassigned/$',
        assign_proposal,
        name='proposal_assign',
    ),
    re_path(
        r'^proposals/unassigned/(?P<proposal_id>\d+)/edit/$',
        proposal_assign_edit,
        name='proposal_assign_edit'
    ),
    re_path(
        r'^proposals/assign/(?P<proposal_id>\d+)/$',
        proposal_assign_view,
        name='proposal_assign_view_submitted',
    ),
    re_path(
        r'^proposals/assign/(?P<proposal_id>\d+)/(?P<user_id>\d+)/$',
        proposal_assign_user,
        name='proposal_assign_user',
    ),
    re_path(
        r'^proposals/history/$',
        proposal_history,
        name='proposals_history',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/$',
        view_proposal,
        name='view_proposal',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/add/editor/$',
        proposal_add_editors,
        name='proposal_add_editors',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/update/editor/$',
        proposal_add_editors,
        name='proposal_update_editors',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/review/start/$',
        start_proposal_review,
        name='start_proposal_review',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/review/add/$',
        add_proposal_reviewers,
        name='add_proposal_reviewers',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/decision/'
        r'(?P<assignment_id>\d+)/access_key/(?P<access_key>[-\w+]+)/$',
        view_proposal_review_decision,
        name='view_proposal_review_decision_access_key',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/'
        r'decision/(?P<assignment_id>\d+)/$',
        view_proposal_review_decision,
        name='view_proposal_review_decision',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/'
        r'(?P<assignment_id>\d+)/decision_email/(?P<decision>accept|decline)/$',
        RequestedReviewerDecisionEmail.as_view(),
        name='proposal_review_decision_email',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/'
        r'(?P<assignment_id>\d+)/decision_email/(?P<decision>accept|decline)/'
        r'access_key/(?P<access_key>[-\w+]+)/$',
        RequestedReviewerDecisionEmail.as_view(),
        name='proposal_review_decision_email_access_key',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/'
        r'(?P<assignment_id>\d+)/access_key/(?P<access_key>[-\w+]+)/$',
        view_proposal_review,
        name='view_proposal_review_access_key',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/(?P<assignment_id>\d+)/$',
        view_proposal_review,
        name='view_proposal_review',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/'
        r'(?P<assignment_id>\d+)/completion-email/'
        r'access_key/(?P<access_key>[-\w+]+)/$',
        ProposalReviewCompletionEmail.as_view(),
        name='proposal_review_completion_email_access_key',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/(?P<assignment_id>\d+)/'
        r'completion-email/$',
        ProposalReviewCompletionEmail.as_view(),
        name='proposal_review_completion_email',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/(?P<assignment_id>\d+)'
        r'/completed/$',
        view_completed_proposal_review,
        name='view_completed_proposal_review',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/remove/assignment/'
        r'(?P<review_id>\d+)/$',
        remove_proposal_review,
        name='remove_proposal_review',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/withdraw/assignment'
        r'/(?P<review_id>\d+)/$',
        withdraw_proposal_review,
        name='withdraw_proposal_review',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/'
        r'(?P<assignment_id>\d+)/reopen/$',
        reopen_proposal_review,
        name='reopen_proposal_review',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/assignment/'
        r'(?P<assignment_id>\d+)/due/$',
        change_review_due_date,
        name='change_review_due_date',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/accept/$',
        accept_proposal,
        name='accept_proposal',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/revisions/$',
        request_proposal_revisions,
        name='request_proposal_revisions',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/decline/$',
        decline_proposal,
        name='decline_proposal',
    ),
    re_path(
        r'^proposals/review-submitted/$',
        proposal_review_submitted,
        name='proposal_review_submitted',
    ),
    re_path(
        r'^proposals/review-declined/$',
        proposal_review_declined,
        name='proposal_review_declined',
    ),
    re_path(  # Contract.
        r'^proposals/(?P<proposal_id>\d+)/manage/contract/$',
        contract_manager,
        name='proposal_contract_manager',
    ),
    re_path(
        r'^proposals/(?P<proposal_id>\d+)/manage/'
        r'contract/(?P<contract_id>\d+)/$',
        contract_manager,
        name='proposal_contract_manager_edit',
    ),
    re_path(  # OAI - /oai?verb=ListRecords&metadataPrefix=oai_dc
        r'^oai/$',
        oai,
        name='oai',
    ),
]

# For cases when Gunicorn/uwsgi is used to serve static files
if settings.INCLUDE_STATIC_FILE_URLCONFS:
    urlpatterns += staticfiles_urlpatterns()

handler403 = permission_denied

# Allow Django to serve static content only in debug/dev mode.
if settings.DEBUG:
    urlpatterns += [
        re_path(
            r'^media/(?P<path>.*)$',
            django.views.static.serve,
            {'document_root': settings.MEDIA_ROOT}
        ),
        re_path(
            r'^404/$',
            TemplateView.as_view(template_name='404.html')
        ),
        re_path(
            r'^500/$',
            TemplateView.as_view(template_name='500.html')
        ),
    ]
