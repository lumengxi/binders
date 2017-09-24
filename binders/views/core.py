from flask import render_template, redirect, g
from flask_appbuilder import BaseView, ModelView, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from binders import app, appbuilder, db

from binders.models.core import DocumentType, RepositoryOwner, Repository, RepositoryLang, Document
from binders.utils.repos import get_repo_doc_details


class Binders(BaseView):

    @expose('/health')
    def health(self):
        return "OK"

    @app.errorhandler(404)
    def page_not_found(self):
        return render_template('404.html',
                               base_template=appbuilder.base_template,
                               appbuilder=appbuilder), 404

    @expose("/welcome")
    def welcome(self):
        """Personalized welcome page"""
        if not g.user or not g.user.get_id():
            return redirect(appbuilder.get_url_for_login)
        return self.render_template(
            'binders/welcome.html', entry='welcome')


class DocumentTypeView(ModelView):
    datamodel = SQLAInterface(DocumentType)
    list_columns = ['name', 'created_by']
    show_columns = add_columns = edit_columns = ['name']


class RepositoryOwnerView(ModelView):
    datamodel = SQLAInterface(RepositoryOwner)
    list_columns = ['name', 'created_by']
    show_columns = add_columns = edit_columns = ['name']


class DocumentView(ModelView):
    datamodel = SQLAInterface(Document)
    list_columns = ['name', 'is_active', 'document_type.name', 'created_by', 'created_at', 'updated_at']
    show_columns = add_columns = edit_columns = ['name', 'is_active', 'document_type',
                                                 'doc_gen_script', 'doc_html_location']

    base_order = ('is_active', 'desc')


class RepositoryLangView(ModelView):
    datamodel = SQLAInterface(RepositoryLang)
    list_columns = ['name', 'created_by']
    show_columns = add_columns = edit_columns = ['name']


class RepositoryView(ModelView):
    datamodel = SQLAInterface(Repository)

    list_columns = ['name', 'updated_at', 'repo_owner', 'documents']

    list_fieldsets = add_fieldsets = edit_fieldsets = [
        ('Summary',
         {
             'fields': ['name', 'url', 'repo_lang', 'branch', 'repo_owner', 'notes']
          }),
        ('Documents',
         {
             'fields': ['documents']
         })
    ]


class RepositoryDocumentView(BaseView):
    route_base = '/RepositoryDocumentView'
    default_view = 'repo_docs'

    @expose('/repo_docs/')
    def repo_docs(self):
        return self.render_template(
            'binders/dashboard.html',
            repo_doc_details=get_repo_doc_details()
        )


db.create_all()

appbuilder.add_view_no_menu(Binders)

appbuilder.add_view(RepositoryDocumentView, 'Dashboard')

appbuilder.add_view(RepositoryView,
                    'Repositories',
                    icon='fa-github',
                    category='Admin')

appbuilder.add_view(RepositoryOwnerView,
                    'Repository Owner',
                    icon='fa-user',
                    category='Admin')

appbuilder.add_view(RepositoryLangView,
                    'Repository Language',
                    icon='fa-user',
                    category='Admin')

appbuilder.add_separator(category='Admin')

appbuilder.add_view(DocumentTypeView,
                    'Document Type',
                    icon='fa-file-text-o',
                    category='Admin')

appbuilder.add_view(DocumentView,
                    'Document',
                    icon='fa-files-o',
                    category='Admin')
